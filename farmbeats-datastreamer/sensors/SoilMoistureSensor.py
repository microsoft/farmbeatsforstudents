from sensors.BaseSensor import BaseSensor
from grove.adc import ADC

class SoilMoistureSensor(BaseSensor):
    def __init__(self):
        BaseSensor.__init__(self)
        self.sensor = None
        self.soil_moisture_pin = 0
        self.setup()

    def setup(self):
        try:
            self.sensor = ADC()
            self.init = True
        except Exception as e:
            print("SoilMoistureSensor.setup: " + str(e))
            self.init = False

    def read(self):
        try:    # connect Grove Capacitive Soil Moisture Sensor (4096-0) - Dry ~2504 Wet ~1543
            if not self.init:
                self.setup()
            soil_moisture = self.sensor.read_raw(self.soil_moisture_pin)
            soil_moisture = self.mapNum(soil_moisture, 2504, 1543, 0.00, 1.00)
            soil_moisture = self.rolling_average(soil_moisture, self.measurements, 20)
        except Exception as e:
            print("SoilMoistureSensor.read: " + str(e))
            soil_moisture = self.null_value
            self.init = False
        finally:
            return soil_moisture