from sensors.BaseSensor import BaseSensor
from seeed_ds18b20 import grove_ds18b20

class SoilTemperatureSensor(BaseSensor):
    def __init__(self):
        BaseSensor.__init__(self)
        self.sensor = None
        self.setup()

    def setup(self):
        try:
            self.sensor = grove_ds18b20()
            self.init = True
        except Exception as e:
            print("SoilTemperatureSensor.setup: " + str(e))
            self.init = False

    def read(self):
        try:
            if not self.init:
                self.setup()
            soil_temperature, soil_tempF = self.sensor.read_temp
            soil_temperature = self.rolling_average(soil_temperature, self.measurements, 10)
        except Exception as e:
            print("SoilTemperatureSensor.read: " + str(e))
            soil_temperature = self.null_value
            self.init = False
        finally:
            return soil_temperature