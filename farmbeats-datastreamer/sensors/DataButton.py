from jacdac import Bus
from jacdac.button import ButtonClient


class DataButton():
    def __init__(self, bus: Bus):
        self.client = ButtonClient(bus, "databutton")

    def button_state(self):
        pressed = self.client.pressed
        if pressed is None:
            pressed = False
        return pressed
