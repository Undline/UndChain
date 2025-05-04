import sys
import tomllib
from typing import Any, Dict, List, Optional
from argparse import ArgumentParser

from M3_Parser import M3Parser
from renderers.factory import get_renderer


def render_m3(
    m3l_filename: str,
    gss_filename: Optional[str] = None,
    engine_name: str = "text"
) -> None:
    """
    Programmatic API: parse an M3L/GSS pair and render via the specified engine.
    """
    # Initialize parser
    parser = M3Parser(m3l_path=m3l_filename, gss_path=gss_filename)
    # Parse M3L and GSS into a widget tree
    widget_tree = parser.parse()

    # Create and run renderer
    renderer = get_renderer(engine_name)
    renderer.setup()
    renderer.render_widget_tree(widget_tree)
    renderer.teardown()


class M3Renderer:
    """
    Wrapper class for parsing and rendering, with dynamic engine switching.
    """
    def __init__(
        self,
        m3l_filename: str,
        gss_filename: Optional[str] = None,
        engine_name: str = "text"
    ) -> None:
        self.m3l = m3l_filename
        self.gss = gss_filename
        self.engine = engine_name
        self.parser = M3Parser(m3l_path=self.m3l, gss_path=self.gss)
        self.renderer = get_renderer(self.engine)

    def set_renderer_engine(self, engine_name: str) -> None:
        """Switch to a different rendering engine at runtime."""
        self.engine = engine_name
        self.renderer = get_renderer(engine_name)

    def render(self) -> None:
        """Parse M3L/GSS and render the resulting widget tree."""
        # Ensure parsing
        tree = self.parser.parse()
        self.renderer.setup()
        self.renderer.render_widget_tree(tree)
        self.renderer.teardown()


if __name__ == "__main__":
    # CLI entrypoint
    parser = ArgumentParser(description="M3 Renderer CLI")
    parser.add_argument(
        "m3l",
        nargs="?",
        default="example.m3l",
        help="M3L filename under examples/ (defaults to example.m3l)"
    )
    parser.add_argument(
        "--gss",
        help="GSS filename under examples/",
        default=None
    )
    parser.add_argument(
        "--engine",
        help="Renderer engine to use",
        default="text"
    )
    args = parser.parse_args()

    # If invoked directly, use the convenience function
    try:
        render_m3(
            m3l_filename=args.m3l,
            gss_filename=args.gss,
            engine_name=args.engine,
        )
    except Exception as e:
        print(f"Error during rendering: {e}")
        sys.exit(1)
