# ---------------------------------------------------------------------------
# renderers/text_renderer.py
# ---------------------------------------------------------------------------
from typing import Any, Dict, List

from .base import BaseRenderer
# Central registry of text builders
from .text_builders.builder_registry import TEXT_BUILDERS

class TextRenderer(BaseRenderer):
    """
    Recursive, builder-driven text renderer.

    Public API (setup / render_widget_tree / teardown) unchanged.
    """

    INDENT_STEP = 2  # spaces to indent per nesting level

    def __init__(self) -> None:
        super().__init__()
        self.widget_lines: Dict[str, int] = {}  # map widget_id to printed line
        self._current_line: int = 0

    def setup(self) -> None:
        print("TextRenderer: setup called")

    def teardown(self) -> None:
        print("TextRenderer: teardown called\n")

    def render_widget_tree(self, widget_tree: List[Dict[str, Any]]) -> None:
        print("\n-- TextRenderer: Rendering Widget Tree --\n")
        self.widget_lines.clear()
        self._current_line = 0
        for widget in widget_tree:
            self._render_subtree(widget, indent=0)
        print("\n-- End of Widget Tree --")

    def _render_subtree(self, widget: Dict[str, Any], indent: int) -> None:
        wtype = widget.get("type", "unknown")
        builder = TEXT_BUILDERS.get(wtype)

        if builder:
            # Attempt positional call first, then fallback to (widget, renderer)
            try:
                line_str = builder(widget)
            except TypeError:
                line_str = builder(widget, self)
        else:
            line_str = f"{wtype}: ??? (no builder registered)"

        padded = " " * indent + line_str
        print(padded)

        # record line for partial updates
        wid = widget.get("id")
        if wid:
            self.widget_lines[wid] = self._current_line
        self._current_line += 1

        # recurse into nested lists of dicts
        for subkey, subval in widget.items():
            if isinstance(subval, list) and subval and isinstance(subval[0], dict):
                for child in subval:
                    child.setdefault("parent", wtype)
                    self._render_subtree(child, indent + self.INDENT_STEP)

    def on_intent(self, intent_name: str, widget_info: Dict[str, Any]) -> None:
        w_id = widget_info.get("widget_id") or widget_info.get("id", "<no-id>")
        if intent_name == "input_error":
            errs = widget_info.get("errors", [])
            print(f"⚠️  input_error from '{w_id}': {', '.join(errs)}")
        else:
            print(f"TextRenderer: intent '{intent_name}' from widget '{w_id}'")

    def update(self, dt: float) -> None:
        pass  # no real-time updates for console

    def update_widget(self, widget_info: Dict[str, Any]) -> None:
        w_id = widget_info.get("id")
        if not w_id or w_id not in self.widget_lines:
            print(f"TextRenderer: cannot partial-update widget '{w_id}'")
            return

        builder = TEXT_BUILDERS.get(widget_info.get("type", "unknown"))
        if builder:
            try:
                new_line = builder(widget_info)
            except TypeError:
                new_line = builder(widget_info, self)
        else:
            new_line = "<unknown>"

        old_line = self.widget_lines[w_id]
        print(f"TextRenderer: would replace line {old_line} ➜ {new_line}")
