from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.layout import Layout
from typing import Any, Dict


def _parse_size(value: Any) -> float:
    """
    Convert a style value like '1rem' or '10px' into a float pixel value.
    Defaults: 1rem = 16px.
    """
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        v = value.strip()
        try:
            if v.endswith('px'):
                return float(v[:-2])
            if v.endswith('rem'):
                return float(v[:-3]) * 16.0
            # plain number
            return float(v)
        except ValueError:
            return 0.0
    return 0.0


def build_frame(widget: Dict[str, Any], renderer: Any = None) -> Layout:
    """
    Kivy builder for 'frame' widgets. Supports 'stack' (vertical BoxLayout) and 'grid'.

    :param widget: dict containing parsed widget info, including:
                   - 'layout': 'stack' or 'grid'
                   - 'columns': int (for grid)
                   - 'style': dict with 'gap', 'padding', etc.
    :param renderer: the KivyRenderer instance (optional)
    """
    # Default layout type
    layout_type = widget.get('layout', 'stack')
    style = widget.get('style', {}) or {}

    # Spacing between children
    gap = _parse_size(style.get('gap', 0))
    # Uniform padding on all sides
    pad_val = _parse_size(style.get('padding', 0))
    padding = [pad_val, pad_val, pad_val, pad_val]

    if layout_type == 'grid':
        # Grid layout with specified number of columns
        cols = int(widget.get('columns', 1))
        container: Layout = GridLayout(
            cols=cols,
            spacing=gap,
            padding=padding
        )
    else:
        # Vertical stack layout
        container = BoxLayout(
            orientation='vertical',
            spacing=gap,
            padding=padding
        )

    return container


if __name__ == "__main__":
    # Basic test: instantiate default stack
    print("Testing build_frame in standalone mode...")
    default_def = {'layout': 'stack', 'style': {'gap': '1rem', 'padding': '0.5rem'}}
    default_container = build_frame(default_def)
    print(f"Default layout container type: {type(default_container)}")

    # Test grid layout
    grid_def = {'layout': 'grid', 'columns': 3, 'style': {'gap': '10px', 'padding': '5px'}}
    grid_container = build_frame(grid_def)
    print(f"Grid layout container type: {type(grid_container)}")

    # visually inspect in a Kivy window
    from kivy.base import runTouchApp
    runTouchApp(grid_container)
