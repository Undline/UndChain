# debug_runtime_builders.py

from M3_Parser import M3Parser
from renderers.text_builders.builder_registry import TEXT_BUILDERS

def run_debug():
    parser = M3Parser(m3l_path="example.m3l")
    widgets = parser.parse()

    print("=== Parsed Widgets ===")
    for w in widgets:
        print(f" • {w.get('id','<no id>')} ({w['type']}) → keys: {list(k for k in w if k not in ('type','id','parent','style'))}")
    print()

    print("=== Builder Outputs ===")
    for w in widgets:
        wtype = w["type"]
        wid   = w.get("id", "<no id>")
        builder = TEXT_BUILDERS.get(wtype)
        if not builder:
            print(f"[NO BUILDER] {wid} ({wtype})")
            continue

        # Some builders take (widget) others (widget, context). We’ll try both.
        try:
            out = builder(w)
        except TypeError:
            out = builder(w, None)

        print(f"[{wtype}] {wid} -> {out}")

if __name__ == "__main__":
    run_debug()
