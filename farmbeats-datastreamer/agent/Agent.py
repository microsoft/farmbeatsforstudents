class Agent:

    def __init__(self, data_settings, relay):
        self.data_settings = data_settings
        self.relay = relay

        self._update = ""
        #Rule Set 1
        self._sensor1 = None
        self._comparator1 = ""
        self._threshold1 = 0.00
        self._sensor1_value = 0.00
        self._rule_set_1 = False
        self._rule_set_1_result = False

        #Rule Set 2
        self._conditional2 = "AND"
        self._sensor2 = None
        self._comparator2 = ""
        self._threshold2 = 0.00
        self._sensor2_value = 0.00
        self._rule_set_2 = False
        self._rule_set_2_result = False

        #Rule Set 3
        self._conditional3 = "AND"
        self._sensor3 = None
        self._comparator3 = ""
        self._threshold3 = 0.00
        self._sensor3_value = 0.00
        self._rule_set_3 = False
        self._rule_set_3_result = False

#-------------------------------------------------------------#
#                         PROPERTIES                          #
#-------------------------------------------------------------#

    def get_relay_state(self):
        return self._relay_state

    def set_relay_state(self, value):
        self._relay_state = value
        if value == 1:
            self.relay.on()
        else:
            self.relay.off()

    relay_state = property(get_relay_state, set_relay_state)

    def get_update(self):
        return self._update

    def set_update(self, value):
        self._update = value

    update = property(get_update, set_update)

#-------------------------------------------------------------#
#                           FUNCTIONS                         #
#-------------------------------------------------------------#
    def update(self):
        self._process_update()
        self._process_config_set()

    def _process_update(self):
        if self.data_settings.agent_configuration_set == '' or self.data_settings.agent_configuration_set == None:
            return
        else:
            configuration_set = self.data_settings.agent_configuration_set.split(":")

            if len(configuration_set) < 5:
                self._is_set = False
                return

            # append None for each empty value in Configuration Set
            if not len(configuration_set) == 13:
                for i in range(len(configuration_set), 13+1):
                    configuration_set.append(None)

            #Configuration Set
            self.data_settings.polling_interval = configuration_set[0]
            self.data_settings.agent_duration = configuration_set[1]

            #Rule Set 1
            self._sensor1 = configuration_set[2]
            self._comparator1 = configuration_set[3]
            self._threshold1 = configuration_set[4]

            #Rule Set 2
            self._conditional2 = configuration_set[5]
            self._sensor2 = configuration_set[6]
            self._comparator2 = configuration_set[7]
            self._threshold2 = configuration_set[8]

            #Rule Set 3
            self._conditional3 = configuration_set[9]
            self._sensor3 = configuration_set[10]
            self._comparator3 = configuration_set[11]
            self._threshold3 = configuration_set[12]

            self.data_settings.agent_update = False

    def _process_config_set(self):
        if self.data_settings.polling_interval == None or self.data_settings.agent_duration == None:
            return

        if self._sensor1 == None or self._comparator1 == None or self._threshold1 == None:
            self._rule_set_1 =  False
            return
        else:
            if self._is_number(self._sensor1)and self._is_number(self._threshold1):
                self._rule_set_1 = True
            else:
                self._rule_set_1 = False
                return

        if self._sensor2 == None or self._comparator2 == None or self._threshold2 == None:
            self._rule_set_2 =  False
        else:
            if self._is_number(self._sensor2) and self._is_number(self._threshold2):
                self._rule_set_2 = True
            else:
                self._rule_set_2 = False


        if self._sensor3== None or self._comparator3 == None or self._threshold3 == None:
            self._rule_set_3 =  False
        else:
            if self._is_number(self._sensor3) and self._is_number(self._threshold3):
                self._rule_set_3 = True
            else:
                self._rule_set_3 = False

    def rule_sets_result(self):
        sensor_values = [
            self.data_settings.soil_temperature,
            self.data_settings.soil_moisture,
            self.data_settings.air_temperature,
            self.data_settings.air_humidity,
            self.data_settings.sunlight_visible,
            self.data_settings.sunlight_uv,
            self.data_settings.sunlight_ir,
            self.data_settings.button
        ]

        #set sensor values/process rule sets
        if self._rule_set_1:
            try:
                self._sensor1_value = sensor_values[int(self._sensor1)]
                self._rule_set_1_result = self._process_rule_set(self._sensor1_value, self._comparator1, self._threshold1)
            except Exception as e:
                print(e)
                self._rule_set_1_result = False
        if self._rule_set_2:
            try:
                self._sensor2_value = sensor_values[int(self._sensor2)]
                self._rule_set_2_result = self._process_rule_set(self._sensor2_value, self._comparator2, self._threshold2)
            except Exception as e:
                print(e)
                self._rule_set_2_result = False
        if self._rule_set_3:
            try:
                self._sensor3_value = sensor_values[int(self._sensor3)]
                self._rule_set_3_result = self._process_rule_set(self._sensor3_value, self._comparator3, self._threshold3)
            except Exception as e:
                print(e)
                self._rule_set_3_result = False

        #set relay state
        if self._rule_set_1 and self._rule_set_2 and self._rule_set_3:
            if self._rule_set_1_result and self._rule_set_2_result and self._rule_set_3_result:
                return True
            else:
                return False
        elif self._rule_set_1 and self._rule_set_2:
            if self._rule_set_1_result and self._rule_set_2_result:
                return True
            else:
                return False
        elif self._rule_set_1:
            if self._rule_set_1_result:
                return True
            else:
                return False
        else:
            return False

    def activate_agent(self, state):
        if state:
            self.relay.on()
        else:
            self.relay.off()

    def _is_number(self, string):
        try:
            float(string)
            return True
        except ValueError:
            try:
                int(string)
                return True
            except ValueError:
                return False

    def _process_rule_set(self, sensor_value, comparator, threshold):
        sensor_value = self._str_to_num(sensor_value)
        threshold = self._str_to_num(threshold)
        try:
            if comparator == "<":
                return (sensor_value < threshold)
            elif comparator == ">":
                return (sensor_value > threshold)
            elif comparator == "<=":
                return (sensor_value <= threshold)
            elif comparator == ">=":
                return (sensor_value >= threshold)
            elif comparator == "==":
                return (sensor_value == threshold)
            else:
                return None
        except:
            return None

    def _str_to_num(self, num):
        if isinstance(num, int):
            return num
        elif isinstance(num, float):
            return num
        else:
            try:
                return int(num)
            except Exception:
                try:
                    return float(num)
                except Exception:
                    return str(num)