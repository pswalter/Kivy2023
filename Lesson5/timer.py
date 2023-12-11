import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock

# Font size to use for the countdown and the revealed message.
FONT_SIZE = 96

class CountdownLabel(Label):
    """
    A label showing countdown starting at [time] seconds
    and displaying a message [secret] when the time runs out
    """

    def __init__(self, secret: str, time: int):
        super().__init__()
        assert time > 0, 'time has to be a positive integer'
        self.font_size = FONT_SIZE
        self.secret = secret
        self.time = time
        # Widget starts as active showing [time] left
        self.active = True
        self.text = str(time)

        # Schedule a call to self.tick() one second from now
        # Note that scheduled function must take exactly one argument (dt)
        Clock.schedule_once(self.tick, 1)

    def tick(self, dt):
        if not self.active: return
        # dt is the time interval that has passed between scheduling the event
        #   and the function being automatically called.
        # It will be close to the time delay requested in schedule_once,
        #   but it is not guaranteed it will be exactly equal to it.
        print(dt)

        # Subtract one from the countdown timer and adjust the label to show it.
        self.time -= 1
        self.text = str(self.time)

        # If timer reached zero, deactivate countdown and reveal secret.
        if self.time <= 0:
            self.active = False
            self.text = self.secret
        # Otherwise schedule self.tick() to be called one second from now.
        else:
            Clock.schedule_once(self.tick, 1)


class Application(App):
    def build(self):
        return CountdownLabel(secret='BOOM!', time=10)

if __name__ == "__main__":
    myApp = Application()
    myApp.run()
    