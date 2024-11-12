import random
import math
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line, Ellipse, Point
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.vector import Vector

# Select the animation you want to run by setting this variable:
# Options: 'ripples', 'fireflies', 'snowfall', 'fire'
ANIMATION = 'fireflies'  # Change this to switch animations

# --- Ripple Animation Classes ---
class Ripple:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 0
        self.lifetime = 2.0  # seconds
        self.elapsed_time = 0.0  # Time since ripple creation

    def update(self, dt):
        self.elapsed_time += dt
        if self.elapsed_time > self.lifetime:
            return False  # Ripple should be removed
        progress = self.elapsed_time / self.lifetime
        self.radius = 100 * progress  # Adjust expansion speed
        return True

    def draw(self, canvas):
        opacity = 1.0 - (self.elapsed_time / self.lifetime)
        with canvas:
            Color(1, 1, 1, opacity)
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
        max_ripples = 50
        if len(self.ripples) > max_ripples:
            self.ripples = self.ripples[-max_ripples:]
        for ripple in self.ripples[:]:
            alive = ripple.update(dt)
            if alive:
                ripple.draw(self.canvas)
            else:
                self.ripples.remove(ripple)

# --- Firefly Animation Classes ---
class Firefly:
    def __init__(self):
        self.x = random.uniform(0, Window.width)
        self.y = random.uniform(0, Window.height)
        self.velocity = Vector(random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5))
        self.blink_time = random.uniform(0.5, 2.0)
        self.elapsed_time = 0.0
        self.visible = True

    def update(self, dt):
        self.elapsed_time += dt
        if self.elapsed_time > self.blink_time:
            self.visible = not self.visible
            self.elapsed_time = 0.0
            self.blink_time = random.uniform(0.5, 2.0)
        self.x += self.velocity.x
        self.y += self.velocity.y
        self.x = self.x % Window.width
        self.y = self.y % Window.height

    def draw(self, canvas):
        if self.visible:
            with canvas:
                Color(1, 1, 0.5)
                Ellipse(pos=(self.x - 2, self.y - 2), size=(4, 4))

class FireflyWidget(Widget):
    def __init__(self, **kwargs):
        super(FireflyWidget, self).__init__(**kwargs)
        self.fireflies = [Firefly() for _ in range(50)]
        Clock.schedule_interval(self.update_fireflies, 1 / 60.)

    def update_fireflies(self, dt):
        self.canvas.clear()
        for firefly in self.fireflies:
            firefly.update(dt)
            firefly.draw(self.canvas)

# --- Snowfall Animation Classes ---
class Snowflake:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.size = random.uniform(2, 5)
        self.velocity_y = random.uniform(-2, -1)
        self.wind = random.uniform(-0.5, 0.5)
        self.width = width
        self.height = height

    def update(self, dt):
        self.y += self.velocity_y
        self.x += self.wind
        if self.y < 0:
            self.y = self.height
            self.x = random.uniform(0, self.width)
        return True

    def draw(self, canvas):
        with canvas:
            Color(1, 1, 1)
            Ellipse(pos=(self.x, self.y), size=(self.size, self.size))

class SnowfallWidget(Widget):
    def __init__(self, **kwargs):
        super(SnowfallWidget, self).__init__(**kwargs)
        self.snowflakes = [Snowflake(random.uniform(0, self.width), random.uniform(0, self.height), self.width, self.height) for _ in range(100)]
        Clock.schedule_interval(self.update_snowflakes, 1 / 60.)

    def update_snowflakes(self, dt):
        self.canvas.clear()
        for snowflake in self.snowflakes:
            snowflake.update(dt)
            snowflake.draw(self.canvas)

# --- Fire Animation Classes ---
class FireParticle:
    def __init__(self, x, y):
        self.x = x + random.uniform(-5, 5)
        self.y = y
        self.size = random.uniform(5, 10)
        self.velocity_y = random.uniform(1, 3)
        self.lifetime = 1.0
        self.elapsed_time = 0.0
        self.color = [1.0, random.uniform(0.5, 1.0), 0.0]  # Orange to yellow

    def update(self, dt):
        self.elapsed_time += dt
        if self.elapsed_time > self.lifetime:
            return False
        self.y += self.velocity_y
        self.size *= 0.95
        self.color[1] -= 0.01  # Gradually change color from yellow to red
        return True

    def draw(self, canvas):
        alpha = 1.0 - (self.elapsed_time / self.lifetime)
        with canvas:
            Color(self.color[0], max(self.color[1], 0), self.color[2], alpha)
            Ellipse(pos=(self.x - self.size / 2, self.y - self.size / 2), size=(self.size, self.size))

class FireWidget(Widget):
    def __init__(self, **kwargs):
        super(FireWidget, self).__init__(**kwargs)
        self.particles = []
        Clock.schedule_interval(self.update_particles, 1 / 60.)
        Clock.schedule_interval(self.emit_particles, 0.02)

    def emit_particles(self, dt):
        x = self.width / 2
        y = self.height / 4
        for _ in range(5):  # Emit multiple particles at once
            self.particles.append(FireParticle(x, y))

    def update_particles(self, dt):
        self.canvas.clear()
        for particle in self.particles[:]:
            alive = particle.update(dt)
            if alive:
                particle.draw(self.canvas)
            else:
                self.particles.remove(particle)

# --- Main Application ---
class AnimationApp(App):
    def build(self):
        if ANIMATION == 'ripples':
            return RandomRippleWidget()
        elif ANIMATION == 'fireflies':
            return FireflyWidget()
        elif ANIMATION == 'snowfall':
            return SnowfallWidget()
        elif ANIMATION == 'fire':
            return FireWidget()
        else:
            # Default to ripples if unknown animation is selected
            return RandomRippleWidget()

if __name__ == '__main__':
    AnimationApp().run()
