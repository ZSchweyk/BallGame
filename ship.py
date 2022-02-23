from kivy.properties import StringProperty, NumericProperty
from kivy.uix.widget import Widget

from bullet import Bullet
from ball import Ball


class Ship(Widget):
    image = StringProperty('images/SpaceShip.jpg')
    move_direction = NumericProperty(0)

    def __init__(self, **kwargs):
        super(Ship, self).__init__(**kwargs)

        self.collision_detected = False

    def update(self, dt):
        # Check for collisions
        for e in self.parent._entities:
            if e is not self:
                if isinstance(e, Ball) and e.collide_widget(self):
                    e.collision_detected = True
                    return False

        if self.move_direction != 0:
            self.center_x += self.move_direction * 5

            if self.x <= 0:
                self.x = 0
            elif self.x + self.width >= self.parent.width:
                self.x = self.parent.width - self.width

        # Still alive.
        return True

    def fire(self, num_in_row=1, strength=1, velocity=(0, 5)):
        bullets = []
        if num_in_row == 1:
            bullet = Bullet(strength=strength)
            bullet.center_x = self.center_x
            bullet.center_y = self.y + self.height + 2
            bullet.velocity = velocity
            bullets.append(bullet)
        elif num_in_row == 2:
            bullet1 = Bullet(strength=strength)
            bullet1.center_x = self.center_x - 4
            bullet1.center_y = self.y + self.height + 2
            bullet1.velocity = velocity
            bullets.append(bullet1)

            bullet2 = Bullet(strength=strength)
            bullet2.center_x = self.center_x + 4
            bullet2.center_y = self.y + self.height + 2
            bullet2.velocity = velocity
            bullets.append(bullet2)
        elif num_in_row == 3:
            bullet1 = Bullet(strength=strength)
            bullet1.center_x = self.center_x - 8
            bullet1.center_y = self.y + self.height + 2
            bullet1.velocity = velocity
            bullets.append(bullet1)

            bullet2 = Bullet(strength=strength)
            bullet2.center_x = self.center_x
            bullet2.center_y = self.y + self.height + 2
            bullet2.velocity = velocity
            bullets.append(bullet2)

            bullet3 = Bullet(strength=strength)
            bullet3.center_x = self.center_x + 8
            bullet3.center_y = self.y + self.height + 2
            bullet3.velocity = velocity
            bullets.append(bullet3)

        return bullets
