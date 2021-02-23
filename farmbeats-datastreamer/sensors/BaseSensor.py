class BaseSensor():
    def __init__(self):
        self.null_value = 0
        self.sensor = None
        self.measurements = []
        self.upper_reasonable_bound = 200
        self.lower_reasonable_bound = 0

    def setup(self):
        self.sensor = None

    def read(self):
        return None

    def average(self, measurements):
        if len(measurements) != 0:
            return sum(measurements)/len(measurements)
        else:
            return self.null_value

    def rolling_average(self, measurement, measurements, size):
        if measurement == None:
            return None
        if self.lower_reasonable_bound < measurement < self.upper_reasonable_bound:
            if len(measurements) >= size:
                measurements.pop(0)
            measurements.append(measurement)
        return self.average(measurements)

    def mapNum(self, val, old_max, old_min, new_max, new_min):
        try:
            old_range = float(old_max - old_min)
            new_range = float(new_max - new_min)
            new_value = float(((val - old_min) * new_range) / old_range) + new_min
            return new_value
        except Exception:
            return val
