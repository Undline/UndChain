from pathlib import Path
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
      parser = M3Parser(m3l_path="example.m3l")
      widget_tree = parser.parse()
    """

    def __init__(self,
                 m3l_path: str,
                 gss_path: Optional[str] = None) -> None:
        """
        Initialize parser with mandatory M3L and auto-load default GSS from UndChain.toml if not provided.
        """
        self.logger = logger

        # Base folder for examples
        base_dir = Path(__file__).resolve().parent
        self.examples_dir = base_dir / "examples"

        # Paths to M3L and GSS files under examples/
        self.m3l_path: str = str(self.examples_dir / m3l_path)
        self.logger.info(f"M3L path explicitly set to: {self.m3l_path}")

        if gss_path is None:
            gss_path = self._load_default_gss_path()

        self.gss_path: str = str(self.examples_dir / gss_path)
        self.logger.info(f"GSS path explicitly set to: {self.gss_path}")

        # Actually load the TOML data into memory:
        self.m3l_data: Dict[str, Any] = self.load_toml(self.m3l_path)
        self.gss_data: Dict[str, Any] = self.load_toml(self.gss_path)

        self.logger.info(f"Loaded M3L from {m3l_path} and GSS from {gss_path}")

    def _load_default_gss_path(self) -> str:
        """
        Loads default GSS path from UndChain.toml located in examples/.
        If 'GSSFile' is not found, fallback 'example.gss'.
        """
        config_path = self.examples_dir / "UndChain.toml"
        try:
            config = self.load_toml(str(config_path))
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
        widget_tree = self._parse_m3l(self.m3l_data)
        gss_styles = self._parse_gss(self.gss_data)
        merged_tree = self._merge_styles(widget_tree, gss_styles)
        return merged_tree

    def _parse_gss(self, gss_data: Dict[str, Any]) -> Dict[str, Any]:
        styles: Dict[str, Any] = {}
        for section_name, props in gss_data.items():
            parts = section_name.split('.')
            current = styles
            for idx, part in enumerate(parts):
                current = current.setdefault(part, {})
                if idx == len(parts) - 1:
                    if isinstance(props, dict):
                        current.update(props)
        return styles

    def _parse_m3l(self, m3l_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Extract widgets from M3L data, flattening all [[frame.xxx]] arrays into
        standalone widget dicts, and explicitly emitting the 'frame' as its own widget.
        """
        widgets: List[Dict[str, Any]] = []

        # 1) Top-level [frame] container
        frame_data = m3l_data.get("frame", {})
        if not isinstance(frame_data, dict):
            return widgets

        # Build the root frame widget
        root = frame_data.copy()
        root["type"] = "frame"
        widgets.append(root)

        # 2) Flatten each array-of-tables under frame.*
        for sect in ("header", "text_box", "checkbox", "secondary_button", "primary_button"):  # order matters if sequencing
            items = root.pop(sect, [])
            if not isinstance(items, list):
                continue
            for item in items:
                w = item.copy()

                # Normalize sect -> widget type
                if sect == "header":
                    lvl = w.get("level", "").lower()
                    wtype = lvl if lvl in ("h1", "h2") else "header"
                elif sect == "checkbox":
                    wtype = "checkitem"
                elif sect in ("primary_button", "secondary_button"):
                    wtype = "button"
                else:
                    wtype = sect  # e.g. 'text_box'

                w["type"] = wtype
                w["parent"] = "frame"
                widgets.append(w)

        return widgets

    def _deep_merge(self, a: Dict[str, Any], b: Dict[str, Any]) -> Dict[str, Any]:
        result = copy.deepcopy(a)
        for k, v in b.items():
            if k in result and isinstance(result[k], dict) and isinstance(v, dict):
                result[k] = self._deep_merge(result[k], v)
            else:
                result[k] = v
        return result

    def _merge_styles(self, widget_tree: List[Dict[str, Any]], gss_styles: Dict[str, Any]) -> List[Dict[str, Any]]:
        for widget in widget_tree:
            wtype = widget.get('type', '')
            style_dict: Dict[str, Any] = {}

            # Base style block
            base_block = gss_styles.get(wtype, {})
            style_dict = self._deep_merge(style_dict, base_block)

            # Conditionals
            for field_k, field_v in widget.items():
                if field_k in base_block:
                    if isinstance(field_v, bool):
                        sub_map = base_block[field_k]
                        if isinstance(sub_map, dict):
                            str_bool = str(field_v).lower()
                            if str_bool in sub_map:
                                style_dict = self._deep_merge(style_dict, sub_map[str_bool])

            # Parent scoping
            parent_type = widget.get('parent')
            if parent_type:
                parent_block = gss_styles.get(parent_type, {})
                sub_style = parent_block.get(wtype, {})
                style_dict = self._deep_merge(style_dict, sub_style)

            widget['style'] = style_dict

        return widget_tree

if __name__ == '__main__':
    parser = M3Parser(m3l_path='example.m3l')
    widget_tree = parser.parse()
    pp = pprint.PrettyPrinter(indent=2, width=120)
    pp.pprint(widget_tree)
