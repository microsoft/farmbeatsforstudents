import shelve
import datetime
import subprocess
from sensors.SensorPoller import SensorPoller

class DataSettings:

    def __init__(self):
        self.sensor_poller = SensorPoller(self)
        self.settings_file = 'fbfs.settings'

        self._date_time = ""
        self._soil_temperature = ""
        self._soil_moisture = ""
        self._air_temperature = ""
        self._air_humidity = ""
        self._sunlight_visible = ""
        self._sunlight_uv = ""
        self._sunlight_ir = ""
        self._relay = ""
        self._button = ""
        self._logger_status = "Not Logging"
        self._logging = False
        self._previous_logging_time = 0
        self._load_logs = False
        self._clear_logs = False
        self._polling_interval = 0
        self._agent_duration = 0
        self._previous_agent_time = 0
        self._agent_configuration_set = ""
        self._agent_state = False
        self._agent_update = False
        self._new_date_time = ""
        self._relay_state_change = ""

#-------------------------------------------------------------#
#                         PROPERTIES                          #
#-------------------------------------------------------------#

    # -------------- Sensor Data Properties -----------------#
    def get_date_time(self):
        return self._date_time

    def set_date_time(self, val):
       self._date_time = val

    date_time = property(get_date_time, set_date_time)

    def get_soil_temperature(self):
        return self._soil_temperature

    def set_soil_temperature(self, val):
       self._soil_temperature = val

    soil_temperature = property(get_soil_temperature, set_soil_temperature)
       
    def get_soil_moisture(self):
        return self._soil_moisture

    def set_soil_moisture(self, val):
       self._soil_moisture = val

    soil_moisture = property(get_soil_moisture, set_soil_moisture)

    def get_air_temperature(self):
        return self._air_temperature

    def set_air_temperature(self, val):
       self._air_temperature = val

    air_temperature = property(get_air_temperature, set_air_temperature)

    def get_air_humidity(self):
        return self._air_humidity

    def set_air_humidity(self, val):
       self._air_humidity = val

    air_humidity = property(get_air_humidity, set_air_humidity)

    def get_sunlight_visible(self):
        return self._sunlight_visible

    def set_sunlight_visible(self, val):
       self._sunlight_visible = val

    sunlight_visible = property(get_sunlight_visible, set_sunlight_visible)

    def get_sunlight_uv(self):
        return self._sunlight_uv

    def set_sunlight_uv(self, val):
       self._sunlight_uv = val

    sunlight_uv = property(get_sunlight_uv, set_sunlight_uv)

    def get_sunlight_ir(self):
        return self._sunlight_ir

    def set_sunlight_ir(self, val):
       self._sunlight_ir = val

    sunlight_ir = property(get_sunlight_ir, set_sunlight_ir)

    def get_relay(self):
        return self._relay

    def set_relay(self, val):
       self._relay = val

    relay = property(get_relay, set_relay)

    def get_button(self):
        return self._button

    def set_button(self, val):
       self._button = val

    button = property(get_button, set_button)

    # -------------- Logger Data Properties -----------------#
    def get_logger_status(self):
        return self._logger_status

    def set_logger_status(self, val):
        self._logger_status = val

    logger_status = property(get_logger_status, set_logger_status)

    def get_logging(self):
        return self._logging
    
    def set_logging(self, value):
        self._logging = value

    logging = property(get_logging, set_logging)

    def get_previous_logging_time(self):
        return self._previous_logging_time

    def set_previous_logging_time(self, value):
        self._previous_logging_time = value

    previous_logging_time = property(get_previous_logging_time, set_previous_logging_time)

    def get_load_logs(self):
        return self._load_logs

    def set_load_logs(self, value):
        self._load_logs = value

    load_logs = property(get_load_logs, set_load_logs)

    def get_clear_logs(self):
        return self._clear_logs

    def set_clear_logs(self, value):
        self._clear_logs = value

    clear_logs = property(get_clear_logs, set_clear_logs)

    # -------------- Agent Data Properties ------------------#
    def get_polling_interval(self):
        return self._polling_interval

    def set_polling_interval(self, value):
        self._polling_interval = value

    polling_interval = property(get_polling_interval, set_polling_interval)

    def get_agent_duration(self):
        return self._agent_duration

    def set_agent_duration(self, value):
        self._agent_duration = value

    agent_duration = property(get_agent_duration, set_agent_duration)

    def get_previous_agent_time(self):
        return self._previous_agent_time

    def set_previous_agent_time(self, value):
        self._previous_agent_time = value

    previous_agent_time = property(get_previous_agent_time, set_previous_agent_time)

    def get_configuration_set(self):
        return self._agent_configuration_set

    def set_configuration_set(self, val):
        self._agent_configuration_set = val

    agent_configuration_set = property(get_configuration_set, set_configuration_set)

    def get_agent_state(self):
        if self._agent_state == '1':
            return True
        else:
            return False 

    def set_agent_state(self, value):
        self._agent_state = value

    agent_state = property(get_agent_state, set_agent_state)

    def get_agent_update(self):
        return self._agent_update

    def set_agent_update(self, value):
        self._agent_update = value

    agent_update = property(get_agent_update, set_agent_update)

    # -------------- Date Time Properties -------------------#
    def get_new_date_time(self):
        return self._new_date_time

    def set_new_date_time(self, value):
        self._new_date_time = value

    new_date_time = property(get_new_date_time, set_new_date_time)

    # -------------- Relay State Change Properties ----------#
    def get_relay_state_change(self):
        return self._relay_state_change

    def set_relay_state_change(self, val):
       self._relay_state_change = val

    relay_state_change = property(get_relay_state_change, set_relay_state_change)

