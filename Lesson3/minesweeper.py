"""
The basic logic of Minesweeper game:
* positions mines randomly on a grid
* calculates number of mines adjacent to each square
* reveals each cell when clicked

Not supported at this stage:
* flagging mined cells using right-click
* restarting game
* revealing more cells when blank clicked.

Better design, allowing to support these features will appear in later lessons.
"""

import random
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

def get_random_coordinates(width_range, height_range, count):
    """Generates *count* pairs of random integer coordinates
       in the range [0..height_range) x [0..width_range)
    """
    coords = []
    for row in range(height_range):
        for col in range(width_range):
            coords.append((row, col))
    return random.sample(coords, count)


class DataModel:

    def __init__(self, width=8, height=8, bombs=10):
        self.width = width
        self.height = height
        self.bomb_count = bombs
        self.hidden = [[True] * width for _ in range(height)]
        # Stores the number of bombs surrounding each cell on the grid
        self.number = [[0] * width for _ in range(height)]
        self.bomb_positions = get_random_coordinates(width, height, bombs)
        for row, col in self.bomb_positions:
            self.number[row][col] = -1
        
        # Calculate the number of surrounding bombs for each cell.
        # Note this is not the most efficient algorithm to do this.
        for row in range(height):
            for col in range(width):
                if (row, col) in self.bomb_positions:
                    continue
                if (row-1, col-1) in self.bomb_positions:
                    self.number[row][col] += 1
                if (row-1, col) in self.bomb_positions:
                    self.number[row][col] += 1
                if (row-1, col+1) in self.bomb_positions:
                    self.number[row][col] += 1
                if (row, col-1) in self.bomb_positions:
                    self.number[row][col] += 1
                if (row, col+1) in self.bomb_positions:
                    self.number[row][col] += 1
                if (row+1, col-1) in self.bomb_positions:
                    self.number[row][col] += 1
                if (row+1, col) in self.bomb_positions:
                    self.number[row][col] += 1
                if (row+1, col+1) in self.bomb_positions:
                    self.number[row][col] += 1


class Application(App):

    def create_button(self, row, col):
        """Creates button at [row, col], reveals the number when clicked.
        """
        
        def callback(instance):
            if self.game_over: return

            # If bomb clicked, X is revealed and no more clicks are handled. 
            if (row, col) in self.model.bomb_positions:
                print('YOU LOSE')
                instance.text = 'X'
                self.game_over = True
                return
 
            self.model.hidden[row][col] = False
            instance.text = str(self.model.number[row][col])

        button = Button(text=str(" "), on_press=callback)
        return button

    def build(self):
        self.model = DataModel()
        self.game_over = False
        layout = GridLayout(cols=self.model.width)

        for row in range(self.model.height):
            for col in range(self.model.width):
                current_button = self.create_button(row, col)
                layout.add_widget(current_button)

        return layout


if __name__ == "__main__":
    myApp = Application()
    myApp.run()