from typing import Dict, Any

def build_frame(widget_info: Dict[str, Any]) -> str:
    fid = widget_info.get("id", "")
    style = widget_info.get("style", {})
    border = style.get("border", "noborder")

    return f"--- FRAME ({fid}) --- (border={border})"
