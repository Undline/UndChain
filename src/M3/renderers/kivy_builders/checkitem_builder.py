from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from typing import Any, Dict


def build_checkitem(widget: Dict[str, Any], renderer: Any = None) -> BoxLayout:
    """
    Kivy builder for 'checkitem' widgets: renders a CheckBox alongside a Label.

    :param widget: dict with keys 'id', 'label', 'checked'
    :param renderer: optional KivyRenderer for dispatching intents
    """
    # Horizontal container for checkbox + label
    container = BoxLayout(orientation='horizontal', spacing=8)

    # Create the checkbox with fixed size
    checked = bool(widget.get('checked', False))
    chk = CheckBox(active=checked, size_hint=(None, None), size=(30, 30))

    # Bind state change to an intent, if provided
    def on_active_change(instance, value):
        if renderer:
            renderer.on_intent('toggle', {'id': widget.get('id'), 'checked': value})
    chk.bind(active=on_active_change)  # type: ignore
    container.add_widget(chk)

    # Create the label next to it, auto-sizing to text width
    label_text = widget.get('label', '')
    lbl = Label(text=label_text, size_hint_x=None)
    lbl.bind(texture_size=lambda instance, size: setattr(instance, 'width', size[0]))  # type: ignore
    container.add_widget(lbl)

    return container


if __name__ == "__main__":
    # Basic test of the checkitem builder
    print("Testing build_checkitem in standalone mode...")
    test_def = {'id': 'remember_me', 'label': 'Remember Me?', 'checked': True}
    widget = build_checkitem(test_def)
    print(f"Built container of type: {type(widget)}, children: {widget.children}")
    from kivy.base import runTouchApp
    runTouchApp(widget)
