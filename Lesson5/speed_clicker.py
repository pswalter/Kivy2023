import kivy

from kivy.app import App
from kivy.clock import Clock

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

# Font size to use for the countdown and the revealed message.
FONT_SIZE = 64
# Time between consecutive time frames in seconds
TICK = 0.1


class AppLayout(BoxLayout):
    """
    An application measuring mouse click speed.

    Key Attributes:
    is_active (bool): state (whether application is accepting clicks) 
    time_elapsed (float): time passed (seconds) while in active state 
    click_count (int): number of clicks registered while in active state

    Widgets:
    time_label (Label): shows the value of (time_elapsed)
    score_label (Label): label shows the number of clicks it was subject to while active
    play_button (Button): toggles the game state between active and inactive when pressed
    timer_event (ClockEvent?): None if application state is inactive.
                               If active, stores the clock tick event ran every 0.1 sec.    
    """
    def __init__(self):
        super().__init__()
        self.orientation = 'vertical'
        
        self.time_elapsed = 0.0
        self.click_count = 0
        self.is_active = False
        self.timer_event = None

        self.time_label = Label(text='Time: 0', font_size=FONT_SIZE)
        self.score_label = Label(text='Clicks: 0', font_size=FONT_SIZE,
                                 on_touch_down=self.handle_click)
        self.play_button = Button(text='START', font_size=FONT_SIZE,
                                  on_press=self.toggle_active)
        
        self.add_widget(self.time_label)
        self.add_widget(self.play_button)
        self.add_widget(self.score_label)


    def handle_click(self, instance, event):
        """ Adds 1 to click_count only if the application state is active and
            the click happened within this widget (instance).

            instance (Widget) - the label clicked (typically score_label)
            event (Event) - the mouse click event (containing pos: (x, y))
        """
        # Uncomment the lines below to see the instance and the event
        # print("Instance:", instance)
        # print("Event:", event)
        if self.is_active and instance.collide_point(*event.pos):
            self.click_count += 1
            self.score_label.text = f"Clicks: {self.click_count}"


    def activate(self):
        """Changes application state from INACTIVE to ACTIVE"""
        self.is_active = True
        # self.tick() is scheduled to run every 0.1 sec.
        # Note self.tick() takes one argument (dt) - number of seconds since schedule/call.
        self.timer_event = Clock.schedule_interval(self.tick, TICK)
        self.play_button.text = 'STOP'


    def deactivate(self):
        """Changes application state from ACTIVE to INACTIVE"""
        self.is_active = False
        # Cancel the ClockEvent so that tick() is no longer called every 0.1 sec.
        self.timer_event.cancel()
        self.timer_event = None
        self.play_button.text = 'START'


    def toggle_active(self, instance):
        """Handle click of play_button (which will be the instance)"""
        if self.is_active:
            self.deactivate()
        else:
            self.activate()


    def tick(self, dt):
        # Add the time elapsed since the last call of tick() [or since scheduling
        #  if it had not been called before] to time_elapsed
        self.time_elapsed += dt
        # Update the label text to display total time elapsed.
        # Try to remove rounding to confirm the time is exact.
        self.time_label.text = f"Time: {round(self.time_elapsed, 1)}"


class Application(App):
    def build(self):
        return AppLayout()


if __name__ == "__main__":
    myApp = Application()
    myApp.run()
    