import os
import time
from jacdac import Bus
from jacdac.button import ButtonClient


class PowerButton():
    def __init__(self, bus: Bus):
        self.bus = bus
        self.client = ButtonClient(self.bus, "powerbutton")
        self.client.on_up(self.handle_up)

    def handle_up(elapsed: int):
        buttonTime = elapsed * 1000
        if buttonTime >= 6:
            print("sudo shutdown -h now")
            os.system("sudo shutdown -h now")
        elif buttonTime >= 3:
            print("sudo reboot")
            os.system("sudo reboot")
