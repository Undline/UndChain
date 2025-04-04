from typing import Dict, Any

def build_h2(widget_info: Dict[str, Any]) -> str:
    """
    Returns a text-based representation of an H2 heading.
    """

    content = widget_info.get("content", "Untitled Heading")
    style = widget_info.get("style", {})
    # Maybe show a style field like 'font-size' or 'color'
    color = style.get("color", "nocolor")

    return f"# [H2] {content} (color={color})"
