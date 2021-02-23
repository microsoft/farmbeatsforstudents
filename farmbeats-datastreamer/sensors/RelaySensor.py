from sensors.BaseSensor import BaseSensor
from grove.grove_relay import GroveRelay

class RelaySensor(BaseSensor):
    def __init__(self):
        BaseSensor.__init__(self)
        self.sensor = None
        self.soil_moisture_pin = 0
        self.relay_pin = 22
        self.setup()

    def setup(self):
        try:
            self.sensor = GroveRelay(self.relay_pin)
            self.init = True
        except Exception as e:
            print("RelaySensor.setup: " + str(e))
            self.init = False

    def read(self):
        try:
            if not self.init:
                self.setup()
            relay_state = self.sensor.read()
        except Exception as e:
            print("RelaySensor.read: " + str(e))
            self.init = False
            relay_state = self.null_value
        finally:
            return relay_state

    def on(self):
        self.sensor.on()

    def off(self):
        self.sensor.off()