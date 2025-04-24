import os
import copy
import pprint
import tomllib
from typing import Any, Dict, List, Optional

from renderers.factory import get_renderer

def load_toml(filepath: str) -> Dict[str, Any]:
    '''Simple loader using Python 3.11+ 'tomllib'.'''
    with open(filepath, "rb") as f:
        return tomllib.load(f)

def deep_merge(a: Dict[str, Any], b: Dict[str, Any]) -> Dict[str, Any]:
    '''Recursively merge dict b into dict a, returning a new dict.'''
    result = copy.deepcopy(a)
    for k, v in b.items():
        if k in result and isinstance(result[k], dict) and isinstance(v, dict):
            result[k] = deep_merge(result[k], v)
        else:
            result[k] = v
    return result

def parse_gss(gss_data: Dict[str, Any]) -> Dict[str, Any]:
    '''
    Convert a GSS dictionary into a nested style structure.
    E.g., [checkitem.checked.true] => gss_styles['checkitem']['checked']['true'] = {...}
    '''
    styles = {}
    for section_name, props in gss_data.items():
        parts = section_name.split(".")  # e.g. ["checkitem","checked","true"]
        current = styles
        for idx, part in enumerate(parts):
            if part not in current:
                current[part] = {}
            if idx == len(parts) - 1:
                # Merge properties into the final sub-dict
                if isinstance(current[part], dict):
                    for k, v in props.items():
                        current[part][k] = v
                else:
                    current[part] = props
            else:
                current = current[part]
    return styles

