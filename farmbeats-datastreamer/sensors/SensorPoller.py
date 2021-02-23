import datetime
from sensors.RelaySensor import RelaySensor
from sensors.SunlightSensor import SunlightSensor
from sensors.SoilMoistureSensor import SoilMoistureSensor
from sensors.SoilTemperatureSensor import SoilTemperatureSensor
from sensors.AirTemperatureHumiditySensor import AirTemperatureHumiditySensor

class SensorPoller:
    def __init__(self, data_settings):
        self.data_settings = data_settings
        self.null_value = 0

        self.soil_temperature_sensor = SoilTemperatureSensor()
        self.soil_moisture_sensor = SoilMoistureSensor()
        self.air_temperature_humidity_sensor = AirTemperatureHumiditySensor()
        self.sunlight_sensor = SunlightSensor()
        self.relay_sensor = RelaySensor()
        self.previous_relay_state = 0

    def poll_sensors(self):
        self.set_date_time()
        self.set_soil_temperature()
        self.set_soil_moisture()
        self.set_air_temperature_humidity()
        self.set_sunlight()
        self.set_relay()
        self.set_relay_state_change()

    def set_date_time(self):
        date_time = datetime.datetime.now()
        self.data_settings.date_time = date_time

# ------------------ Sensor Data Capture ----------------#
    def set_soil_temperature(self):
        self.data_settings.soil_temperature = self.soil_temperature_sensor.read()

    def set_soil_moisture(self):
        self.data_settings.soil_moisture = self.soil_moisture_sensor.read()

    def set_air_temperature_humidity(self):
        self.data_settings.air_humidity, self.data_settings.air_temperature = self.air_temperature_humidity_sensor.read()

    def set_sunlight(self):
        sunlight_visible, sunlight_uv, sunlight_ir = self.sunlight_sensor.read()
        self.data_settings.sunlight_visible = sunlight_visible
        self.data_settings.sunlight_uv = sunlight_uv
        self.data_settings.sunlight_ir = sunlight_ir

    def set_relay(self):
        self.data_settings.relay = self.relay_sensor.read()

    def set_relay_state_change(self):
        try:
            if self.data_settings.relay == self.previous_relay_state:
                self.data_settings.relay_state_change = False
            else:
                self.data_settings.relay_state_change = True
        except Exception:
            pass
        finally:
            self.previous_relay_state = self.data_settings.relay