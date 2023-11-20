import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class Application(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")
        
        firstLabel = Label(text="First Label")
        layout.add_widget(firstLabel)

        secondLabel = Label(text="Second Label")
        layout.add_widget(secondLabel)

        clickButton = Button(text="Click me!")
        layout.add_widget(clickButton)

        return layout
    
if __name__ == "__main__":
    myApp = Application()
    myApp.run()