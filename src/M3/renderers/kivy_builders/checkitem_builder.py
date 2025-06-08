from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from typing import Any, Dict


def build_checkitem(widget: Dict[str, Any], renderer: Any = None) -> BoxLayout:
    """
    Kivy builder for 'checkitem' widgets: renders a CheckBox alongside a Label.
    """
    # Horizontal container that will shrink to its contents
    container = BoxLayout(orientation='horizontal', spacing=8)
    container.size_hint_x = None
    # Bind the minimum_width to width so it auto-sizes
    container.bind(minimum_width=lambda inst, val: setattr(inst, 'width', val))  # type: ignore

    # Create the checkbox with fixed size
    checked = bool(widget.get('checked', False))
    chk = CheckBox(active=checked, size_hint=(None, None), size=(30, 30))
    # Bind toggle intent
    def on_active(instance, value):
        if renderer:
            renderer.on_intent('toggle', {'id': widget.get('id'), 'checked': value})
    chk.bind(active=on_active)  # type: ignore
    container.add_widget(chk)

    # Create the label and auto-size to its text
    lbl = Label(text=widget.get('label', ''), size_hint=(None, None))
    lbl.bind(texture_size=lambda inst, val: setattr(inst, 'size', val))  # type: ignore
    container.add_widget(lbl)

    return container

if __name__ == "__main__":
    print("Testing build_checkitem in standalone mode...")
    test_def = {'id': 'remember_me', 'label': 'Remember Me?', 'checked': True}
    widget = build_checkitem(test_def)
    print(f"Built container: {type(widget)}, children count: {len(widget.children)}")
    from kivy.base import runTouchApp
    runTouchApp(widget)
