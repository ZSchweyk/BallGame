from kivy.properties import StringProperty, NumericProperty
from kivy.uix.widget import Widget

from bullet import Bullet


class Ship(Widget):
    image = StringProperty('images/SpaceShip.jpg')
    move_direction = NumericProperty(0)

    def __init__(self, **kwargs):
        super(Ship, self).__init__(**kwargs)

        self.collision_detected = False

    def update(self, dt):
        # Check for collisions
        # for e in self.parent._entities:
        #     if e is not self and e.collide_widget(self):
        #         e.collision_detected = True
        #         return False

        if self.move_direction != 0:
            self.center_x += self.move_direction * 5

            if self.x <= 0:
                self.x = 0
            elif self.x + self.width >= self.parent.width:
                self.x = self.parent.width - self.width

        # Still alive.
        return True

    def fire(self, velocity=(0, 5)):
        bullet = Bullet()

        bullet.center_x = self.center_x
        bullet.center_y = self.y + self.height + 2
        bullet.velocity = velocity

        return bullet
