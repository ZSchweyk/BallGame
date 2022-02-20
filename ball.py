from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector


class Ball(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    acceleration_x = NumericProperty(0)
    acceleration_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    acceleration = ReferenceListProperty(acceleration_x, acceleration_y)

    def __init__(self, **kwargs):
        super(Ball, self).__init__(**kwargs)
        self.collision_detected = False

    def update(self, dt):
        self.velocity[0] += self.acceleration[0]
        self.velocity[1] += self.acceleration[1]
        self.pos = Vector(*self.velocity) + self.pos

        print(self.parent.y)

        if self.y - self.height < 0:
            self.velocity[1] *= -1

        if self.center_x - self.width / 2 <= self.parent.x or self.center_x + self.width / 2 >= self.parent.width:
            self.velocity[0] *= -1

        return True
