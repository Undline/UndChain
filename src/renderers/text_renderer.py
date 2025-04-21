# ---------------------------------------------------------------------------
# renderers/text_renderer.py
# ---------------------------------------------------------------------------
from typing import Any, Dict, List

from .base import BaseRenderer

# 🔵  USE THE *CENTRAL* REGISTRY – same place you’ve been adding builders
from .text_builders.registry import TEXT_BUILDERS   # ← one canonical map


class TextRenderer(BaseRenderer):
    """
    Recursive, builder‑driven text renderer.

    Public API (setup / render_widget_tree / teardown) has **not** changed,
    so external callers do not need to be updated.
    """

    INDENT_STEP = 2  # spaces to indent per nesting level

    def __init__(self) -> None:
        super().__init__()
        # line number → widget‑id mapping, used for partial updates
        self.widget_lines: Dict[str, int] = {}
        # running line counter while printing
        self._current_line: int = 0

    # ------------------------------------------------------------------#
    #  Lifecycle hooks (same signatures as before)
    # ------------------------------------------------------------------#
    def setup(self) -> None:
        print("TextRenderer: setup called")

    def teardown(self) -> None:
        print("TextRenderer: teardown called\n")

    # ------------------------------------------------------------------#
    #  Recursive rendering
    # ------------------------------------------------------------------#
    def render_widget_tree(self, widget_tree: List[Dict[str, Any]]) -> None:
        """
        Walk the tree depth‑first, calling a builder for every widget.
        Each builder returns a **single‑line string** that we print with indent.
        """
        print("\n-- TextRenderer: Rendering Widget Tree --\n")

        # reset counters each time we render the full tree
        self.widget_lines.clear()
        self._current_line = 0

        for widget in widget_tree:
            self._render_subtree(widget, indent=0)

        print("\n-- End of Widget Tree --")

    # --------------------------------------------#
    #  Helpers
    # --------------------------------------------#
    def _render_subtree(self, widget: Dict[str, Any], indent: int) -> None:
        """
        Recursively render *one* widget and any children nested under keys
        like 'frame', 'header', 'text_box', etc.
        """
        wtype = widget.get("type", "unknown")
        builder = TEXT_BUILDERS.get(wtype)

        if builder:
            # many of our builders expect (widget_info, renderer)  ➜ pass self
            line_str = builder(widget, renderer=self)
        else:
            line_str = f"{wtype}: ??? (no builder registered)"

        # final composed line with indentation
        padded_line = " " * indent + line_str
        print(padded_line)

        # store for partial updates if widget has an id
        widget_id = widget.get("id")
        if widget_id:
            self.widget_lines[widget_id] = self._current_line
        self._current_line += 1

        # --- Recursively walk known child‑widget lists -----------------
        # Convention: container widgets store children in sub‑lists
        # like widget['checkitem'] (list), widget['text_box'] (list), etc.
        for subkey, subval in widget.items():
            if isinstance(subval, list) and subval and isinstance(subval[0], dict):
                # Heuristic: assume this is a list of child widgets
                for child in subval:
                    # attach original parent info for parent‑scoped styles/debug
                    child.setdefault("parent", wtype)
                    self._render_subtree(child, indent + self.INDENT_STEP)

    # ------------------------------------------------------------------#
    #  Event + partial‑update support  (unchanged)
    # ------------------------------------------------------------------#
    def on_intent(self, intent_name: str, widget_info: Dict[str, Any]) -> None:
        """
        Builders can notify us of input errors, clicks, etc.
        For now we just print the intent so that running the text renderer
        shows *where* validation failed.
        """
        w_id = widget_info.get("widget_id") or widget_info.get("id", "<no‑id>")
        if intent_name == "input_error":
            errs = widget_info.get("errors", [])
            print(f"⚠️  input_error from '{w_id}': {', '.join(errs)}")
        else:
            print(f"TextRenderer: intent '{intent_name}' from widget '{w_id}'")

    def update(self, dt: float) -> None:
        """No real‑time loop for a pure console renderer."""
        pass

    def update_widget(self, widget_info: Dict[str, Any]) -> None:
        """
        Re‑render *one* widget in‑place.  (Useful in tests.)
        """
        w_id = widget_info.get("id")
        if not w_id or w_id not in self.widget_lines:
            print(f"TextRenderer: cannot partial‑update widget '{w_id}'.")
            return

        builder = TEXT_BUILDERS.get(widget_info.get("type", "unknown"))
        new_line = builder(widget_info, renderer=self) if builder else "<unknown>"

        old_line_no = self.widget_lines[w_id]
        print(f"TextRenderer: would replace line {old_line_no} ➜ {new_line}")
