# audio/base.py
from abc import ABC, abstractmethod
from typing import Dict

class SoundManager(ABC):
    @abstractmethod
    def preload(self, sounds: Dict[str, str]) -> None:
        '''
        Load a mapping of sound-keys → file paths.
        '''
        pass

    @abstractmethod
    def play(self, key: str) -> None:
        '''
        Play the preloaded sound for this key asynchronously.
        '''
        pass

    @abstractmethod
    def stop(self, key: str) -> None:
        '''
        Stop playback of the sound (if supported).
        '''
        pass