#-------------------------------------------------------------#
#                           FUNCTIONS                         #
#-------------------------------------------------------------#

    # ------------- Sensor Functions ------------------------#
    def poll_sensors(self):
        self.sensor_poller.poll_sensors()

    # ------------- String Builder Functions ----------------#
    def build_data_string(self):
        data_string = ""
        #-------------------- sensor data --------------------#
        data_string += self.format(self.date_time.strftime("%m-%d-%Y %H:%M:%S"))
        data_string += ","
        data_string += self.format(self.soil_temperature)
        data_string += ","
        data_string += self.format(self.soil_moisture)
        data_string += ","
        data_string += self.format(self.air_temperature)
        data_string += ","
        data_string += self.format(self.air_humidity)
        data_string += ","
        data_string += self.format(self.sunlight_visible)
        data_string += ","
        data_string += self.format(self.sunlight_uv)
        data_string += ","
        data_string += self.format(self.sunlight_ir)
        data_string += ","
        data_string += self.format(self.relay)
        data_string += ","
        data_string += self.format(self.button)
        data_string += ","
        data_string += self.format(self.logger_status)
        data_string += ","
        data_string += self.format(self.agent_configuration_set)
        data_string += ","
        data_string += self.format(self.agent_state)

        data_string += "\n"
        return data_string

    def format(self, data):
        if data is None:
            return str(data).strip()
        else:
            try:
                return str("{:.2f}".format(float(data))).strip()
            except Exception:
                try:
                    return str(int(data)).strip()
                except Exception:
                    return str(data).strip()

    # ------------- Data Streamer File Functions ------------#
    def process_incoming_serial(self, data_streamer_data):
        if not data_streamer_data == None:
            # print(data_streamer_data)
            try:
                if len(data_streamer_data) >=1:
                    # ------------------ logger_mode ----------------#
                    logger_mode = data_streamer_data[0]

                    if "SL" in logger_mode:  # Start Logging
                        self.logger_status = "Logging"
                        self.logging = True

                    elif "EL" in logger_mode:  # End Logging
                        self.logger_status = "Not Logging"
                        self.logging = False

                    elif "CL" in logger_mode:  # Clear Logs
                        self.clear_logs = True

                    elif "LD" in logger_mode:  # Load Data
                        self.load_logs = True

                    else: # invalid command
                        pass

                    # ------------------ configuration_set ----------------#
                    if len(data_streamer_data) >=2:
                        self.agent_configuration_set = data_streamer_data[1]

                    # ------------------ agent_state ----------------#
                    if len(data_streamer_data) >=3:
                        self.agent_state = data_streamer_data[2]

                    # ------------------ agent_update ----------------#
                    if len(data_streamer_data) >=4:
                        self.agent_update = data_streamer_data[3]

                    # ------------------ update datetime ----------------#
                    if len(data_streamer_data) >=5:
                        self.set_timestamp(data_streamer_data[4])

            except IndexError: # serial failed or cable unplugged
                data_streamer_data == None

            self.save_settings()

    # ------------- DateTime Functions ----------------------#
    def set_timestamp(self, new_date_time):
        if len(new_date_time) > 1:
            try:
                time_pieces = new_date_time.split("_")
                date_time = datetime.datetime.today()
                new_date_time = date_time.replace(
                    year = int(time_pieces[0]),
                    month = int(time_pieces[1]),
                    day = int(time_pieces[2]),
                    hour = int(time_pieces[3]),
                    minute = int(time_pieces[4]),
                    second = int(time_pieces[5])
                )
                subprocess.run(["sudo", "date", "-s", str(new_date_time)])
            except:
                pass

    # ------------- Settings File Functions -----------------#
    def save_settings(self):
        try:
            with shelve.open(self.settings_file, writeback=True) as settings:
                settings['logger_status'] = self.logger_status
                settings['logging'] = self.logging
                settings['previous_logging_time'] = self.previous_logging_time
                settings['polling_interval'] = self.polling_interval
                settings['agent_duration'] = self.agent_duration
                settings['previous_agent_time'] = self.previous_agent_time
                settings['agent_configuration_set'] = self.agent_configuration_set
                settings['agent_state'] = self.agent_state
        except Exception:
            self.save_settings()

    def load_settings(self):
        try:
            with shelve.open(self.settings_file, writeback=True) as settings:
                self.logger_status = settings['logger_status']
                self.logging = settings['logging']
                self.previous_logging_time = settings['previous_logging_time']
                self.polling_interval = settings['polling_interval']
                self.agent_duration = settings['agent_duration']
                self.previous_agent_time = settings['previous_agent_time']
                self.agent_configuration_set = settings['agent_configuration_set']
                self.agent_state = settings['agent_state']
        except KeyError:
            self.save_settings()
            self.load_settings()
        except Exception:
            return