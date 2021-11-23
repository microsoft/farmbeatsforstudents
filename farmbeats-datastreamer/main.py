import threading
import queue
import time
import datetime
from data.DataSettings import DataSettings
from data_streamer.DataStreamer import DataStreamer
from data_logger.DataLogger import DataLogger
from agent.Agent import Agent
from sensors.PowerButton import PowerButton
from sensors.DataButton import DataButton
from sensors.RelaySensor import RelaySensor
from jacdac import Bus

bus = Bus()
data_settings = DataSettings()
data_streamer = DataStreamer()
data_logger = DataLogger(data_streamer)
relay = RelaySensor()
agent = Agent(data_settings, relay)
power_button = PowerButton(bus)
data_button = DataButton(bus)
command_queue = queue.Queue()

def setup():
    data_settings.load_settings()
    agent.update()
    t1 = threading.Thread(target=read_incoming_serial)
    t1.start()

def read_incoming_serial():
    previous_serial_data = ""
    while True:
        serial_data = data_streamer.read_data()
        if not serial_data == None:
            if not serial_data == previous_serial_data:
                command_queue.put(serial_data)
                previous_serial_data = serial_data
        time.sleep(.02)

def main():
    setup()
    previous_agent_time = 0
    while True:
        power_button.button_state()

        if not command_queue.empty():
            data_settings.process_incoming_serial(command_queue.get())

        # ------------------ agent ----------------#
        if data_settings.agent_update:
            agent.update()

        current_time = time.time() # agent polling/activation
        if data_settings.agent_state:
            if current_time - previous_agent_time >= int(data_settings.polling_interval): # activate agent
                agent.activate_agent(agent.rule_sets_result())
                previous_agent_time = current_time

            if current_time - previous_agent_time >= int(data_settings.agent_duration): # deactivate agent
                agent.activate_agent(False)
        else:
            agent.activate_agent(False)

        # ------------------ data streamer ----------------#
        data_settings.poll_sensors()
        data_settings.button = data_button.button_state()
        data_snapshot = data_settings.button
        data_string = data_settings.build_data_string()
        if not data_string == None:
            data_streamer.send_data(data_string)

        # ------------------ data logger ----------------#
        if data_settings.logging:
            logged = False
            if data_settings.previous_logging_time != datetime.datetime.now().hour:
                if datetime.datetime.now().minute <= 2:
                    data_logger.log_data(data_string)
                    data_settings.previous_logging_time = datetime.datetime.now().hour
                    logged = True

            if data_snapshot and not logged:
                data_logger.log_data(data_string)
                logged = True

            if data_settings.relay_state_change and not logged:
                data_logger.log_data(data_string)

        if data_settings.clear_logs: # clear log file on Raspberry Pi
            data_logger.clear_logs()
            data_settings.clear_logs = False

        if data_settings.load_logs: # load logs into Data_streamer/Excel
            data_logger.load_logs()
            data_settings.load_logs = False

        # ------------------ settings ----------------#
        data_settings.save_settings()

if __name__ == '__main__':
    main()