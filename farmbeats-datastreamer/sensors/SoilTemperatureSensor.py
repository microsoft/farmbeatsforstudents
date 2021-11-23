from sensors.BaseSensor import BaseSensor
from jacdac import Bus
from jacdac.thermometer import ThermometerClient


class SoilTemperatureSensor(BaseSensor):
    def __init__(self, bus: Bus):
        BaseSensor.__init__(self, bus)
        self.sensor = ThermometerClient("soil.temperature")

    def read(self):
        soil_temperature = self.sensor.temperature
        if soil_temperature is None:
            soil_temperature = self.null_value
        else:
            soil_temperature = self.rolling_average(
                soil_temperature, self.measurements, 10)
