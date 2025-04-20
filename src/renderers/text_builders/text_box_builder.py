from typing import Any, Dict, List
import string

def build_text_box(widget_info: Dict[str, Any], renderer=None) -> str:
    """
    Text‑only representation of an <input> field with inline validation.
    Emits renderer.on_intent('input_error', …) for each failing rule.
    """

    label        = widget_info.get("label", "")
    placeholder  = widget_info.get("placeholder", "")
    is_password  = widget_info.get("is_password", False)
    style        = widget_info.get("style", {})

    # this would come from a real UI’s data‑binding; here we just consume whatever the test harness supplies
    user_value: str = widget_info.get("user_value", "")

    # --- validation rules ----------------------------------------------------
    validate: Dict[str, Any] = widget_info.get("validate", {})
    errors_cfg: Dict[str, str] = validate.get("errors", {})

    min_len          = validate.get("min_length")
    max_len          = validate.get("max_length")
    forbidden_chars  = validate.get("forbidden_chars", "")
    require_digit    = validate.get("require_digit", False)
    require_special  = validate.get("require_special", False)

    errors_found: List[str] = []

    def add_error(rule_key: str, default_msg: str) -> None:
        msg = errors_cfg.get(rule_key, default_msg)
        errors_found.append(msg)
        if renderer:
            renderer.on_intent("input_error", {
                "widget_id": widget_info.get("id"),
                "failed_rule": rule_key,
                "message": msg
            })

    # -------------------------------------------------------------------------
    if user_value:  # only run rules once the user started typing
        if min_len is not None and len(user_value) < min_len:
            add_error("min_length", f"Must be ≥ {min_len} chars.")

        if max_len is not None and len(user_value) > max_len:
            add_error("max_length", f"Must be ≤ {max_len} chars.")

        if forbidden_chars and any(ch in forbidden_chars for ch in user_value):
            add_error("forbidden_chars", "Contains forbidden character(s).")

        if require_digit and not any(ch.isdigit() for ch in user_value):
            add_error("require_digit", "Must include at least one number (0‑9).")

        if require_special and not any(ch in string.punctuation for ch in user_value):
            add_error("require_special", "Must include at least one special character.")

    # --- build textual representation ---------------------------------------
    if is_password:
        field_display = "[••••••••]" if user_value else "[Password Field]"
    else:
        field_display = f"'{user_value}'" if user_value else f"(placeholder: “{placeholder}”)"

    if errors_found:
        return f"TextBox({label}): INVALID → {', '.join(errors_found)}"
    else:
        if user_value:
            return f"TextBox({label}): {field_display}"
        else:
            # No input yet: show the rule summary so testers can see what will be enforced
            rules = []
            if min_len is not None:
                rules.append(f"min ≥ {min_len}")
            if max_len is not None:
                rules.append(f"max ≤ {max_len}")
            if require_digit:
                rules.append("digit")
            if require_special:
                rules.append("special")
            if forbidden_chars:
                rules.append("no " + "".join(forbidden_chars))
            rule_summary = " | ".join(rules) if rules else "no rules"
            return f"TextBox({label}): {field_display}  — rules: {rule_summary}"
