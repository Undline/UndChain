from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from typing import Any, Dict


def build_checkitem(widget: Dict[str, Any], renderer: Any = None) -> BoxLayout:
    """
    Kivy builder for 'checkitem' widgets: renders a CheckBox alongside a Label,
    auto-sizes its container around its contents.
    """
    container = BoxLayout(orientation='horizontal', spacing=8)
    container.size_hint_x = None
    container.size_hint_y = None
    container.bind( # type: ignore
        minimum_width=lambda inst, val: setattr(inst, 'width', val),  # type: ignore
        minimum_height=lambda inst, val: setattr(inst, 'height', val)  # type: ignore
    ) 

    checked = bool(widget.get('checked', False))
    chk = CheckBox(active=checked, size_hint=(None, None), size=(30, 30))

    def on_active(instance, value) -> None:
        if renderer:
            renderer.on_intent('toggle', {'id': widget.get('id'), 'checked': value})
    chk.bind(active=on_active)  # type: ignore
    container.add_widget(chk)

    lbl = Label(text=widget.get('label', ''), size_hint=(None, None))
    lbl.bind(texture_size=lambda inst, val: setattr(inst, 'size', val))  # type: ignore
    container.add_widget(lbl)

    return container


if __name__ == "__main__":
    # Test multiple instances and positioning
    from kivy.uix.floatlayout import FloatLayout
    from kivy.base import runTouchApp

    print("Testing multiple build_checkitem instances...")
    test_defs = [
        {'id': 'c1', 'label': 'Option A', 'checked': False},
        {'id': 'c2', 'label': 'Option B', 'checked': True},
        {'id': 'c3', 'label': 'Option C', 'checked': False},
        {'id': 'c4', 'label': 'Option D', 'checked': True},
    ]

    root = FloatLayout()
    positions: list[dict[str, float]] = [
        {'center_x': 0.25, 'center_y': 0.75},
        {'center_x': 0.75, 'center_y': 0.75},
        {'center_x': 0.25, 'center_y': 0.25},
        {'center_x': 0.75, 'center_y': 0.25},
    ]

    for defn, pos in zip(test_defs, positions):
        chk: BoxLayout = build_checkitem(defn)
        chk.pos_hint = pos
        root.add_widget(chk)

    runTouchApp(root)
