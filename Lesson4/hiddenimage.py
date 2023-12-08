import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout

class HiddenImage(BoxLayout):
    """
    A BoxLayout which contains EITHER a label or an image, depending on
    the value of the Boolean self.visible flag.

    On touch up event, self.visible switches between True and False
    """

    def __init__(self, source):
        """
        source (str): location of the image file (must be .jpg format)
        """
        super().__init__()
        self.image_filename = source
        self.image = Image(source=self.image_filename,
                           size_hint=(1, 1),
                           allow_stretch=True)
        self.label = Label(text="Click to reveal",
                           size_hint=(1,1),
                           font_size=36)
        self.visible = False
        # Note that self.image and self.label exist as attributes of an instance
        # of Hidden image, but only one of them is added to the visual layout.
        self.add_widget(self.label)

    def toggle_visible(self):
        self.visible = not self.visible
        if self.visible:
            self.remove_widget(self.label)
            self.add_widget(self.image)
        else:
            self.remove_widget(self.image)
            self.add_widget(self.label)

    def on_touch_up(self, touch):
        """
        This method exists in Widget and is overridden in this child class.
        It is triggered every time mouse button is released after the click
        happened on the widget or one of its children.
        """
        self.toggle_visible()
        # You can see the details of the touch_up event by uncommenting below:
        # print(touch)
        
        # Call the overridden on_touch_up of the BoxLayout
        # It is good practice to always do this when handling events in Kivy.
        return super().on_touch_up(touch)

class Application(App):
    def build(self):
        layout = HiddenImage(source='images/landscape.jpg')
        return layout

if __name__ == "__main__":
    myApp = Application()
    myApp.run()
