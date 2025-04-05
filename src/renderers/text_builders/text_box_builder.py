from typing import Dict, Any, List

def build_text_box(widget_info: Dict[str, Any], renderer=None) -> str:
    label       = widget_info.get("label", "")
    placeholder = widget_info.get("placeholder", "")
    is_password = widget_info.get("is_password", False)
    style       = widget_info.get("style", {})

    # If the user typed something (in a real UI, you'd store partial input somewhere)
    user_value  = widget_info.get("user_value", "")

    validate  = widget_info.get("validate", {})
    errors    = validate.get("errors", {})

    # read the actual validation rules
    min_len   = validate.get("min_length", None)
    max_len   = validate.get("max_length", None)
    forbidden = validate.get("forbidden_chars", "")

    # We'll track any errors found
    errors_found: List[str] = []

    # 1) Check min_length
    if min_len is not None and len(user_value) < min_len:
        msg = errors.get("min_length", "Input is too short.")
        errors_found.append(msg)

    # 2) Check max_length
    if max_len is not None and len(user_value) > max_len:
        msg = errors.get("max_length", "Input is too long.")
        errors_found.append(msg)

    # 3) Check forbidden_chars
    if forbidden:
        for c in user_value:
            if c in forbidden:
                msg = errors.get("forbidden_chars", "Contains forbidden punctuation.")
                errors_found.append(msg)
                break

    # handle password display
    if is_password:
        text_representation = "[Password Field]"
    else:
        text_representation = f"user_value='{user_value}'"

    # If any errors found, we can call an intent or just show them
    if errors_found:
        if renderer:
            renderer.on_intent("input_error", {
                "widget_id": widget_info.get("id"),
                "errors": errors_found
            })
        combined_errors = "; ".join(errors_found)
        return f"TextBox({label}): INVALID -> {combined_errors}"
    else:
        return f"TextBox({label}): {text_representation} (placeholder='{placeholder}')"
