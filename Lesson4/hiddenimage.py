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

    def __init__(self, source, label_text="Click to reveal"):
        """
        source (str): location of the image file (must be .jpg format)
        """
        # Always call the constructor of the superclass when inheriting from
        # Kivy widgets to ensure the widget is properly initialised.
        super().__init__()
        self.image_filename = source
        print(self.size)
        self.image = Image(source=self.image_filename,
                           size_hint=(1, 1),
                           allow_stretch=True)
        self.label = Label(text=label_text,
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
        It is triggered every time mouse button is released after a click.
        """
        # You can see the details of the touch_up event by uncommenting below:
        # print(touch)
        
        # We want to reveal the image ONLY if the click happened on this widget,
        # by default on_touch_up is called regardless of where on the screen
        # the click happened.
        if self.collide_point(touch.pos[0], touch.pos[1]):
            self.toggle_visible()
                 
        # Call the overridden on_touch_up of the BoxLayout
        # It is good practice to always do this when handling events in Kivy.
        return super().on_touch_up(touch)

class Application(App):
    def build(self):
        # Note that label_text parameter takes the default value.
        layout = HiddenImage(source='images/landscape.jpg')
        return layout

if __name__ == "__main__":
    myApp = Application()
    myApp.run()
