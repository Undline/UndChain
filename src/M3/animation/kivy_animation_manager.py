from typing import Any, Dict, List, Tuple
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle, PushMatrix, PopMatrix, Rotate
from kivy.uix.label import Label
from kivy.graphics import Color, Line
from kivy.graphics import Color, Ellipse
from kivy.utils import get_color_from_hex

from base_animation_manager import BaseAnimationManager


def _schedule_or_start(anim: Animation, widget: Any, delay: float) -> None:
    if delay and delay > 0:
        Clock.schedule_once(lambda dt: anim.start(widget), delay)
    else:
        anim.start(widget)


class KivyAnimationManager(BaseAnimationManager):
    def fade_in(self, widgets: List[Any], duration=0.3, delay=0.0, easing='linear'):
        for w in widgets:
            w.opacity = 0.0
            anim = Animation(opacity=1.0, duration=duration, t=easing)
            _schedule_or_start(anim, w, delay)

    def fade_out(self, widgets: List[Any], duration=0.3, delay=0.0, easing='linear'):
        for w in widgets:
            w.opacity = getattr(w, 'opacity', 1.0)
            anim = Animation(opacity=0.0, duration=duration, t=easing)
            _schedule_or_start(anim, w, delay)

    def slide_left(self, widgets: List[Any], distance=100, duration=0.3, delay=0.0, easing='out_quad'):
        for w in widgets:
            target_x = w.x - distance
            anim = Animation(x=target_x, duration=duration, t=easing)
            _schedule_or_start(anim, w, delay)

    def slide_right(self, widgets: List[Any], distance=100, duration=0.3, delay=0.0, easing='out_quad'):
        for w in widgets:
            target_x = w.x + distance
            anim = Animation(x=target_x, duration=duration, t=easing)
            _schedule_or_start(anim, w, delay)

    def slide_up(self, widgets: List[Any], distance=100, duration=0.3, delay=0.0, easing='out_quad'):
        for w in widgets:
            target_y = w.y + distance
            anim = Animation(y=target_y, duration=duration, t=easing)
            _schedule_or_start(anim, w, delay)

    def slide_down(self, widgets: List[Any], distance=100, duration=0.3, delay=0.0, easing='out_quad'):
        for w in widgets:
            target_y = w.y - distance
            anim = Animation(y=target_y, duration=duration, t=easing)
            _schedule_or_start(anim, w, delay)

    def scale_up(
    self,
    widgets: List[Any],
    scale: float = 1.2,
    duration: float = 0.3,
    delay: float = 0.0,
    easing: str = "in_out_quad"
) -> None:
        """
        Uniformly scale each widget’s size up by the given factor.
        """
        for w in widgets:
            orig_w, orig_h = w.size
            target_size = (orig_w * scale, orig_h * scale)
            anim = Animation(size=target_size, duration=duration, t=easing)
            _schedule_or_start(anim, w, delay)

    def scale_down(
        self,
        widgets: List[Any],
        scale: float = 0.8,
        duration: float = 0.3,
        delay: float = 0.0,
        easing: str = "in_out_quad"
    ) -> None:
        """
        Uniformly scale each widget’s size down by the given factor.
        """
        for w in widgets:
            orig_w, orig_h = w.size
            target_size = (orig_w * scale, orig_h * scale)
            anim = Animation(size=target_size, duration=duration, t=easing)
            _schedule_or_start(anim, w, delay)

    def rotate(
    self,
    widgets: List[Any],
    angle: float = 360.0,
    duration: float = 0.5,
    delay: float = 0.0,
    easing: str = "linear"
) -> None:
        """
        Rotate each widget around its center by the given angle.
        Attaches a Rotate instruction if missing, then animates its 'angle'.
        """
        from kivy.graphics import PushMatrix, Rotate, PopMatrix

        for w in widgets:
            # 1) ensure we have a Rotate instruction stored on the widget
            instr = getattr(w, "_rotation_instr", None)
            if instr is None:
                # wrap draws so rotation applies
                with w.canvas.before:
                    PushMatrix()
                    instr = Rotate(angle=0, origin=w.center)
                    # store it for reuse
                    setattr(w, "_rotation_instr", instr)
                with w.canvas.after:
                    PopMatrix()

            # 2) reset to zero before animating
            instr.angle = 0

            # 3) build and start the animation on the instruction itself
            anim = Animation(angle=angle, duration=duration, t=easing)
            _schedule_or_start(anim, instr, delay)

    def shake(self, widgets: List[Any], distance=10.0, duration=0.3, delay=0.0, easing='in_out_quad'):
        for w in widgets:
            orig_x = w.x
            anim = (Animation(x=orig_x - distance, duration=duration/4, t=easing) +
                    Animation(x=orig_x + distance, duration=duration/2, t=easing) +
                    Animation(x=orig_x, duration=duration/4, t=easing))
            _schedule_or_start(anim, w, delay)

    def bounce(self, widgets: List[Any], distance=20.0, duration=0.5, delay=0.0, easing='out_bounce'):
        for w in widgets:
            orig_y = w.y
            anim = (Animation(y=orig_y + distance, duration=duration/2, t=easing) +
                    Animation(y=orig_y, duration=duration/2, t=easing))
            _schedule_or_start(anim, w, delay)

    def pulse(self, widgets: List[Any], min_scale=0.9, max_scale=1.1, duration=1.0, delay=0.0, easing='in_out_quad'):
        for w in widgets:
            anim = (Animation(scale=max_scale, duration=duration/2, t=easing) +
                    Animation(scale=min_scale, duration=duration/2, t=easing))
            anim.repeat = True
            _schedule_or_start(anim, w, delay)

    def border_glow(
    self,
    widgets: List[Any],
    color: str = "#FFD369",
    duration: float = 0.5,
    delay: float = 0.0,
    easing: str = "in_out_quad"
) -> None:
        """
        Draw a glowing border around each widget, fading in then out.
        """
        rgba = get_color_from_hex(color)
        for w in widgets:
            # clear any old glow
            w.canvas.after.clear()

            # 1) insert a Color + Line into canvas.after
            with w.canvas.after:
                glow_color = Color(rgba[0], rgba[1], rgba[2], 0)
                Line(rectangle=(w.x, w.y, w.width, w.height), width=2)

            # 2) build an animation on the Color.a property
            anim = (
                Animation(a=rgba[3] if len(rgba) > 3 else 1.0, duration=duration/2, t=easing) +
                Animation(a=0.0, duration=duration/2, t=easing)
            )

            # 3) schedule/start it *on the Color instruction*, not the widget
            _schedule_or_start(anim, glow_color, delay)


    def color_transition(self, widgets: List[Any], start_color, end_color, duration=0.5, delay=0.0, easing='linear'):
        sc = get_color_from_hex(start_color)
        ec = get_color_from_hex(end_color)
        for w in widgets:
            if isinstance(w, Label):
                w.color = sc
                anim = Animation(color=tuple(ec), duration=duration, t=easing)
                _schedule_or_start(anim, w, delay)
            else:
                print("color_transition only supports Label by default")

    def flip(self, widgets: List[Any], axis='y', duration=0.5, delay=0.0, easing='linear'):
        # simplistic: rotate 180 then back
        for w in widgets:
            prop = 'rotation_y' if axis=='y' else 'rotation'
            anim = (Animation(**{prop:180}, duration=duration/2, t=easing) +
                    Animation(**{prop:0}, duration=duration/2, t=easing))
            _schedule_or_start(anim, w, delay)

    def ripple(
        self,
        widgets: List[Any],
        radius: float = 100.0,
        duration: float = 0.5,
        color: str = "#FFFFFF",
        delay: float = 0.0
    ) -> None:
        """
        Draw an expanding circle (ripple) from the center of each widget,
        fading out as it grows.
        """
        rgba = get_color_from_hex(color)
        for w in widgets:
            # clear previous
            w.canvas.after.clear()

            # compute center
            cx, cy = w.center
            # initial small circle
            with w.canvas.after:
                ripple_color = Color(rgba[0], rgba[1], rgba[2], 1.0)
                ripple_circle = Ellipse(pos=(cx, cy), size=(0, 0))

            # animate circle size & position
            target_size = (radius * 2, radius * 2)
            target_pos = (cx - radius, cy - radius)
            anim_shape = Animation(
                size=target_size,
                pos=target_pos,
                duration=duration,
                t="out_quad"
            )
            # animate alpha fade
            anim_alpha = Animation(a=0.0, duration=duration, t="linear")

            # schedule both
            _schedule_or_start(anim_shape, ripple_circle, delay)
            _schedule_or_start(anim_alpha, ripple_color, delay)


    def typewriter(
        self,
        widgets: List[Any],
        text: str,
        char_delay: float = 0.05
    ) -> None:
        """
        “Type” the given text into each Label, one character at a time.
        """
        def _type(w: Label, idx: int = 0):
            if idx <= len(text):
                w.text = text[:idx]
                # schedule next character
                Clock.schedule_once(lambda dt: _type(w, idx + 1), char_delay)

        for w in widgets:
            if not isinstance(w, Label):
                continue
            w.text = ""            # start empty
            _type(w, 1)            # begin with first char


    def expand_collapse(self, widgets: List[Any], expand=True, duration=0.5, delay=0.0, easing='in_out_quad'):
        for w in widgets:
            target_h = w.height if expand else 0
            anim = Animation(height=target_h, duration=duration, t=easing)
            _schedule_or_start(anim, w, delay)

    def loading_shimmer(self, widgets: List[Any], duration=1.5, delay=0.0):
        print("loading_shimmer not implemented; requires custom shader or gradient widget")

    def parallax(self, widgets: List[Any], speed=0.5):
        print("parallax not implemented; integrate with scrolling logic")

