from typing import Dict, Any

def build_paragraph(widget_info: Dict[str, Any]) -> str:
    content = widget_info.get("content", "")
    style = widget_info.get("style", {})
    font_size = style.get("font-size", "nofontsize")

    return f"Paragraph: {content} (font_size={font_size})"
