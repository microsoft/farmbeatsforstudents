from sensors.BaseSensor import BaseSensor
from seeed_dht import DHT
import time

class AirTemperatureHumiditySensor(BaseSensor):
    def __init__(self):
        BaseSensor.__init__(self)

        self.dht_pin = 16
        self.dht_type = '11'
        self.humidity_measurements = []
        self.temperature_measurements = []
        self.sensor = None
        self.setup()

    def setup(self):
        try:
            self.sensor = DHT(self.dht_type, self.dht_pin)
            self.init = True
        except Exception as e:
            print("AirTemperatureHumiditySensor.setup: " + str(e))
            self.init = False

    def read(self):
        air_humidity, air_temperature = self._take_readings()

        if (air_humidity == 0 or air_temperature == 0):
            time.sleep(0.1)
            reH, reT = self._take_readings()
            if (air_humidity == 0):
                air_humidity = reH
            if (air_temperature == 0):
                air_temperature = reT

        air_humidity = self.rolling_average(air_humidity, self.humidity_measurements,10)
        air_temperature = self.rolling_average(air_temperature, self.temperature_measurements,10)

        return air_humidity, air_temperature

    def _take_readings(self):
        try:
            if not self.init:
                self.setup()
            air_humidity, air_temperature = self.sensor.read()

        except Exception as e:
            print("AirTemperatureHumiditySensor.read: " + str(e))
            self.init = False
            air_humidity, air_temperature = self.null_value, self.null_value

        finally:
            return air_humidity, air_temperature
