import os
import time
import RPi.GPIO as GPIO

class PowerButton():
    def __init__(self, power_pin):
        self.power_pin = power_pin
        self.power_button_connected = False
        self.setup()

    def setup(self):
        try:
            GPIO.setup(self.power_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.add_event_detect(self.power_pin, GPIO.FALLING, callback=self.button_callback, bouncetime=500)
            self.init = True
        except Exception as e:
            print("PowerButton.setup: " + str(e))
            self.init = False

    def button_callback(self, channel):
        start_time = time.time()
        while GPIO.input(channel) == 0:  # Wait for the button up
            pass
        buttonTime = time.time() - start_time  # How long was the button down?
        if buttonTime >= 6:
            print ("sudo shutdown -h now")
            os.system("sudo shutdown -h now")
        elif buttonTime >= 3:
            print ("sudo reboot")
            os.system("sudo reboot")

    def button_state(self):
        # Grove Dual Button (0)
        try:
            if not self.init:
                self.setup()
            if (GPIO.input(self.power_pin) == GPIO.LOW):
                return 1
            else:
                return 0
        except Exception as e:
            print("PowerButton.button_state: " + str(e))
            self.init = False
            return 0