if __name__ == '__main__':
    from kivy.app import App
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.label import Label
    from kivy.uix.button import Button
    from kivy.clock import Clock

    class TestAnimationApp(App):
        def build(self):
            # simple vertical layout
            root = BoxLayout(orientation='vertical', spacing=20, padding=20)
            self.lbl = Label(text='Hello, M3!', size_hint=(1, None), height=50)
            self.btn = Button(text='Click Me', size_hint=(None, None), size=(150, 50))
            root.add_widget(self.lbl)
            root.add_widget(self.btn)
            return root

        def on_start(self):
            mgr = KivyAnimationManager()

            # 1) fade in the label
            Clock.schedule_once(lambda dt: mgr.fade_in([self.lbl], duration=1.0), 0.5)
            # 2) slide the button to the right
            Clock.schedule_once(lambda dt: mgr.slide_right([self.btn], distance=200, duration=1.0), 2.0)
            # 3) scale up the button
            Clock.schedule_once(lambda dt: mgr.scale_up([self.btn], scale=1.5, duration=1.0), 3.5)
            # 4) rotate the button 180° over 1s
            Clock.schedule_once(lambda dt: mgr.rotate([self.btn], angle=180, duration=1.0), 5.0)
            # 5) shake the label
            Clock.schedule_once(lambda dt: mgr.shake([self.lbl], distance=20, duration=0.5), 6.5)
            # 6) bounce the button
            Clock.schedule_once(lambda dt: mgr.bounce([self.btn], distance=30, duration=0.7), 8.0)
            # 7) border-glow on the button
            Clock.schedule_once(
                lambda dt: mgr.border_glow(
                    [self.btn],
                    color='#FFD369',
                    duration=1.0,
                    delay=0.0,
                    easing='in_out_quad'
                ),
                9.0
            )
            # 8) color-transition on the label (black → red)
            Clock.schedule_once(
                lambda dt: mgr.color_transition(
                    [self.lbl],
                    start_color='#000000',
                    end_color='#FFD369',
                    duration=1.0,
                    delay=0.0,
                    easing='linear'
                ),
                10.5
            )
            # 9) Ripple 
            Clock.schedule_once(lambda dt: mgr.ripple([self.btn], radius=80, duration=1.0, color="#FFD369"), 12.0)
            # 10) Typewritter
            Clock.schedule_once(lambda dt: mgr.typewriter([self.lbl], text="Typed by M3!", char_delay=0.1), 13.5)
            # 11) fade everything out
            Clock.schedule_once(lambda dt: mgr.fade_out([self.lbl, self.btn], duration=1.0), 15.0)
            # 12) exit
            Clock.schedule_once(lambda dt: self.stop(), 16.0)


    TestAnimationApp().run()
