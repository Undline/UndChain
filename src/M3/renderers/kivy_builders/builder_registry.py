# renderers/kivy_builders/builder_registry.py
from typing import Dict, Callable, Any

# Import each Kivy-specific widget builder here
from .frame_builder import build_frame
# from .checkitem_builder import build_checkitem
# from .h1_builder import build_h1
# from .h2_builder import build_h2
# from .paragraph_builder import build_paragraph
# from .text_box_builder import build_text_box
# from .hyperlink_builder import build_hyperlink
# from .button_builder import build_button

# Central registry mapping widget types to their Kivy builder functions
KIVY_BUILDERS: Dict[str, Callable[..., Any]] = {
    "frame":            build_frame,
    # "checkitem":        build_checkitem,
    # "h1":               build_h1,
    # "h2":               build_h2,
    # "paragraph":        build_paragraph,
    # "text_box":         build_text_box,
    # "hyperlink":        build_hyperlink,
    # "button":           build_button,
    # # Alias for primary/secondary buttons if needed
    # "primary_button":   build_button,
    # "secondary_button": build_button,
}
