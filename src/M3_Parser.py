import tomllib
from typing import Any, Dict, List, Optional
import os

from logging import Logger
from logger_util import setup_logger

logger: Logger = setup_logger('M3_Parser', 'M3_Parser.log')

# Define absolute paths explicitly
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
RUN_RULES_DIR = os.path.join(PROJECT_ROOT, "Run Rules")

class M3Parser:
    '''
    M3 Parser explicitly loads and merges M3L widget definitions
    with GSS styling into a clear widget tree.
    '''

    def __init__(self, 
                 m3l_path: str, 
                 gss_path: Optional[str] = None) -> None:
        '''
        Initialize parser with mandatory M3L and auto-load default GSS from UndChain.toml.
        '''

        # Explicitly resolve paths
        self.m3l_path: str = os.path.join(RUN_RULES_DIR, m3l_path)
        logger.info(f"M3L path explicitly set to: {self.m3l_path}")

        if gss_path is None:
            gss_path = self._load_default_gss_path()

        self.gss_path: str = os.path.join(RUN_RULES_DIR, gss_path)
        logger.info(f"GSS path explicitly set to: {self.gss_path}")

        self.gss_data: Dict[str, Any] = self.load_toml(self.gss_path)

    def _load_default_gss_path(self) -> str:
        '''
        Loads default GSS path from UndChain.toml explicitly located in ../Run Rules/.
        '''
        config_path = os.path.join(RUN_RULES_DIR, "UndChain.toml")
        try:
            config = self.load_toml(config_path)
            default_gss = config.get("GSSFile", "example.gss")
            logger.info(f"Default GSS file loaded from UndChain.toml: {default_gss}")
            return default_gss
        except FileNotFoundError:
            logger.warning("UndChain.toml not found; fallback 'example.gss'")
            return "example.gss"
        except Exception as e:
            logger.error(f"Error loading UndChain.toml: {e}; fallback 'example.gss'")
            return "example.gss"

    def switch_gss(self, new_gss_path: str) -> None:
        '''
        Allows switching the current GSS file at runtime.
        '''
        self.gss_path = os.path.join(RUN_RULES_DIR, new_gss_path)
        self.gss_data = self.load_toml(self.gss_path)
        logger.info(f"GSS switched explicitly to: {self.gss_path}")

    def load_toml(self, file_path: str) -> Dict[str, Any]:
        '''
        Explicitly loads a TOML file; falls back gracefully if GSS is missing.
        '''
        try:
            with open(file_path, "rb") as f:
                data = tomllib.load(f)
                logger.debug(f"TOML file '{file_path}' loaded successfully.")
                return data
        except FileNotFoundError:
            logger.error(f"TOML file not found: {file_path}")
            if file_path == self.gss_path:
                logger.warning("GSS file missing; activating backup emergency style.")
                return self._backup_gss_style()
            return {}
        except tomllib.TOMLDecodeError as e:
            logger.error(f"TOML decode error in {file_path}: {e}")
            return {}

    def _backup_gss_style(self) -> Dict[str, Any]:
        '''
        Minimal backup GSS used only when external GSS file is missing.
        Loaded explicitly to conserve memory in normal operation.
        '''
        logger.info("Explicitly loading minimal backup GSS styling.")
        return {
            "default": {
                "font-family": "sans-serif",
                "font-size": "1rem",
                "color": "#000",
                "padding": "0.5rem"
            }
        }

    def parse(self) -> List[Dict[str, Any]]:
        '''
        Parses and combines M3L and GSS into a widget tree.
        '''

        m3l_data: Dict[str, Any] = self.load_toml(self.m3l_path)
        widget_tree = []

        if not m3l_data:
            logger.warning("No M3L data found; widget tree will be empty.")

        for widget_type, widget_props_list in m3l_data.items():
            if not isinstance(widget_props_list, list):
                widget_props_list = [widget_props_list]

            for widget_props in widget_props_list:
                widget = {
                    "type": widget_type,
                    **widget_props,
                    "style": self.resolve_styles(widget_type, widget_props) or {},
                    "animation": self.resolve_animations(widget_type, widget_props) or {}
                }
                widget_tree.append(widget)
                logger.debug(f"Widget '{widget_type}' parsed with ID '{widget_props.get('id', 'N/A')}'")

        logger.info(f"Parsing completed: {len(widget_tree)} widgets loaded.")
        return widget_tree


    def resolve_styles(
        self, 
        widget_type: str, 
        widget_props: Dict[str, Any],
        parent_widget: Optional[str] = None
    ) -> Dict[str, Any]:
        '''
        Resolves widget styles from GSS, supports parent-child conditions.
        '''

        styles = self.gss_data.get(widget_type, self.gss_data.get("default", {})).copy()

        conditional_styles: List[str] = [
            key for key in self.gss_data 
            if key.startswith(f"{widget_type}.")
        ]

        for cond_style in conditional_styles:
            condition: str = cond_style.split(".")[-1]
            prop, expected = condition.split('.', 1) if '.' in condition else (condition, "true")
            
            if str(widget_props.get(prop, "false")).lower() == expected.lower():
                styles.update(self.gss_data[cond_style])

        if parent_widget:
            parent_key: str = f"{widget_type}.inside-{parent_widget}"
            if parent_key in self.gss_data:
                styles.update(self.gss_data[parent_key])

        return styles

    def resolve_animations(self, widget_type: str, widget_props: Dict[str, Any]) -> Dict[str, Any]:
        animations = {}
        widget_styles = self.gss_data.get(widget_type, {})

        # Example usage if you wanted to check widget_props
        # e.g., if 'hover_animation' is turned off in widget_props, skip it
        # if not widget_props.get("hover_animation_disabled", False):
        #     # then set animations["hover"] = ...

        animation_keys: List[str] = [
            key for key in widget_styles if key.startswith("animation.")
        ]

        for anim_key in animation_keys:
            anim_name = anim_key.split(".", 1)[1]
            animations[anim_name] = widget_styles[anim_key]

        return animations


# Explicit Example Usage for Testing:
if __name__ == "__main__":
    import pprint

    def display_pretty(data):
        pp = pprint.PrettyPrinter(indent=2)
        pp.pprint(data)

    parser = M3Parser(m3l_path="example.m3l")  # explicit M3L path required
    widget_tree: List[Dict[str, Any]] = parser.parse()

    logger.info(f"Final widget tree:\n{display_pretty(widget_tree)}")
