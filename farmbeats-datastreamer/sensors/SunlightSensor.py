from jacdac import uv_index
from sensors.BaseSensor import BaseSensor
from jacdac import Bus
from jacdac.uv_index import UvIndexClient


class SunlightSensor(BaseSensor):
    def __init__(self, bus: Bus):
        BaseSensor.__init__(self, bus)
        self.sensor = None
        self.sunlight_uv_sensor = UvIndexClient(self.bus, "sunlight.uv")

    def read(self):
        # TODO
        #sunlight_visible = self.sensor.ReadVisible
        #sunlight_ir = self.sensor.ReadIR
        sunlight_visible = 0
        sunlight_ir = 0
        sunlight_uv = self.sunlight_uv_sensor.uv_index
        if uv_index is None:
            sunlight_uv = self.null_value
        else:
            sunlight_uv = sunlight_uv / 100
            sunlight_uv = self.rolling_average(
                sunlight_uv, self.measurements, 10)

        return (sunlight_visible, sunlight_uv, sunlight_ir)