def parse_m3l(m3l_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    '''
    Convert M3L data (as a dict) into a list of widget dictionaries,
    e.g. [ {type: 'checkitem', 'id': 'todo1', ...}, {type: 'paragraph', ...}, ... ].
    Handles array-of-tables (like [[checkitem]]) and nested ([frame.checkitem]).
    '''
    widget_list = []
    for key, val in m3l_data.items():
        if isinstance(val, dict):
            # single table => e.g. [frame]
            widget = val.copy()
            widget["type"] = key
            widget_list.append(widget)

            # If we see sub-lists like [frame.checkitem], parse those
            for subkey, subval in val.items():
                if isinstance(subval, list) and subkey == "checkitem":
                    # e.g. [[frame.checkitem]]
                    for item_dict in subval:
                        w = item_dict.copy()
                        w["type"] = "checkitem"
                        w["parent"] = key
                        widget_list.append(w)

        elif isinstance(val, list):
            # array-of-tables => e.g. [[checkitem]]
            for item_dict in val:
                if isinstance(item_dict, dict):
                    w = item_dict.copy()
                    w["type"] = key
                    widget_list.append(w)
        else:
            # e.g. "version" or another scalar
            pass
    return widget_list

class M3Parser:
    '''
    Class-based parser for M3L/GSS.
    Optionally, we can hold a renderer engine to show final UI output.
    '''

    def __init__(self,
                 m3l_path: str,
                 gss_path: Optional[str] = None,
                 engine_name: str = "text") -> None:
        '''
        :param m3l_path: Name of the M3L file (within ../Run Rules/).
        :param gss_path: Name of the GSS file (within ../Run Rules/). If None, loads from UndChain.toml or fallback.
        :param engine_name: e.g. 'text', 'kivy'. We'll create the renderer instance from that.
        '''
        
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.run_rules_dir = os.path.join(self.base_dir, "..", "Run Rules")

        self.m3l_path: str = os.path.join(self.run_rules_dir, m3l_path)
        if gss_path is None:
            gss_path = self._load_default_gss_path()
        self.gss_path: str = os.path.join(self.run_rules_dir, gss_path)

        # We'll use the factory to get a renderer
        self.engine_name = engine_name
        self.renderer = get_renderer(self.engine_name)

        # Internal data structures
        self.m3l_data: Dict[str, Any] = {}
        self.gss_data: Dict[str, Any] = {}
        self.widget_tree: List[Dict[str, Any]] = []

        self._load_files()

    def _load_default_gss_path(self) -> str:
        '''
        If user doesn't specify a GSS path, we try reading UndChain.toml's GSSFile
        or fallback to 'example.gss'.
        '''
        config_path = os.path.join(self.run_rules_dir, "UndChain.toml")
        try:
            cfg = load_toml(config_path)
            return cfg.get("GSSFile", "example.gss")
        except:
            return "example.gss"

    def _load_files(self):
        '''
        Actually load M3L and GSS from disk into self.m3l_data / self.gss_data.
        '''
        try:
            self.m3l_data = load_toml(self.m3l_path)
        except FileNotFoundError:
            print(f"M3L file not found: {self.m3l_path}")
            self.m3l_data = {}

        try:
            self.gss_data = load_toml(self.gss_path)
        except FileNotFoundError:
            print(f"GSS file not found: {self.gss_path}")
            self.gss_data = {}

    def parse(self) -> List[Dict[str, Any]]:
        '''
        Parse the M3L + GSS data into a final widget_tree, stored in self.widget_tree.
        Returns the widget_tree as well.
        '''
        self.widget_tree = parse_m3l(self.m3l_data)
        gss_styles = parse_gss(self.gss_data)
        self._merge_styles(self.widget_tree, gss_styles)
        return self.widget_tree

    def _merge_styles(self, widget_tree: List[Dict[str, Any]], gss_styles: Dict[str, Any]) -> None:
        '''
        Merges the GSS style blocks into each widget in the widget_tree.
        '''
        for widget in widget_tree:
            wtype = widget["type"]
            style_dict = {}

            base_block = gss_styles.get(wtype, {})
            style_dict = deep_merge(style_dict, base_block)

            # conditionals
            for field_k, field_v in widget.items():
                if wtype in gss_styles:
                    if isinstance(field_v, bool) and field_k in base_block:
                        sub_map = base_block[field_k]
                        if isinstance(sub_map, dict):
                            str_bool = str(field_v).lower()
                            if str_bool in sub_map:
                                style_dict = deep_merge(style_dict, sub_map[str_bool])
                    elif isinstance(field_v, str) and field_k in base_block:
                        # e.g. [header.level.H2]
                        pass

            # parent scoping
            parent = widget.get("parent")
            if parent:
                p_block = gss_styles.get(parent, {})
                sub_style = p_block.get(wtype, {})
                style_dict = deep_merge(style_dict, sub_style)

            widget["style"] = style_dict

    def set_renderer_engine(self, engine_name: str) -> None:
        '''
        Dynamically switch to another engine. e.g. "kivy", "text", etc.
        '''
        self.engine_name = engine_name
        self.renderer = get_renderer(engine_name)
        print(f"Switched to renderer engine: {engine_name}")

    def render(self) -> None:
        '''
        Renders the widget_tree using the current renderer.
        If we haven't parsed yet, we'll parse first.
        '''
        if not self.widget_tree:
            print("No widget_tree found yet, calling parse() first.")
            self.parse()

        self.renderer.setup()
        self.renderer.render_widget_tree(self.widget_tree)
        self.renderer.teardown()

# ---------------------------------------------------------------------------
# If run directly, do a quick test with multiple engines
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("Running M3_Parser main with external factory for renderer.\n")

    parser = M3Parser(m3l_path="example.m3l", engine_name="text")

    # 1) Parse the M3L
    parser.parse()

    # 2) Render using 'text'
    print("[MAIN] Rendering with the text engine:\n")
    parser.render()

    # 3) Demonstrate switching to 'kivy'
    print("\n[MAIN] Let's pretend we switch to 'kivy' engine. If not implemented, we'll catch it.\n")

    try:
        parser.set_renderer_engine("kivy")
        parser.render()
    except NotImplementedError as e:
        print(f"Caught NotImplementedError: {e}")
    except Exception as e:
        print(f"Caught an unexpected error when switching to 'kivy': {e}")

    print("\nEnd of test.")

