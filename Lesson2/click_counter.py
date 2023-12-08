import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# We keep the counter value in a global variable to ensure all components
# of the application can access and modify it. 
# In future lessons we will discuss better ways to achieve this. 
value = 0

class Application(App):

    def update_label(self):
        self.value_label.text = str(value)

    def handle_subtract(self, instance):
        global value
        # If we had not declared value to be global above, the next line
        # would instead create a local variable *value* and set it to one less
        # than the global value - the global wouldn't change.
        value = value - 1
        self.update_label()
    
    def handle_add(self, instance):
        # What happens when you comment out the line below? Try and check.
        global value
        value = value + 1
        self.update_label()

    def build(self):
        layout = BoxLayout()
        self.subtract_button = Button(text="-", font_size=48, on_press=self.handle_subtract)
        self.add_button = Button(text="+", font_size=48, on_press=self.handle_add)
        self.value_label = Label(text="0", font_size=48)

        layout.add_widget(self.subtract_button)
        layout.add_widget(self.value_label)
        layout.add_widget(self.add_button)
        
        return layout


if __name__ == "__main__":
    myApp = Application()
    myApp.run()