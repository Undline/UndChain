# renderers/kivy_builders/checkitem_builder.py
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex
from kivy.resources import resource_find
from typing import Any, Dict
import os

# reuse the size parser from frame_builder
try:
    from .frame_builder import _parse_size
except ImportError:
    from frame_builder import _parse_size


def build_checkitem(widget: Dict[str, Any], renderer: Any = None) -> BoxLayout:
    """
    Kivy builder for 'checkitem' widgets: renders a CheckBox alongside a Label,
    supports custom images and style keys for spacing, box-size, label-color, font-size, font-name, bold.
    """
    style = widget.get('style', {}) or {}

    # Container with custom spacing and auto-sizing
    spacing = _parse_size(style.get('spacing', '8px'))
    container = BoxLayout(
        orientation='horizontal',
        spacing=spacing,
        size_hint=(None, None)
    )
    container.bind(
        minimum_width=lambda inst, val: setattr(inst, 'width', val),   # type: ignore
        minimum_height=lambda inst, val: setattr(inst, 'height', val)  # type: ignore
    )

    # Checkbox size
    box_size = _parse_size(style.get('box-size', '30px'))
    chk = CheckBox(
        active=bool(widget.get('checked', False)),
        size_hint=(None, None),
        size=(box_size, box_size)
    )

    # Custom images override if provided
    def apply_image(prop_normal, prop_down, key):
        path = style.get(key)
        if not path:
            return
        # try resource_find
        real = resource_find(path) or path
        if os.path.exists(real):
            setattr(chk, prop_normal, real)
            setattr(chk, prop_down, real)
        else:
            print(f"Warning: checkitem image '{path}' not found at '{real}'")
    # check-image sets both states
    apply_image('background_checkbox_normal','background_checkbox_down','check-image')
    # specific normal/down
    apply_image('background_checkbox_normal','background_checkbox_down','check-image-normal')
    apply_image('background_checkbox_down','background_checkbox_down','check-image-down')

    # Bind toggle intent
    def on_active(inst, val):
        if renderer:
            renderer.on_intent('toggle', {'id': widget.get('id'), 'checked': val})
    chk.bind(active=on_active)  # type: ignore
    container.add_widget(chk)

    # Label font, styles and auto-size
    lbl = Label(
        text=widget.get('label', ''),
        size_hint=(None, None)
    )
    # Font size
    if style.get('font-size'):
        lbl.font_size = _parse_size(style['font-size'])  # type: ignore
    # Font name
    if style.get('font-name'):
        lbl.font_name = style['font-name']               # type: ignore
    # Bold via markup
    if style.get('bold'):
        lbl.markup = True  # type: ignore
        lbl.text = f"[b]{lbl.text}[/b]"
    # Label color
    if style.get('label-color'):
        lbl.color = get_color_from_hex(style['label-color'])  # type: ignore
    lbl.bind(texture_size=lambda inst, val: setattr(inst, 'size', val))  # type: ignore
    container.add_widget(lbl)

    return container


if __name__ == "__main__":
    # Test four variations: image both, image normal/down, font-size, font-name+bold
    from kivy.uix.floatlayout import FloatLayout
    from kivy.base import runTouchApp

    print("Testing styled checkitems (4 samples) …")
    test_defs = [
        # 1. Single image
        {
            'id': 'c1', 'label': 'Normal', 'checked': True,
            'style': {}
        },
        # 2. Separate off/on images
        {
            'id': 'c2', 'label': 'Custom Check Box', 'checked': False,
            'style': {
                'check-image-normal': 'assets/checkbox_off_orange.png',
                'check-image-down':   'assets/checkbox_on_orange.png'
            }
        },
        # 3. Font size change
        {
            'id': 'c3', 'label': 'Large Font', 'checked': True,
            'style': {'font-size': '24px'}
        },
        # 4. Font name + bold
        {
            'id': 'c4', 'label': 'Bold Font', 'checked': False,
            'style': {'bold': True, 'font-size': '24px'}
        }
    ]
    positions = [
        {'center_x': 0.2, 'center_y': 0.8},
        {'center_x': 0.8, 'center_y': 0.8},
        {'center_x': 0.2, 'center_y': 0.2},
        {'center_x': 0.8, 'center_y': 0.2}
    ]
    root = FloatLayout()
    for defn, pos in zip(test_defs, positions):
        chk = build_checkitem(defn)
        chk.pos_hint = pos
        root.add_widget(chk)
    runTouchApp(root)
