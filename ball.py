from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector

from bullet import Bullet


class Ball(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    acceleration_x = NumericProperty(0)
    acceleration_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    acceleration = ReferenceListProperty(acceleration_x, acceleration_y)

    def __init__(self, strength=50, **kwargs):
        super(Ball, self).__init__(**kwargs)
        self.collision_detected = False
        self.strength = strength

    def update(self, dt):
        for e in self.parent._entities:
            if e is not self and e.collide_widget(self):
                if isinstance(e, Bullet):
                    e.collision_detected = True
                    self.strength -= 1
                    if self.strength <= 0:
                        self.collision_detected = True
                        # The return statement below is not technically needed; it just prevents the computation below.
                        return False

        self.velocity[0] += self.acceleration[0]
        self.velocity[1] += self.acceleration[1]
        self.pos = Vector(*self.velocity) + self.pos

        if self.center_y - self.height / 2 < self.parent.y + 5:
            self.velocity[1] *= -1

        if self.center_x - self.width / 2 <= self.parent.x or self.center_x + self.width / 2 >= self.parent.width:
            self.velocity[0] *= -1

        return True
