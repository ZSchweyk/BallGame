from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector


class Bullet(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def __init__(self, **kwargs):
        super(Bullet, self).__init__(**kwargs)

        self.collision_detected = False

    def update(self, dt):
        self.pos = Vector(*self.velocity) + self.pos

        # Check if we've gone off-screen
        if self.center_y > self.parent.height:
            return False

        # Still alive.
        return True
