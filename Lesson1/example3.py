import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Application(App):
    def build(self):
        layout = GridLayout(cols=2)

        # First Row
        firstNumberLabel = Label(text="First Number")
        layout.add_widget(firstNumberLabel)
        self.firstNumberInput = TextInput(multiline=False)
        layout.add_widget(self.firstNumberInput)

        # Second Row
        secondNumberLabel = Label(text="Second Number")
        layout.add_widget(secondNumberLabel)
        self.secondNumberInput = TextInput(multiline=False)
        layout.add_widget(self.secondNumberInput)

        # Third Row
        self.calculateButton = Button(text="Multiply")
        self.calculateButton.bind(on_press=self.handle_click)
        layout.add_widget(self.calculateButton)

        self.resultLabel = Label(text="")
        layout.add_widget(self.resultLabel)

    def handle_click(self):
        result = self.get_first_number() * self.get_second_number()
        self.resultLabel.text = "Result: " + str(result)

    def get_first_number(self):
        return int(self.firstNumberInput.text)
    
    def get_second_number(self):
        return int(self.secondNumberInput.text)
        