import RPi.GPIO as GPIO

class DataButton():
    def __init__(self, data_pin):
        self.data_pin = data_pin
        self.button_connected = False
        self.setup()

    def setup(self):
        try:
            GPIO.setup(self.data_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            self.init = True
        except Exception as e:
            print("DataButton.setup: " + str(e))
            self.init = False

    def button_state(self):
        # Grove Dual Button (0)
        try:
            if not self.init:
                self.setup()
            if (GPIO.input(self.data_pin) == GPIO.LOW):
                return 1
            else:
                return 0
        except Exception as e:
            print("DataButton.button_state: " + str(e))
            self.init = False
            return 0