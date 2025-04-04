from typing import Dict, Any

def build_h1(widget_info: Dict[str, Any]) -> str:
    """
    Returns a text-based representation of an H1 heading.
    If you wanted a generic approach, you might read widget_info.get("level") 
    for H1, H2, etc. But let's keep it direct for H1.
    """
    content = widget_info.get("content", "Untitled Heading")
    style = widget_info.get("style", {})
    # Maybe show a style field like 'font-size' or 'color'
    color = style.get("color", "nocolor")

    return f"# [H1] {content} (color={color})"
