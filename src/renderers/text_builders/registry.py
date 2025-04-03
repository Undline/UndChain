# registry.py
from typing import Dict, Any, Callable

from .checkitem_builder import build_checkitem
from .paragraph_builder import build_paragraph
from .frame_builder import build_frame
# import each new widget builder

TEXT_BUILDERS: Dict[str, Callable[[Dict[str, Any]], str]] = {
    "checkitem": build_checkitem,
    "paragraph": build_paragraph,
    "frame":     build_frame,
    # add each new widget type here
}
