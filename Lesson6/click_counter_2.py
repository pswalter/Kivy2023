import kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, StringProperty

# Each class present in .kv file must be declared in Python file
# Despite we don't use Label in this file, we mention one in the .kv file
from kivy.uix.label import Label
from kivy.uix.button import Button


# This is the same class as in the previous example
class CountingButton(Button):
    
    count = NumericProperty()
 
    def do_action(self):
        self.count += 1



class CountingBox(BoxLayout):
    
    title = StringProperty()


# As in previous example, this is the only correct main widget class name
#  to handle Kivy file clickcounter2.py
class Clickcounter2App(App):

    def build(self):
        return CountingBox(title='The Ultimate Triple-Counter...')


if __name__ == '__main__':
    Clickcounter2App().run()
