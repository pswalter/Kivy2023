from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty, StringProperty

from random import choice


# Declare both screens
class FirstPlayerScreen(Screen):
    results = StringProperty()

    def append_character(self):
        self.results = self.results + choice('012')

class SecondPlayerScreen(Screen):
    results = StringProperty()

    def append_character(self):
        self.results = self.results + choice('abc')

class MultiscreenApp(App):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(FirstPlayerScreen(name='First'))
        sm.add_widget(SecondPlayerScreen(name='Second'))

        return sm

if __name__ == '__main__':
    MultiscreenApp().run()

