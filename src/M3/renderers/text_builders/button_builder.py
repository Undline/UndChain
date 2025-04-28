from typing import Dict, Any

def build_button(widget_info: Dict[str, Any]) -> str:
    label = widget_info.get("label", "Button")
    style = widget_info.get("style", {})

    bg  = style.get("background-color", "nobg")
    bold = style.get("font-weight", "normal")

    return f"Button: [{label}] (background={bg}, bold={bold})"
