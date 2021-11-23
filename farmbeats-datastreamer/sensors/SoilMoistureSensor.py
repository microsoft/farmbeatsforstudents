from sensors.BaseSensor import BaseSensor
from jacdac import Bus
from jacdac.soil_moisture import SoilMoistureClient


class SoilMoistureSensor(BaseSensor):
    def __init__(self, bus: Bus):
        BaseSensor.__init__(self, bus)
        self.sensor = None
        self.soil_moisture_pin = 0
        self.sensor = SoilMoistureClient(
            self.bus, "soil.moisture")

    def read(self):
        soil_moisture = self.sensor.moisture
        if soil_moisture is None:
            soil_moisture = self.null_value
        else:
            soil_moisture = self.mapNum(soil_moisture, 0, 100, 0.00, 1.00)
            soil_moisture = self.rolling_average(
                soil_moisture, self.measurements, 20)
        return soil_moisture
