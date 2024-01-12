import kivy

from kivy.uix.button import Button
from kivy.app import App
from kivy.properties import NumericProperty


class CountingButton(Button):
    
    # You declare a property as a class variable like this:
    # Kivy will then adjust the constructor of MainButton to include setting an instance attribute count.
    # Each instance of MainButton will have its own <count>, despite it was Kivy, not you, placing it in the constructor. 
    count = NumericProperty()

    def do_action(self):
        self.count += 1



# IMPORTANT NAMING ISSUE
# Your main class MUST be named exactly like your .kv file with App added at the end
# For example, if your .kv file is clickcounter.kv, your main widget class must be named clickcounterApp
# (capitalization does not matter)
class ClickcounterApp(App):

    def build(self):
        return CountingButton(count=0)


if __name__ == '__main__':
    ClickcounterApp().run()
