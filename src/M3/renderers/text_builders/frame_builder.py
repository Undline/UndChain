#  text_builders/frame_builder.py
from typing import Dict, Any, Optional

def build_frame(widget_info: Dict[str, Any],
                renderer: Optional[Any] = None) -> str:     # ← added
    header = f"--- FRAME ({widget_info.get('id', '?')}) ---"
    border = widget_info.get("style", {}).get("border", "noborder")
    return f"{header} (border={border})"
