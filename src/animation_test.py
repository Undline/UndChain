from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
from kivy.clock import Clock
import random

class Ripple:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 0
        self.opacity = 1.0
        self.lifetime = 2.0  # Ripple's total lifetime in seconds
        self.elapsed_time = 0.0  # Time since ripple creation

    def update(self, dt):
        self.elapsed_time += dt
        if self.elapsed_time > self.lifetime:
            return False  # Ripple should be removed

        progress = self.elapsed_time / self.lifetime
        self.radius = 100 * progress  # Adjust expansion speed
        self.opacity = 1.0 - progress  # Fade out over lifetime
        return True

    def draw(self, canvas):
        with canvas:
            Color(1, 1, 1, self.opacity)
            Line(circle=(self.x, self.y, self.radius), width=2)

class RandomRippleWidget(Widget):
    def __init__(self, **kwargs):
        super(RandomRippleWidget, self).__init__(**kwargs)
        self.ripples = []
        Clock.schedule_interval(self.update_ripples, 1 / 60.)
        self.schedule_next_ripple()

    def schedule_next_ripple(self):
        next_interval = random.uniform(0.5, 1.5)
        Clock.schedule_once(self.create_random_ripple, next_interval)

    def create_random_ripple(self, dt):
        x = random.uniform(0, self.width)
        y = random.uniform(0, self.height)
        self.ripples.append(Ripple(x, y))
        self.schedule_next_ripple()

    def update_ripples(self, dt):
        self.canvas.clear()
        # Limit the number of ripples to prevent excessive memory usage
        max_ripples = 50
        if len(self.ripples) > max_ripples:
            self.ripples = self.ripples[-max_ripples:]

        # Update and draw ripples
        for ripple in self.ripples[:]:
            alive = ripple.update(dt)
            if alive:
                ripple.draw(self.canvas)
            else:
                self.ripples.remove(ripple)

class RandomRippleApp(App):
    def build(self):
        return RandomRippleWidget()

if __name__ == '__main__':
    RandomRippleApp().run()
