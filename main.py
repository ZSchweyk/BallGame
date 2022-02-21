from kivy.app import App
from kivy.clock import Clock
from kivy.app import Builder

from main_game import MainGame

class BallGame(App):
    def build(self):
        game = MainGame()

        Clock.schedule_interval(game.update, 1 / 1000)

        return game


Builder.load_file("main.kv")
if __name__ == '__main__':
    BallGame().run()
