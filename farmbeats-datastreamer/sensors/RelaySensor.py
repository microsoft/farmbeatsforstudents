from sensors.BaseSensor import BaseSensor
from jacdac import Bus
from jacdac.relay import RelayClient


class RelaySensor(BaseSensor):
    def __init__(self, bus: Bus):
        BaseSensor.__init__(self, bus)
        self.sensor = None
        self.soil_moisture_pin = 0
        self.sensor = RelayClient(bus, "relay")

    def read(self):
        relay_state = self.sensor.closed
        if relay_state is None:
            relay_state = self.null_value
        return relay_state

    def on(self):
        self.sensor.closed = True

    def off(self):
        self.sensor.closed = False
