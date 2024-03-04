from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty

from random import choice


# The screens are almost the same - and normally we would use inheritance here.
# I write them separately to show they can be completely different, as long as they
#   both inherit from Screen
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
        sm = ScreenManager()
        # Note that each screen MUST have a name.
        # If you want to switch screens you can use sm.current = 'screen_name', but
        #   in this simple example, Kivy code handles this.
        sm.add_widget(FirstPlayerScreen(name='First'))
        sm.add_widget(SecondPlayerScreen(name='Second'))
        return sm

if __name__ == '__main__':
    MultiscreenApp().run()

