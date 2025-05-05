# registry.py
from typing import Dict, Any, Callable

# import each new widget builder here
from .checkitem_builder import build_checkitem
from .paragraph_builder import build_paragraph
from .frame_builder import build_frame
from .text_box_builder import build_text_box
from .hyperlink_builder import build_hyperlink
from .button_builder import build_button
from .h1_builder import build_h1
from .h2_builder import build_h2

TEXT_BUILDERS: Dict[str, Callable[..., str]] = {
    "checkitem":        build_checkitem,
    "paragraph":        build_paragraph,
    "frame":            build_frame,
    "text_box":         build_text_box,
    "hyperlink":        build_hyperlink,
    "button":           build_button,
    "primary_button":   build_button, #need to implement a separate builder for this
    "secondary_button": build_button,
    "h1":               build_h1,
    "h2":               build_h2,
}
