import os
import copy
import pprint
import tomllib
from typing import Any, Dict, List, Optional
from logging import Logger
from logger_util import setup_logger

logger: Logger = setup_logger('M3_Parser', 'M3_Parser.log')

class M3Parser:
    """
    A class-based parser for M3L and GSS.

    Usage:
      parser = M3Parser(m3l_path=\"some_file.m3l\")
      widget_tree = parser.parse()
    """

    def __init__(self,
                 m3l_path: str,
                 gss_path: Optional[str] = None) -> None:
        """
        Initialize parser with mandatory M3L and auto-load default GSS from UndChain.toml if not provided.
        """
        self.logger = logger

        # Resolve absolute paths:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.run_rules_dir = os.path.join(base_dir, "..", "Run Rules")

        self.m3l_path: str = os.path.join(self.run_rules_dir, m3l_path)
        self.logger.info(f"M3L path explicitly set to: {self.m3l_path}")

        if gss_path is None:
            gss_path = self._load_default_gss_path()

        self.gss_path: str = os.path.join(self.run_rules_dir, gss_path)
        self.logger.info(f"GSS path explicitly set to: {self.gss_path}")

        # Actually load the TOML data into memory:
        self.m3l_data: Dict[str, Any] = self.load_toml(self.m3l_path)
        self.gss_data: Dict[str, Any] = self.load_toml(self.gss_path)

        self.logger.info(f"Loaded M3L from {m3l_path} and GSS from {gss_path}")

    def _load_default_gss_path(self) -> str:
        """
        Loads default GSS path from UndChain.toml located in ../Run Rules/.
        If 'GSSFile' is not found, fallback 'example.gss'.
        """
        config_path = os.path.join(self.run_rules_dir, "UndChain.toml")
        try:
            config = self.load_toml(config_path)
            default_gss = config.get("GSSFile", "example.gss")
            self.logger.info(f"Default GSS file loaded from UndChain.toml: {default_gss}")
            return default_gss
        except FileNotFoundError:
            self.logger.warning("UndChain.toml not found; fallback 'example.gss'")
            return "example.gss"
        except Exception as e:
            self.logger.error(f"Error loading UndChain.toml: {e}; fallback 'example.gss'")
            return "example.gss"

    def load_toml(self, file_path: str) -> Dict[str, Any]:
        """
        Explicitly loads a TOML file using Python 3.11+ 'tomllib'.
        """
        try:
            with open(file_path, "rb") as f:
                data = tomllib.load(f)
                self.logger.debug(f"TOML file '{file_path}' loaded successfully.")
                return data
        except FileNotFoundError:
            self.logger.error(f"TOML file not found: {file_path}")
            return {}
        except tomllib.TOMLDecodeError as e:
            self.logger.error(f"TOML decode error in {file_path}: {e}")
            return {}

    def parse(self) -> List[Dict[str, Any]]:
        """
        Parses and combines M3L and GSS into a final widget tree.
        Returns the list of widget dictionaries with merged 'style'.
        """
        # 1) parse M3L => widget structures
        widget_tree = self._parse_m3l(self.m3l_data)

        # 2) parse GSS => nested style rules
        gss_styles = self._parse_gss(self.gss_data)

        # 3) merge styles
        merged_tree = self._merge_styles(widget_tree, gss_styles)

        return merged_tree

    def _parse_gss(self, gss_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Convert GSS data into nested dictionary. e.g.:
          [checkitem.checked.true] => gss_styles['checkitem']['checked']['true'] = {...}
          [frame.checkitem] => gss_styles['frame']['checkitem'] = {...}
        """
        styles = {}
        for section_name, props in gss_data.items():
            parts = section_name.split(".")
            current = styles
            for idx, part in enumerate(parts):
                if part not in current:
                    current[part] = {}
                if idx == len(parts) - 1:
                    # Merge props
                    if isinstance(current[part], dict):
                        for k, v in props.items():
                            current[part][k] = v
                    else:
                        current[part] = props
                else:
                    current = current[part]
        return styles

    def _parse_m3l(self, m3l_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Extract widgets from M3L data. E.g.:
          [frame] -> single widget
          [[frame.checkitem]] -> multiple checkitem widgets with parent='frame'
          [[checkitem]] -> multiple root-level checkitems
        """
        widget_list = []

        for key, val in m3l_data.items():
            if isinstance(val, dict):
                # single table, e.g. [frame]
                widget = val.copy()
                widget["type"] = key
                widget_list.append(widget)

                # if that dict might contain array-of-tables like [frame.checkitem]
                for subkey, subval in val.items():
                    if isinstance(subval, list) and subkey == "checkitem":
                        # means we have [[frame.checkitem]]
                        for item_dict in subval:
                            w = item_dict.copy()
                            w["type"] = "checkitem"
                            w["parent"] = key
                            widget_list.append(w)

            elif isinstance(val, list):
                # array of tables => each item is a dict, e.g. [[checkitem]]
                for item_dict in val:
                    if isinstance(item_dict, dict):
                        w = item_dict.copy()
                        w["type"] = key
                        widget_list.append(w)
            else:
                # Possibly a top-level scalar like 'version'; ignoring here or handle separately
                self.logger.debug(f"Ignoring top-level scalar: {key}={val}")

        return widget_list

    def _deep_merge(self, a: Dict[str, Any], b: Dict[str, Any]) -> Dict[str, Any]:
        """Recursively merge dict b into dict a, returning a new dict."""
        result = copy.deepcopy(a)
        for k, v in b.items():
            if k in result and isinstance(result[k], dict) and isinstance(v, dict):
                result[k] = self._deep_merge(result[k], v)
            else:
                result[k] = v
        return result

    def _merge_styles(self, widget_tree: List[Dict[str, Any]], gss_styles: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        For each widget, build a final 'style' dict by merging:
          - Base style block for its type (e.g. gss_styles['checkitem'])
          - Conditionals (e.g. if 'checked' = true => gss_styles['checkitem']['checked']['true'])
          - Parent scoping if 'parent' is present (e.g. gss_styles['frame']['checkitem'])
        """
        for widget in widget_tree:
            wtype = widget["type"]
            style_dict = {}

            # Base style e.g. [checkitem]
            base_block = gss_styles.get(wtype, {})
            style_dict = self._deep_merge(style_dict, base_block)

            # Conditionals
            for field_k, field_v in widget.items():
                if wtype in gss_styles:
                    if isinstance(field_v, bool) and field_k in base_block:
                        # e.g. 'checked': True => base_block['checked']['true']
                        sub_map = base_block[field_k]
                        if isinstance(sub_map, dict):
                            str_bool = str(field_v).lower()  # 'true' or 'false'
                            if str_bool in sub_map:
                                style_dict = self._deep_merge(style_dict, sub_map[str_bool])
                    elif isinstance(field_v, str) and field_k in base_block:
                        # For other possible attributes (like level=H2 for header)
                        pass

            # Parent scoping
            parent_type = widget.get("parent")
            if parent_type:
                parent_block = gss_styles.get(parent_type, {})
                sub_style = parent_block.get(wtype, {})
                style_dict = self._deep_merge(style_dict, sub_style)

            widget["style"] = style_dict

        return widget_tree

if __name__ == "__main__":
    # Example usage:
    parser = M3Parser(m3l_path="example.m3l")  # no gss_path => auto-load from UndChain.toml or fallback
    widget_tree = parser.parse()

    pp = pprint.PrettyPrinter(indent=2, width=120)
    pp.pprint(widget_tree)
