from typing import Dict, Any

def build_checkitem(widget_info: Dict[str, Any]) -> str:
    checked = widget_info.get("checked", False)
    label = widget_info.get("label", "")
    style = widget_info.get("style", {})
    color = style.get("color", "nocolor")

    mark = "[X]" if checked else "[ ]"
    return f"{mark} {label} (color={color})"
