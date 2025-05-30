# ---------------------------------------------------------------------------
# renderers/kivy_renderer.py
# ---------------------------------------------------------------------------
from typing import Any, Dict, List
from kivy.app import App
from .base import BaseRenderer
# Central registry of Kivy builders (one builder per widget type)
from .kivy_builders.builder_registry import KIVY_BUILDERS

class KivyRenderer(BaseRenderer):
    """
    Modular Kivy renderer: delegates widget construction to builder functions,
    then recursively adds child widgets.
    """
    def setup(self) -> None:
        print("KivyRenderer: setup called")

    def teardown(self) -> None:
        print("KivyRenderer: teardown called")

    def render_widget_tree(self, widget_tree: List[Dict[str, Any]]) -> None:
        # Expect first entry to be the root frame
        root_def = widget_tree[0]

        # Build Kivy widget hierarchy
        root_widget = self._build_node(root_def)

        # Wrap in App
        class M3LApp(App):
            def build(inner):
                return root_widget

        self.app = M3LApp()
        self.app.run()

    def _build_node(self, widget: Dict[str, Any]) -> Any:
        """
        Lookup the builder for this widget type, build it, then attach children.
        """
        wtype = widget.get('type', 'unknown')
        builder = KIVY_BUILDERS.get(wtype)
        if not builder:
            raise ValueError(f"No Kivy builder registered for '{wtype}'")

        # Builder signature: build_fn(widget_info: dict, renderer: KivyRenderer) -> Kivy Widget
        try:
            kivy_widget = builder(widget, self)
        except TypeError:
            # fallback if builder only expects (widget)
            kivy_widget = builder(widget)

        # Recursively add any nested widget lists
        for subkey, subval in widget.items():
            if (
                isinstance(subval, list)
                and subval
                and isinstance(subval[0], dict)
                and 'type' in subval[0]
            ):
                for child_def in subval:
                    # build child and add to container if possible
                    child_widget = self._build_node(child_def)
                    if hasattr(kivy_widget, 'add_widget'):
                        kivy_widget.add_widget(child_widget)
        return kivy_widget

    def on_intent(self, intent_name: str, widget_info: Dict[str, Any]) -> None:
        print(f"KivyRenderer: intent '{intent_name}' from '{widget_info.get('id', '<no-id>')}'")
        # TODO: dispatch to business logic

    def update(self, dt: float) -> None:
        # No real-time loop by default
        pass

    def update_widget(self, widget_info: Dict[str, Any]) -> None:
        # Partial updates can be no-ops or small in-place tweaks
        print(f"KivyRenderer: update_widget called for {widget_info}")
