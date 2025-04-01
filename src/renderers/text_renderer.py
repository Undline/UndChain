from typing import Any, Dict, List
from .base import BaseRenderer

class TextRenderer(BaseRenderer):
    '''
    A simple text-based renderer demonstrating how to
    inherit from BaseRenderer and implement its methods.
    '''

    def __init__(self) -> None:
        '''
        If you need a local data structure for tracking lines or partial updates,
        you can define them here.
        '''

        super().__init__()
        self.widget_lines = {}  # e.g. store line numbers or text references if partial updates needed

    def setup(self) -> None:
        '''
        Called once before rendering. 
        For text-based, we might just clear the screen or do nothing special.
        '''

        print("TextRenderer: setup called")

    def render_widget_tree(self, widget_tree: List[Dict[str, Any]]) -> None:
        '''
        Print out each widget in a basic text form.
        For a large UI, you might also store references for partial updates later.
        '''

        print("\n-- TextRenderer: Rendering Widget Tree --\n")
        line_num = 0
        for widget in widget_tree:
            line_str = self._render_single_widget(widget)
            print(line_str)
            # Store reference for partial updates, if desired
            widget_id = widget.get("id")
            if widget_id:
                self.widget_lines[widget_id] = line_num
            line_num += 1
        print("\n-- End of Widget Tree --")

    def teardown(self) -> None:
        '''
        Called at shutdown to release resources.
        For text-based, no real resources, so we might just print a message.
        '''

        print("TextRenderer: teardown called\n")

    def update(self, dt: float) -> None:
        '''
        (Optional) For a real-time loop, we might re-check user input or re-print dynamic content.
        For text-based, you might do nothing or show a spinner, etc.
        '''

        print(f"TextRenderer: Update called with dt={dt}")
        pass

    def on_intent(self, intent_name: str, widget_info: Dict[str, Any]) -> None:
        '''
        Called when a widget triggers an event. 
        We'll just print out the event or do minimal logic.
        '''

        w_id = widget_info.get("id", "<no-id>")
        print(f"TextRenderer: on_intent '{intent_name}' triggered by widget '{w_id}'")

    def update_widget(self, widget_info: Dict[str, Any]) -> None:
        '''
        Called when a single widget's data changes. 
        For text-based approach, we can re-print just that line if we track line numbers in self.widget_lines.
        '''

        w_id = widget_info.get("id")
        if w_id not in self.widget_lines:
            # We didn't originally have a line for it, so maybe do nothing
            print(f"TextRenderer: No line reference for widget {w_id}; can't partial update.")
            return

        line_num = self.widget_lines[w_id]
        # In a real console approach, you'd have to move the cursor or re-print the entire output.
        # For a simple approach, we just note that we would re-print that line:
        new_str = self._render_single_widget(widget_info)
        print(f"TextRenderer: Updating line {line_num} to: {new_str}")

    # --- Utility method for printing a single widget
    def _render_single_widget(self, widget: Dict[str, Any]) -> str:
        '''
        Returns a string representation of a single widget.
        '''

        wtype = widget.get("type", "unknown")
        label = widget.get("label", "")
        checked = widget.get("checked", False)
        content = widget.get("content", "")

        if wtype == "checkitem":
            mark = "[X]" if checked else "[ ]"
            return f"{mark} {label}"

        elif wtype == "paragraph":
            return f"Paragraph: {content}"

        elif wtype == "frame":
            fid = widget.get("id", "")
            return f"--- FRAME ({fid}) ---"

        else:
            # fallback
            return f"{wtype}: {label or content}"
