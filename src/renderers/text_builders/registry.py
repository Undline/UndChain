# registry.py
from typing import Dict, Any, Callable

# import each new widget builder here
from .checkitem_builder import build_checkitem
from .paragraph_builder import build_paragraph
from .frame_builder import build_frame
from .text_box_builder import build_text_box
from .hyperlink_builder import build_hyperlink
from .button_builder import build_button

TEXT_BUILDERS: Dict[str, Callable[[Dict[str, Any]], str]] = {
    "checkitem": build_checkitem,
    "paragraph": build_paragraph,
    "frame":     build_frame,
    "text_box":  build_text_box,   
    "hyperlink": build_hyperlink,  
    "button":    build_button,  
}
