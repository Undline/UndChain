from typing import Any, Dict, List
from .base import BaseRenderer
# The aggregator registry
from .text_builders.registry import TEXT_BUILDERS

class TextRenderer(BaseRenderer):
    def __init__(self):
        super().__init__()
        self.widget_lines = {}

    def setup(self) -> None:
        print("TextRenderer: setup called")

    def render_widget_tree(self, widget_tree: List[Dict[str, Any]]) -> None:
        print("\n-- TextRenderer: Rendering Widget Tree --\n")
        line_num = 0
        for widget in widget_tree:
            wtype = widget.get("type", "unknown")

            # 1) Look up the builder function
            builder = TEXT_BUILDERS.get(wtype)
            if builder:
                line_str = builder(widget)
            else:
                # Fallback if no builder found
                line_str = f"{wtype}: ??? (no builder found)"

            print(line_str)

            # 2) Store a line reference for partial updates
            widget_id = widget.get("id")
            if widget_id:
                self.widget_lines[widget_id] = line_num
            line_num += 1

        print("\n-- End of Widget Tree --")

    def teardown(self) -> None:
        print("TextRenderer: teardown called\n")

    def update(self, dt: float) -> None:
        """
        If you had a loop-based or real-time approach,
        you might do something here. Currently, do nothing.
        """
        pass

    def on_intent(self, intent_name: str, widget_info: Dict[str, Any]) -> None:
        w_id = widget_info.get("id", "<no-id>")
        print(f"TextRenderer: on_intent('{intent_name}') triggered by widget '{w_id}'")

    def update_widget(self, widget_info: Dict[str, Any]) -> None:
        """
        Partial update for a single widget. We'll re-print that line only.
        """
        w_id = widget_info.get("id")
        if w_id not in self.widget_lines:
            print(f"TextRenderer: No line reference for widget {w_id}; can't partial update.")
            return

        line_num = self.widget_lines[w_id]
        wtype = widget_info.get("type", "unknown")

        builder = TEXT_BUILDERS.get(wtype)
        if builder:
            new_str = builder(widget_info)
        else:
            new_str = f"{wtype}: ??? (no builder found)"

        print(f"TextRenderer: Updating line {line_num} to: {new_str}")
