import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class DataModel:

    def change_turn(self):
        if self.turn == 'O':
            self.turn = 'X'
        else:
            self.turn = 'O'

    def check_winner(self):
        """Checks if the game is in an ending position.
           If so, stores the game outcome in self.winner, which it returns.
        """

        # Check each column
        for col in range(3):
            if (self.board[col][0] == self.board[col][1] and
                self.board[col][0] == self.board[col][2] and
                self.board[col][0] != ' '):
                self.winner = self.board[col][0]
        
        # Check each row
        for row in range(3):
            if (self.board[0][row] == self.board[1][row] and
                self.board[0][row] == self.board[2][row] and
                self.board[0][row] != ' '):
                self.winner = self.board[0][row]

        # Check diagonals
        if (self.board[0][0] == self.board[1][1] and
            self.board[0][0] == self.board[2][2] and
            self.board[0][0] != ' '):
            self.winner = self.board[0][0]
        if (self.board[2][0] == self.board[1][1] and
            self.board[2][0] == self.board[0][2] and
            self.board[2][0] != ' '):
            self.winner = self.board[2][0]

        # Check for draw (board fully filled in)
        if (' ' not in self.board[0] and ' ' not in self.board[1] and
            ' ' not in self.board[2] and self.winner is None):
            self.winner = 'draw'

        return self.winner
    
    def place(self, row, col):
        '''Registers a move at (col, row), updating game state.
           Cell must be empty to make this move.
           Returns char: the symbol just placed on the board.
        '''
        assert self.board[col][row] == ' ', 'Attempt to place in non-empty cell.'
        self.board[col][row] = self.turn
        self.check_winner()
        self.change_turn()
        return self.board[col][row]

    def __init__(self):
        self.board = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
        self.winner = None
        self.turn = 'O'

class Application(App):
    """Application consists of two parts: Label and GridLayout positioned under each other.
       Label shows game state, GridLayout is 3x3 layout of buttons representing the board.
    """


    def update_info_label(self):
        """Updates the top label showing next player or game outcome (if game over).
        """
        if self.model.winner is None:
            self.info_label.text = f'Next turn: {self.model.turn}'
        elif self.model.winner == 'draw':
            self.info_label.text=  'Game over. Draw.'
        else:
            self.info_label.text = f'Game over. Winner: {self.model.winner}'

        return True

    def create_button(self, row, col):
        """Creates button at [row, col] on the grid and registers the function
           called when the button is clicked (making a move in that cell)
        """
        
        def callback(instance):
            if self.model.winner: return
            if self.model.board[col][row] != ' ': return
            instance.text = self.model.place(row, col)
            self.update_info_label()

        button = Button(text=str(" "), on_press=callback)
        return button

    def build(self):
        self.model = DataModel()
        self.game_over = False

        layout = BoxLayout(orientation='vertical')

        # Note size_hint is the fraction of the parent layout the widget will take.
        # E.g. info_label will take full width and 0.2 of the height of Box Layout.
        self.info_label = Label(text='Current turn: O', size_hint=(1, 0.2))
        self.playing_board = GridLayout(cols=3, size_hint=(1, 0.8))

        for row in range(3):
            for col in range(3):
                current_button = self.create_button(row, col)
                self.playing_board.add_widget(current_button)

        layout.add_widget(self.info_label)
        layout.add_widget(self.playing_board)

        return layout


if __name__ == "__main__":
    myApp = Application()
    myApp.run()