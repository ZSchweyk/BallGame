import sys

from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.core.window import Window
from ship import Ship


class MainGame(Widget):
    player_ship = ObjectProperty(None)

    def __init__(self):
        super(MainGame, self).__init__()
        self._entities = []

        self._add_entity(self.player_ship, skip_widget=True)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down, on_key_up=self._on_key_up)

    def update(self, dt):
        for e in self._entities[:]:
            status = e.update(dt)
            if not status or e.collision_detected:
                self._remove_entity(e)

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
            bullet = self.player_ship.fire()
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
