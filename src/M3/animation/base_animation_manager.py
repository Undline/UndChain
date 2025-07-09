"""
Abstract base class for all AnimationManagers. Defines the required API for core animation types:
  - fade-in / fade-out
  - slide-left / slide-right / slide-up / slide-down
  - scale-up / scale-down
  - rotate
  - shake
  - bounce
  - pulse
  - border_glow
  - color_transition
  - flip
  - ripple
  - typewriter
  - expand_collapse
  - loading_shimmer
  - parallax
"""
from abc import ABC, abstractmethod
from typing import Any, Dict, List


class BaseAnimationManager(ABC):
    """
    Defines the mandatory animation API for all UI engines.
    """
    @abstractmethod
    def fade_in(self,
                widgets: List[Any],
                duration: float = 0.3,
                delay: float = 0.0,
                easing: str = "linear") -> None:
        pass

    @abstractmethod
    def fade_out(self,
                 widgets: List[Any],
                 duration: float = 0.3,
                 delay: float = 0.0,
                 easing: str = "linear") -> None:
        pass

    @abstractmethod
    def slide_left(self,
                   widgets: List[Any],
                   distance: float = 100,
                   duration: float = 0.3,
                   delay: float = 0.0,
                   easing: str = "out_quad") -> None:
        pass

    @abstractmethod
    def slide_right(self,
                    widgets: List[Any],
                    distance: float = 100,
                    duration: float = 0.3,
                    delay: float = 0.0,
                    easing: str = "out_quad") -> None:
        pass

    @abstractmethod
    def slide_up(self,
                 widgets: List[Any],
                 distance: float = 100,
                 duration: float = 0.3,
                 delay: float = 0.0,
                 easing: str = "out_quad") -> None:
        pass

    @abstractmethod
    def slide_down(self,
                   widgets: List[Any],
                   distance: float = 100,
                   duration: float = 0.3,
                   delay: float = 0.0,
                   easing: str = "out_quad") -> None:
        pass

    @abstractmethod
    def scale_up(self,
                 widgets: List[Any],
                 scale: float = 1.2,
                 duration: float = 0.3,
                 delay: float = 0.0,
                 easing: str = "in_out_quad") -> None:
        pass

    @abstractmethod
    def scale_down(self,
                   widgets: List[Any],
                   scale: float = 0.8,
                   duration: float = 0.3,
                   delay: float = 0.0,
                   easing: str = "in_out_quad") -> None:
        pass

    @abstractmethod
    def rotate(self,
               widgets: List[Any],
               angle: float = 360.0,
               duration: float = 0.5,
               delay: float = 0.0,
               easing: str = "linear") -> None:
        pass

    @abstractmethod
    def shake(self,
              widgets: List[Any],
              distance: float = 10.0,
              duration: float = 0.3,
              delay: float = 0.0,
              easing: str = "in_out_quad") -> None:
        pass

    @abstractmethod
    def bounce(self,
               widgets: List[Any],
               distance: float = 20.0,
               duration: float = 0.5,
               delay: float = 0.0,
               easing: str = "out_bounce") -> None:
        pass

    @abstractmethod
    def pulse(self,
              widgets: List[Any],
              min_scale: float = 0.9,
              max_scale: float = 1.1,
              duration: float = 1.0,
              delay: float = 0.0,
              easing: str = "in_out_quad") -> None:
        pass

    @abstractmethod
    def border_glow(self,
                    widgets: List[Any],
                    color: str = "#FFD369",
                    duration: float = 0.5,
                    delay: float = 0.0,
                    easing: str = "in_out_quad") -> None:
        pass

    @abstractmethod
    def color_transition(self,
                         widgets: List[Any],
                         start_color: str,
                         end_color: str,
                         duration: float = 0.5,
                         delay: float = 0.0,
                         easing: str = "linear") -> None:
        pass

    @abstractmethod
    def flip(self,
             widgets: List[Any],
             axis: str = "y",
             duration: float = 0.5,
             delay: float = 0.0,
             easing: str = "linear") -> None:
        pass

    @abstractmethod
    def ripple(self,
               widgets: List[Any],
               radius: float = 100.0,
               duration: float = 0.5,
               color: str = "#FFFFFF",
               delay: float = 0.0) -> None:
        pass

    @abstractmethod
    def typewriter(self,
                   widgets: List[Any],
                   text: str,
                   char_delay: float = 0.05) -> None:
        pass

    @abstractmethod
    def expand_collapse(self,
                        widgets: List[Any],
                        expand: bool,
                        duration: float = 0.5,
                        delay: float = 0.0,
                        easing: str = "in_out_quad") -> None:
        pass

    @abstractmethod
    def loading_shimmer(self,
                        widgets: List[Any],
                        duration: float = 1.5,
                        delay: float = 0.0) -> None:
        pass

    @abstractmethod
    def parallax(self,
                 widgets: List[Any],
                 speed: float = 0.5) -> None:
        pass
