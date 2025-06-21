'''
Kivy-specific SoundManager implementation for the M3 framework.
This manager preloads and queues sounds for asynchronous playback using Kivy's SoundLoader.
'''
from typing import Dict, Any
from threading import Thread, Lock
from collections import deque
from kivy.core.audio import SoundLoader


class KivySoundManager:
    '''
    Asynchronous sound manager using Kivy's SoundLoader.
    '''

    def __init__(self) -> None:
        '''
        Initialize the KivySoundManager and start the background playback thread.
        '''
        self._sounds: Dict[str, Any] = {}       # key -> Sound instance
        self._queue: deque[Any] = deque()       # queued Sound instances
        self._lock = Lock()                     # protect access to queue
        self._thread = Thread(target=self._player_loop, daemon=True)
        self._thread.start()

    def preload(self, sounds: Dict[str, str]) -> None:
        '''
        Preload a mapping of sound keys to file paths.

        :param sounds: Dict where each key is a logical name and value is a file path.
        '''
        for key, path in sounds.items():
            snd = SoundLoader.load(path)
            if snd:
                self._sounds[key] = snd
            else:
                print(f"Warning: could not load sound for key '{key}' at '{path}'")

    def play(self, key: str) -> None:
        '''
        Queue a preloaded sound for playback. Non-blocking.

        :param key: The logical sound name to play.
        '''
        with self._lock:
            snd = self._sounds.get(key)
            if snd:
                self._queue.append(snd)
            else:
                print(f"Warning: sound key '{key}' not preloaded.")

    def stop(self, key: str) -> None:
        '''
        Immediately stop playback of a sound, if it is playing.

        :param key: The logical sound name to stop.
        '''
        with self._lock:
            snd = self._sounds.get(key)
            if snd:
                snd.stop()

    def _player_loop(self) -> None:
        '''
        Background thread loop that plays queued sounds sequentially.
        Waits until the current sound is no longer playing before starting the next.
        '''
        import time
        while True:
            with self._lock:
                if self._queue and getattr(self._queue[0], 'state', None) != 'play':
                    s = self._queue.popleft()
                    s.play()
            time.sleep(0.01)


# Singleton instance for import convenience
test_mgr = KivySoundManager()

if __name__ == "__main__":
    '''
    Basic standalone test:
      - Expects a file at 'assets/test_sound.wav' (WAV or OGG).
      - Preloads and plays it for two seconds, then stops.
    '''
    import time

    mgr = test_mgr
    sounds = {"test": "assets/test_sound.wav"}
    print("Preloading sounds...")
    mgr.preload(sounds)

    print("Playing 'test' for 2 seconds...")
    mgr.play("test")
    time.sleep(2.0)

    print("Stopping 'test' and exiting.")
    mgr.stop("test")
