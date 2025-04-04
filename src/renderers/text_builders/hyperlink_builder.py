from typing import Dict, Any

def build_hyperlink(widget_info: Dict[str, Any]) -> str:
    text = widget_info.get("text", "untitled link")
    url  = widget_info.get("url", "")
    style = widget_info.get("style", {})
    color = style.get("color", "nocolor")
    underline = style.get("underline", "false")

    return f"Hyperlink: '{text}' => {url} (color={color}, underline={underline})"
