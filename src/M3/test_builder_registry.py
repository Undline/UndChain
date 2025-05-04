# debug_builders.py

from renderers.text_builders.builder_registry import TEXT_BUILDERS

def invoke_builder(wtype: str, builder_fn):
    # minimal dummy widget
    widget = {
        "type": wtype,
        "id": f"test_{wtype}",
        # most text‐builders only look at widget["id"] or widget["style"], so this should suffice
        "style": {}
    }
    try:
        # try calling with just widget
        return builder_fn(widget)
    except TypeError:
        try:
            # or widget + None for context
            return builder_fn(widget, None)
        except Exception as e:
            return f"<Error: {e}>"

if __name__ == "__main__":
    print("=== Registered TEXT_BUILDERS keys ===")
    for wtype in sorted(TEXT_BUILDERS):
        print(f" - {wtype}")
    print()

    print("=== Builder invocation results ===")
    for wtype, fn in TEXT_BUILDERS.items():
        result = invoke_builder(wtype, fn)
        print(f"{wtype:15s} -> {result}")
