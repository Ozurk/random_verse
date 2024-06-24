from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter


class RandomDev(Widget):
    pass


class TopLabel(Widget):
    pass


class StartButton(Widget):
    pass


class RandomDevApp(App):
    def build(self):
        main_gui = RandomDev()
        return main_gui


if __name__ == '__main__':
    app = RandomDevApp()
    app.run()
