# kivy_renderer.py
from typing import Dict, Any, List
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from .base import BaseRenderer

class KivyRenderer(BaseRenderer):
    def __init__(self):
        super().__init__()
        self.app = None
        self.widget_tree = []

    def setup(self):
        print("KivyRenderer: setup called")

    def render_widget_tree(self, widget_tree: List[Dict[str, Any]]) -> None:
        print("KivyRenderer: render_widget_tree called")
        self.widget_tree = widget_tree

        # Kivy typically wants an App with a build() method returning the root layout.
        # So we might define an inner class or something. For simplicity:
        class M3LApp(App):
            def build(app_self):
                root = BoxLayout(orientation='vertical', padding=10, spacing=10)
                for w in widget_tree:
                    kv = self.create_kivy_widget(w)
                    if kv:
                        root.add_widget(kv)
                return root

        self.app = M3LApp()
        self.app.run()

    def teardown(self):
        print("KivyRenderer: teardown called")

    def update(self, dt: float):
        # If you want real-time updates or any special scheduling
        pass

    def on_intent(self, intent_name: str, widget_info: Dict[str, Any]) -> None:
        print(f"KivyRenderer: on_intent '{intent_name}' triggered by {widget_info.get('id')}")
        # Possibly do something with widget references if you store them

    def update_widget(self, widget_info: Dict[str, Any]) -> None:
        print("KivyRenderer: partial widget update not fully implemented yet")

    def create_kivy_widget(self, widget: Dict[str, Any]):
        """
        Actually convert a single M3L widget dict into a Kivy Widget
        """
        wtype = widget.get("type")
        label = widget.get("label","")
        content = widget.get("content","")
        checked = widget.get("checked",False)

        if wtype == "paragraph":
            lbl = Label(text=content)
            return lbl
        elif wtype == "checkitem":
            # Maybe a Button that toggles text from [ ] to [X]
            mark = "[X]" if checked else "[ ]"
            btn = Button(text=f"{mark} {label}")
            # You could do btn.bind(on_press=...) to call self.on_intent
            return btn
        elif wtype == "frame":
            box = BoxLayout(orientation='vertical')
            # If we want to sub-render inside a frame, we can do so:
            # or rely on the top-level logic to flatten. For now, assume top-level.
            box.add_widget(Label(text=f"Frame: {widget.get('id','')}"))
            return box
        else:
            # fallback
            return Label(text=f"{wtype}: {label or content}")
