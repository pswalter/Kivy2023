import kivy
from random import randint
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

from hiddenimage import HiddenImage

# Images are located at images/pattern_01.jpg ... images/pattern_84.jpg
IMAGE_PREFIX = "images/pattern_"
IMAGE_COUNT = 84

class Board(GridLayout):
    """
    Each cell of the rectangular grid is a hidden image.
    Each image is selected randomly from the collection of JPG files.
    """
    def __init__(self, width, height):
        super().__init__()
        self.cols = width

        for _ in range(width * height):
            image_index = randint(1, IMAGE_COUNT)
            # .zfill pads a number with zeroes, eg. '7'.zfill(3) = '007'
            image_path = IMAGE_PREFIX + str(image_index).zfill(2) + '.jpg'
            cell = HiddenImage(source=image_path, label_text='?')
            self.add_widget(cell)


class Application(App):
    def build(self):
        layout = Board(5, 4)
        return layout

if __name__ == "__main__":
    myApp = Application()
    myApp.run()