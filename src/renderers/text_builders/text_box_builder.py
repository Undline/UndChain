from typing import Dict, Any

def build_text_box(widget_info: Dict[str, Any]) -> str:
    label = widget_info.get("label", "")
    placeholder = widget_info.get("placeholder", "")
    is_password = widget_info.get("is_password", False)
    style = widget_info.get("style", {})

    mask_text = style.get("mask_text", False) or is_password  # if style says `mask_text=true` or if is_password is True
    font_size = style.get("font-size", "nofontsize")
    border = style.get("border", "noborder")

    # We'll just do a textual representation:
    if mask_text:
        return f"TextBox({label}): [Password Field] (font_size={font_size}, border={border})"
    else:
        return f"TextBox({label}): placeholder='{placeholder}' (font_size={font_size}, border={border})"
