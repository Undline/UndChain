"""
Standalone Kivy App to test KivyAudioManager with proper Clock scheduling.
Requires Kivy environment.
"""
from typing import Dict, Optional, List
from kivy.core.audio import SoundLoader, Sound
from kivy.clock import Clock
from kivy.app import App
from kivy.uix.widget import Widget


def _clamp(val: float, min_v: float = 0.0, max_v: float = 1.0) -> float:
    """Clamp a float between min_v and max_v."""
    return max(min_v, min(max_v, val))


class KivyAudioManager:
    """
    Audio manager with four channels and global control:
      - music: playlist, sequential or shuffled, loop flag
      - ambient: single looping background
      - vo: voice-over tracks with ducking
      - sfx: transient one-shot effects

    Features:
      - master_volume & mute
      - per-channel volume
      - playlist & shuffle for music
      - VO ducking: instant or animated
    """

    def __init__(self) -> None:
        # Global settings
        self.master_volume: float = 1.0
        self.muted: bool = False
        self._duck_factor: float = 1.0  # for music & ambient when VO playing

        # Music channel
        self._music_paths: List[str] = []
        self._music_index: int = 0
        self._music_sound: Optional[Sound] = None
        self._music_volume: float = 1.0
        self._music_loop_single: bool = False
        self._music_shuffle: bool = False

        # Ambient channel
        self._ambient: Optional[Sound] = None
        self._ambient_volume: float = 1.0

        # VO channel
        self._vo: Optional[Sound] = None
        self._vo_volume: float = 1.0

        # SFX registry
        self._sfx_paths: Dict[str, str] = {}
        self._sfx_volume: float = 1.0

    # ------ Global ------
    def set_master_volume(self, volume: float) -> None:
        self.master_volume = _clamp(volume)
        self._apply_volumes()

    def mute(self) -> None:
        self.muted = True
        self._apply_volumes()

    def unmute(self) -> None:
        self.muted = False
        self._apply_volumes()

    def toggle_mute(self) -> None:
        self.muted = not self.muted
        self._apply_volumes()

    def _apply_volumes(self) -> None:
        base = 0.0 if self.muted else self.master_volume
        if self._music_sound:
            self._music_sound.volume = base * self._music_volume * self._duck_factor
        if self._ambient:
            self._ambient.volume = base * self._ambient_volume * self._duck_factor
        if self._vo:
            self._vo.volume = base * self._vo_volume

    # ------ Music / Playlist ------
    def preload_playlist(self, paths: List[str], shuffle: bool = False, loop_single: bool = False) -> None:
        from random import shuffle as _shuffle
        self._music_paths = paths.copy()
        self._music_index = 0
        self._music_shuffle = shuffle
        self._music_loop_single = loop_single and len(paths) == 1
        if self._music_shuffle:
            _shuffle(self._music_paths)
        self._load_current_music()

    def _load_current_music(self) -> None:
        if not self._music_paths:
            self._music_sound = None
            return
        path = self._music_paths[self._music_index]
        snd = SoundLoader.load(path)
        if snd:
            snd.loop = self._music_loop_single
            self._music_sound = snd
            self._apply_volumes()
            snd.bind(on_stop=lambda *args: self._on_music_end())  # type: ignore
        else:
            print(f"Warning: failed to load music '{path}'")

    def _on_music_end(self) -> None:
        if not self._music_sound:
            return
        if self._music_loop_single:
            self._music_sound.play()
            return
        self._music_index = (self._music_index + 1) % len(self._music_paths)
        self._load_current_music()
        if self._music_sound:
            self._music_sound.play()

    def play_music(self, volume: float = 1.0) -> None:
        if not self._music_sound:
            print("Error: no music preloaded.")
            return
        self._music_volume = _clamp(volume)
        self._apply_volumes()
        self._music_sound.play()

    def stop_music(self) -> None:
        if self._music_sound:
            self._music_sound.stop()

    # ------ Ambient ------
    def preload_ambient(self, path: str) -> None:
        snd = SoundLoader.load(path)
        if snd:
            snd.loop = True
            self._ambient = snd
            self._apply_volumes()
        else:
            print(f"Warning: failed to load ambient '{path}'")

    def play_ambient(self, volume: float = 1.0) -> None:
        if not self._ambient:
            print("Error: no ambient preloaded.")
            return
        self._ambient_volume = _clamp(volume)
        self._apply_volumes()
        self._ambient.play()

    def stop_ambient(self) -> None:
        if self._ambient:
            self._ambient.stop()

    # ------ VO (Voice-over) ------
    def preload_vo(self, path: str) -> None:
        snd = SoundLoader.load(path)
        if snd:
            self._vo = snd
            self._apply_volumes()
        else:
            print(f"Warning: failed to load VO '{path}'")

    def play_vo(self, volume: float = 1.0, duck: float = 0.3) -> None:
        if not self._vo:
            print("Error: no VO preloaded.")
            return
        self._vo_volume = _clamp(volume)
        # instant duck
        self._duck_factor = duck
        self._apply_volumes()
        # bind restore
        try:
            self._vo.unbind(on_stop=self._restore_duck)
        except Exception:
            pass
        self._vo.bind(on_stop=lambda *args: self._restore_duck())  # type: ignore
        # schedule restore by length
        length = getattr(self._vo, 'length', 0) or 0
        if length > 0:
            Clock.schedule_once(lambda dt: self._restore_duck(), length)
        self._vo.play()

    def stop_vo(self) -> None:
        if self._vo:
            self._vo.stop()

    def _restore_duck(self) -> None:
        self._duck_factor = 1.0
        self._apply_volumes()

    # ------ SFX -----
    def preload_sfx(self, sfx_map: Dict[str, str]) -> None:
        self._sfx_paths.update(sfx_map)

    def play_sfx(self, key: str, volume: Optional[float] = None) -> None:
        path = self._sfx_paths.get(key)
        if not path:
            print(f"Error: sfx '{key}' not registered.")
            return
        snd = SoundLoader.load(path)
        if not snd:
            print(f"Warning: cannot load sfx '{key}' from '{path}'")
            return
        vol = _clamp(volume) if volume is not None else self._sfx_volume
        snd.volume = 0.0 if self.muted else self.master_volume * vol
        snd.play()

    def set_sfx_volume(self, volume: float) -> None:
        self._sfx_volume = _clamp(volume)


