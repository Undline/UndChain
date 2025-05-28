from .text_renderer import TextRenderer
from .kivy_renderer import KivyRenderer

def get_renderer(engine_name: str):
    if engine_name == "text":
        return TextRenderer()
    elif engine_name == "kivy":
        return KivyRenderer()
        raise NotImplementedError("KivyRenderer not yet implemented.")
    else:
        raise ValueError(f"Unknown engine '{engine_name}'")
