from sensors.BaseSensor import BaseSensor
import time
from jacdac import Bus
from jacdac.thermometer import ThermometerClient
from jacdac.humidity import HumidityClient

class AirTemperatureHumiditySensor(BaseSensor):
    def __init__(self, bus: Bus):
        BaseSensor.__init__(self, bus)

        self.humidity_measurements = []
        self.temperature_measurements = []
        self.humidity_sensor = HumidityClient(self.bus, "air.humidity")
        self.temperature_sensor = ThermometerClient(self.bus, "air.temperature")

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
        air_humidity = self.humidity_sensor.humidity
        if air_humidity is None:
            air_humidity = self.null_value
        air_temperature = self.temperature_sensor.temperature
        if air_temperature is None:
            air_temperature = self.null_value
        
        return air_humidity, air_temperature
