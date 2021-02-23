import os

class DataLogger:
    def __init__(self, data_streamer):
        self.data_streamer = data_streamer
        self.log_file = "/home/pi/Documents/farmbeats_log.csv"

    def log_data(self, data_string):
        with open(self.log_file, "a") as file:
            file.write(data_string)

    def clear_logs(self):
        with open(self.log_file, "w+") as file:
            file.write("")

    def delete_log(self):
        if os.path.isfile(self.log_file):
            os.remove(self.log_file)

    def get_rows(self):
        rows = 0
        with open(self.log_file, "r") as file:
            for line in file:
                rows += 1
        return rows

    def load_logs(self):
        if os.path.isfile(self.log_file):
            self.read_log_rows()
        else:
            open(self.log_file, "a")
            if os.path.isfile(self.log_file):
                self.read_log_rows()

    def read_log_rows(self):
        rows = self.get_rows()
        self.data_streamer.send_data(",,,,,,,,,,Start Load Data Log")
        with open(self.log_file, "r") as file:
            i = 0
            while i <= rows:
                if (i == rows):
                    break
                logData = file.readline()
                self.data_streamer.send_data(logData)
                i += 1
        self.data_streamer.send_data(",,,,,,,,,,End Load Data Log,,,," + str(rows) + " rows loaded")