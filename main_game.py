import random
import sys

from kivy.graphics import Color
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from datetime import datetime

from ship import Ship
from ball import Ball

BULLET_STRENGTH = 1
NUM_SECONDS_BETWEEN_BALL_ENTRIES = 3
MAX_NUM_BALLS_ALLOWED_ON_SCREEN = 5


class MainGame(Widget):
    player_ship = ObjectProperty(None)

    def __init__(self):
        super(MainGame, self).__init__()
        self._entities = []

        self._add_entity(self.player_ship, skip_widget=True)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down, on_key_up=self._on_key_up)
        self.time = datetime.now()

    def update(self, dt):
        for e in self._entities[:]:
            status = e.update(dt)
            if not status or e.collision_detected:
                if isinstance(e, Ship):
                    # popup = MDDialog(text="Game Over")
                    # popup.open()
                    sys.exit(0)
                if isinstance(e, Ball):
                    self.add_ball(strength=int(e.strength / 2))
                    self.add_ball(strength=int(e.strength / 2))
                self._remove_entity(e)

        if datetime.now().timestamp() - self.time.timestamp() >= NUM_SECONDS_BETWEEN_BALL_ENTRIES:
            if sum([1 if isinstance(entity, Ball) else 0 for entity in
                    self._entities]) < MAX_NUM_BALLS_ALLOWED_ON_SCREEN:
                ball = self.add_ball()
                self._add_entity(ball)
                self.time = datetime.now()
        else:
            pass

    def add_ball(self, strength=random.randint(10, 100), velocity=(1, -3), acceleration=(0, -.125)):
        ball = Ball(strength=strength)
        size = random.uniform(30, 70)
        ball.size = size, size
        # specify the color of the ball. Not completely sure how to do this yet...
        if random.random() <= .5:
            ball.center_x = self.width * random.uniform(.05, .15)
        else:
            ball.center_x = self.width * random.uniform(.9, .95)

        ball.center_y = self.height * .9
        ball.velocity = velocity
        ball.acceleration = acceleration
        return ball

    def _add_entity(self, entity, skip_widget=False):
        self._entities.append(entity)
        if not skip_widget:
            self.add_widget(entity)

    def _remove_entity(self, entity):
        self.remove_widget(entity)
        self._entities.remove(entity)

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        # Logger.debug(keycode)

        if keycode[1] == 'escape':
            sys.exit(0)

        elif keycode[1] == 'spacebar':
            bullets = self.player_ship.fire(num_in_row=3, strength=BULLET_STRENGTH)
            for bullet in bullets:
                self._add_entity(bullet)

        elif keycode[1] in ('left', 'right'):
            if keycode[1] == 'left':
                self.player_ship.move_direction = -1
            elif keycode[1] == 'right':
                self.player_ship.move_direction = 1

        return True

    def _on_key_up(self, keyboard, keycode):
        if keycode[1] in ('left', 'right'):
            self.player_ship.move_direction = 0

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard = None

    def on_touch_move(self, touch):
        if touch.x + self.player_ship.width / 2 > self.width or touch.x - self.player_ship.width / 2 < self.x:
            return
        self.player_ship.center_x = touch.x

