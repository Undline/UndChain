"""
Abstract base class for AudioManager implementations,
defining the required multi-channel audio API.
"""
from abc import ABC, abstractmethod
from typing import Dict, List, Optional


class BaseAudioManager(ABC):
    """
    Defines the interface for all audio managers in M3:
      - music (playlist, shuffle, loop)
      - ambient (loop)
      - vo (voice-over with ducking)
      - sfx (one-shot effects)
      - master volume & mute
    """

    @abstractmethod
    def set_master_volume(self, volume: float) -> None:
        pass

    @abstractmethod
    def mute(self) -> None:
        pass

    @abstractmethod
    def unmute(self) -> None:
        pass

    # Music / playlist
    @abstractmethod
    def preload_playlist(self, paths: List[str], shuffle: bool = False, loop_single: bool = False) -> None:
        pass

    @abstractmethod
    def play_music(self, volume: float = 1.0) -> None:
        pass

    @abstractmethod
    def stop_music(self) -> None:
        pass

    @abstractmethod
    def set_music_volume(self, volume: float) -> None:
        pass

    # Ambient
    @abstractmethod
    def preload_ambient(self, path: str) -> None:
        pass

    @abstractmethod
    def play_ambient(self, volume: float = 1.0) -> None:
        pass

    @abstractmethod
    def stop_ambient(self) -> None:
        pass

    @abstractmethod
    def set_ambient_volume(self, volume: float) -> None:
        pass

    # Voice-over
    @abstractmethod
    def preload_vo(self, path: str) -> None:
        pass

    @abstractmethod
    def play_vo(self, volume: float = 1.0, duck: float = 0.3) -> None:
        pass

    @abstractmethod
    def stop_vo(self) -> None:
        pass

    # SFX
    @abstractmethod
    def preload_sfx(self, sfx_map: Dict[str, str]) -> None:
        pass

    @abstractmethod
    def play_sfx(self, key: str, volume: Optional[float] = None) -> None:
        pass

    @abstractmethod
    def set_sfx_volume(self, volume: float) -> None:
        pass
