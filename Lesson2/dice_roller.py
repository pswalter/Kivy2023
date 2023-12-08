import kivy
from random import randint
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

"""
Input: 
* Text input allowing user to enter a dice roll in DnD format
  e.g. 3d6 means rolling three six-sided dice.

Output:
* Label showing the total of the numbers rolled on dice.
* A separate label showing rolls of individual dice.
"""

# Rolling dice with number of sides outside LEGAL_DICE will cause an error.
LEGAL_DICE = [4, 6, 8, 10, 12, 20]
# Rolling more dice than MAX_DICE_COUNT will cause an error.
MAX_DICE_COUNT = 20

# Font sizes for the GUI. It is good practice to declare these as constants.
FONT_LARGE = 48
FONT_SMALL = 18

def validate_input(code):
    """
    Tests if code (str) is a valid input in [num_dice]d[dice_sides] format.
    If input valid, returns two integers:
    * number of dice
    * number of dice sides
    Otherwise, returns None, None
    """
    code = code.lower().strip()

    if "d" not in code: return None, None
    code_sections = code.split("d")
    if len(code_sections) != 2: return None, None

    try:
        dice_count = int(code_sections[0])
        dice_sides = int(code_sections[1])
    except ValueError:
        # At least one of the parts of the code was non-numeric
        return None, None

    return dice_count, dice_sides

class Application(App):

    def build(self):
        layout = BoxLayout(orientation="vertical")
        self.instruction = Label(text="Enter your roll e.g. 3d6",
                                 font_size=FONT_SMALL)
        self.input_box = TextInput(multiline=False,
                                   halign= "center",
                                   font_size=FONT_LARGE)
        self.roll_button = Button(text="ROLL!",
                                  on_press=self.handle_roll,
                                  font_size=FONT_LARGE)
        self.total_label = Label(text="...", font_size=FONT_LARGE)
        self.rolls_label = Label(text="",font_size=FONT_SMALL)

        layout.add_widget(self.instruction)
        layout.add_widget(self.input_box)
        layout.add_widget(self.roll_button)
        layout.add_widget(self.total_label)
        layout.add_widget(self.rolls_label)
        return layout
    

    def handle_roll(self, instance):
        dice_count, dice_sides = validate_input(self.input_box.text)

        if dice_count is None or dice_count <= 0:
            self.rolls_label.text = "Error: Invalid input format."
            self.total_label.text = "..."
        elif dice_sides not in LEGAL_DICE:
            self.rolls_label.text = f"Error: d{dice_sides} does not exist."
            self.total_label.text = "..."
        elif dice_count > MAX_DICE_COUNT:
            self.rolls_label.text = "Error: I do not have this many dice."
            self.total_label.text = "..."
        else:
            # Valid input case: rolling (dice_count) dice:
            # dice is a list of strings for ease of producing rolls_label
            dice = []
            total = 0
            for _ in range(dice_count):
                die_roll = randint(1, dice_sides)
                dice.append(str(die_roll))
                total += die_roll
            self.total_label.text = str(total)
            self.rolls_label.text = f'({",".join(dice)})'


if __name__ == "__main__":
    myApp = Application()
    myApp.run()