# Singleton instance for application use
audio_mgr = KivyAudioManager()


class AudioTestApp(App):
    def build(self):
        # invisible root widget
        return Widget()

    def on_start(self):
        # Preload assets
        audio_mgr.preload_playlist(['assets/test_music.mp3'], shuffle=False, loop_single=True)
        audio_mgr.preload_ambient('assets/test_ambient.wav')
        audio_mgr.preload_vo('assets/test_vo.mp3')
        audio_mgr.preload_sfx({'click': 'assets/test_sfx.wav'})

        # Schedule test sequence
        Clock.schedule_once(lambda dt: self._play_music_and_ambient(), 0)
        Clock.schedule_once(lambda dt: audio_mgr.play_vo(volume=1.0, duck=0.1), 3)
        Clock.schedule_once(lambda dt: audio_mgr.play_sfx('click'), 8)
        Clock.schedule_once(lambda dt: audio_mgr.play_sfx('click'), 8.5)
        Clock.schedule_once(lambda dt: audio_mgr.play_sfx('click'), 9)
        Clock.schedule_once(lambda dt: audio_mgr.set_master_volume(0.4), 10)
        Clock.schedule_once(lambda dt: audio_mgr.mute(), 11)
        Clock.schedule_once(lambda dt: audio_mgr.unmute(), 13)
        # Clock.schedule_once(lambda dt: self._stop_all(), 15)

    def _play_music_and_ambient(self):
        print("[Test] Play music + ambient @50%")
        audio_mgr.play_music(volume=0.5)
        audio_mgr.play_ambient(volume=0.5)

    def _stop_all(self):
        print("[Test] Stopping all channels and exiting")
        audio_mgr.stop_vo()
        audio_mgr.stop_ambient()
        audio_mgr.stop_music()
        self.stop()


if __name__ == '__main__':
    AudioTestApp().run()
