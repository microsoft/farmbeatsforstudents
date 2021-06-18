[https://github.com/microsoft/farmbeatsforstudents/tree/main/farmbeats-datastreamer](https://github.com/microsoft/farmbeatsforstudents/tree/main/farmbeats-datastreamer)

# Introduction

The FarmBeats for Students Grove Smart Agriculture Kit is a garden monitoring system that consists of the Raspberry Pi 4 Small Board Computer (SBC), several environmental sensors that monitor soil and atmospheric conditions, a relay indicator/actuator, and a USB serial cable for data transmission. The data is visualized and analyzed using a custom Excel workbook.

Helpful FarmBeats resources:

* FarmBeats for Students website: [https://aka.ms/farmbeatsforstudents](https://aka.ms/farmbeatsforstudents)
* Purchase the hardware kit: [https://aka.ms/fbfskit](https://aka.ms/fbfskit)
* Download the kit build instructions: [https://aka.ms/fbfsbuildinstructions](https://aka.ms/fbfsbuildinstructions)
* Download the Excel workbook: [https://aka.ms/FBFSWorkbook](https://aka.ms/FBFSWorkbook)

**Note:** The FarmBeats  application requires the hardware kit to be assembled and connected to the Pi.

## Installation

There are 2 ways to install the FarmBeats for Students application on the Pi

* **SD Card Installation:** Write the FarmBeats for Students image to your SD card. Our image has the FarmBeats application pre-installed for a no-code, plug-and-play experience. This is the recommended and supported method.

* **Manual Installation:** This option is best for those that are familiar with the Raspberry Pi and those who want to customize the FarmBeats experience.

### SD Card Installation

Start with our custom Raspberry Pi image with the FarmBeats application pre-installed and configured. This is the recommended method and is perfect for schools and classrooms, and anyone who wants a no-code solution.

To write the FarmBeats image to your SD card:

* Download the latest FarmBeats for Students SD card image here: [https://aka.ms/FBFSImage](https://aka.ms/FBFSImage)
* Write the image to your SD card using the [Raspberry Pi Imager](https://www.raspberrypi.org/software/)
* Place the SD card in the Pi
* Power up the Pi. The 1st boot will take ~2 minutes to configure the FarmBeats application. Subsequent boots will take 30 seconds.
* Done! You are now ready to connect to the [custom Excel workbook](https://aka.ms/FBFSWorkbook) to visualize your sensor data.

**Once the FarmBeats application is installed it will run at boot. You do not need to install anything or do anything else.**

### Manual Installation

Start with a fresh Raspberry Pi OS (32-bit) image using [Raspberry Pi Imager](https://www.raspberrypi.org/software/), or add FarmBeats to your current environment. Manual installation requires the use of the [Raspberry Pi terminal](https://www.raspberrypi.org/documentation/usage/terminal/) and git.

To manually install FarmBeats for Students on the Raspberry Pi:

* Clone this repository:

```bash
  git clone https://github.com/microsoft/farmbeatsforstudents.git
```

* Navigate to the farmbeats-datastreamer directory:

```bash
  cd farmbeatsforstudents/farmbeats-datastreamer
```

* Run install.sh:

```bash
  sudo ./install.sh
```

**Once the FarmBeats application is installed it will run at boot. You do not need to do anything else.**

## Known Issue

There is a known issue with the serial-TTL chipset driver. Please see [this issue](https://github.com/microsoft/farmbeatsforstudents/issues/1).

## What's installed

### farmbeats-datastreamer directory

The farmbeats-datastreamer contains the python code files for the FarmBeats application.

### farmbeats-datastreamer.service

The farmbeats-datastreamer.service file is registered with Systemd and runs every time the Pi boots up, and will recover if it crashes. Its purpose is to run the FarmBeats application and perform the functions described in the next sections.

### farmbeats-interfaces.service

The farmbeats-interfaces.service file is registered with Systemd and runs once every time the Pi boots up. Its purpose is to set the interfaces required for the FarmBeats application to function. By default the following are enabled:

* Camera
* SSH
* VNC
* SPI
* I2C
* Serial Port
* 1-Wire
* Remote GPIO

The Serial Console is disabled to free up the UART for serial communication.

## Raspberry Pi

The Raspberry Pi manages the following:

* Sensor data collection
* Serial data communication
* Data Logger
* Reactive Agent

## Sensors

* Soil Temperature
  One Wire Temperature Sensor DS18B20 <https://www.seeedstudio.com/One-Wire-Temperature-Sensor-p-1235.html>
* Soil Moisture
  Grove Capacitive Soil Moisture Sensor <https://www.seeedstudio.com/Grove-Capacitive-Moisture-Sensor-Corrosion-Resistant.html>
* Grove Air Temperature and Air Humidity
  DHT11 Temperature & Humidity Sensor <https://www.seeedstudio.com/Grove-Temperature-Humidity-Sensor-DHT11.html>
* Sunlight Sensor
  Grove Sunlight Sensor <https://www.seeedstudio.com/Grove-Sunlight-Sensor.html>
* Dual Button
  Grove Dual Button <https://www.seeedstudio.com/Grove-Dual-Button-p-4529.html>
* Relay
  Grove Relay <https://www.seeedstudio.com/Grove-Relay.html>

## Serial Communication

The Raspberry Pi interacts with a custom Excel workbook using the Microsoft Data Streamer Add-in for Excel. Data transmitted from the Pi to Excel will stream into worksheet 'Data In', and data sent from Excel worksheet 'Data Out' streams to the Pi. For more information about Microsoft Data Streamer visit: <https://docs.microsoft.com/en-us/microsoft-365/education/data-streamer/>

Interaction with the Pi can also be managed by any serial terminal program or any device capable of sending and receiving serial data by using the following schema.

### Serial Data Schema

The serial data format is a comma delimited string with a single line ending character.

Example:
`"data1,data2\n"`

#### Serial data transmitted by the Pi

The data transmitted is a series of live data points from sensors and variables that indicate the current state of the Pi.

* Column 1: Raspberry Pi Time
* Column 2: Soil temperature
* Column 3: Soil moisture
* Column 4: Air temperature
* Column 5: Air humidity
* Column 6: Sunlight visible
* Column 7: Sunlight UV
* Column 8: Sunlight IR
* Column 9: Relay State
* Column 10: Blue Button State
* Column 11: Logger Status
* Column 12: Agent Configuration Set
* Column 13: Agent State
* Column 14: Agent Update
* Column 15: Number of rows in data log

Example:
`01-06-2021 12:30:41,22.62,0.01,21,51.7,261,0.02,254,0,0,Logging,10:10:0:<:21.1:AND::::AND:::,1,,`

#### Serial data received by the Pi

The data received is a set of commands that control the program flow on the Raspberry Pi. These commands can be sent to the Pi using the Excel workbook, or a serial terminal program, which is very useful for testing and debugging.

* Column 1: Set Logger Status
* Column 2: Set Agent Configuration Set
* Column 3: Set Agent State
* Column 4: Agent Update Trigger

**Example**
    #SL,10:10:0:<:21.1:AND::::AND:::,1,1

## Data Logger

The Data Logger class manages a log file on the Pi. The following command needs to be entered into **cell A5** on the **Data Out** worksheet in the Excel workbook (Column 1 of the received serial data).

* `#SL` - This will start the data Logger.
* `#EL` - This will stop the data Logger.
* `#CL` - This will clear all data from the log file.
* `#LD` - This will load the data from the CSV log file and send to Excel via Data Streamer one row at a time. When initiated the logger_status is set to 'Start Load Data Log', and upon completion 'End Load Data Log'. A row count is also sent in Column 15

Data is saved to the file `/home/pi/Documents/fbfs_log.csv` on the Raspberry Pi.

## Reactive Agent

The agent observes the environment (Sensors), processes a set of rules (Configuration Set), and acts upon the environment (relay activation).

### Agent Configuration Set

The agent will be configured via Configuration Sets that are defined in the Excel workbook. The agent will run in a loop with parameters that can be modified to affect how it operates. Each Configuration Set will consist of high-level parameters that define the overall operation of the agent, and 1-3 Rule Sets which are sensor/rule configurations that define the specific parameters for monitoring the environment.

Configuration Sets will be entered into **cell B5** on the **Data Out** worksheet in the Excel workbook and sent to the Pi (Column 2 of the received serial data). The Configuration Set will also be transmitted from the Pi to Excel into **column 13** on the **Data In** worksheet in the Excel workbook (Column 12 of the transmitted serial data). This will allow the use of a single computer in the classroom to be used to configure multiple Raspberry Pi devices. The current Configuration Set will always be sent to the workbook upon device connection.

The Agent will act on the Relay. Only one Configuration set will be possible at a time.

#### Configuration Set parameters

* Polling Interval: Interval that sensors are polled for data (sense the environment)
* Agent Duration: Amount of time that the agent turns on the relay (affect the environment)

#### Rule Set parameters

* Sensor: The sensor to be monitored (See section: Sensors below)
* Comparator: The comparison operator (>, <, ==)
* Threshold: The value to compare against (25 degrees C, 65% RH, etc.)
* Conditional: The condition of the optional sensor/rule (AND)

#### Additional Commands

* Agent State: Sets the current state of the agent (ON, OFF)
* Agent Update: Flag to trigger an Agent Update event on the Raspberry Pi (0, 1). When 1 the Raspberry Pi will process the current Configuration Set.

### Agent Data Display

The agent configuration will be sent from the Raspberry Pi to Excel using the Configuration Set schema below. The agent configuration data will be updated and prominently displayed in the Excel workbook.

#### Configuration Set Schema

The agent parameters in the Configuration Set will be sent to the Raspberry Pi as a colon delimited string of data into **cell B5** on the **Data Out** worksheet in the Excel workbook (Column 2 of the received serial data).

##### Sensor Values

* 0 = Soil Temperature
* 1 = Soil Moisture
* 2 = Air Temperature
* 3 = Air Humidity
* 4 = Sunlight Visible
* 5 = Sunlight UV
* 6 = Sunlight IR
* 7 = Button

Comparators
AND | ==

##### Configuration Set Parameters

* PI = Polling Interval
* AD = Agent Duration

##### Default Rule Set (required)

* S1 = Sensor to be monitored (see table below)
* C1 = Comparator for S1
* T1 = Threshold for S1

##### Optional Rule Set 2 (optional)

* X2: Conditional for S2 Rule Set
* S2: Sensor to be monitored (see table below)
* C2: Comparator for S2
* T2: Threshold for S2

##### Optional Rule Set 3 (optional)

* X3: Conditional for S3 Rule Set
* S3: Sensor to be monitored
* C3: Comparator for S3
* T3: Threshold for S3

Example using placeholders:
`PI:AD:S1:C1:T1:X2:S2:C2:T2:X3:S3:C3:T3`

Example using values:
`60:60:1:<:90:AND:3:>:25:AND:4:==:23`

The processing of the Configuration Set will stop after the first empty parameter. Incomplete Rule Sets will be discarded.

Example 1:
Poll every 10 minutes. Active for 30 seconds. Set agent to trigger when air temperature is greater than 60.
`600:30:2:>:60`

Example 2:
Poll every minute. Active for 15 seconds. Trigger when soil moisture is greater than 1000 AND when soil temperature is greater than 100 AND when air humidity is less than 15.
`60:15:2:>:1000:AND:1:>100:AND:4:<:15`

## Timestamp

When the Raspberry Pi is not connected to a network it cannot connect to a time server. To ensure that the timestamp on the collected sensor data is accurate the Pi can receive a timestamp from Excel in **cell the `Data Out` worksheet in cell E5. The format of the timestamp is a `_` delimited string as follows:

`year_month_day_hour_minute_second`

**Example**
To set the date and time to January 4th, 2021 at 6:35am exactly, the string would be:

`2021_1_4_6_35_00`

## Settings

Settings are saved in the `farmbeatsforstudents/farmbeats-datastreamer/` directory in `

## Button Functions

The (red) button attached to D18 is used to reboot or shutdown the Raspberry Pi.

* Press the button for 3 seconds and the Pi will reboot using `sudo reboot`.
  * It will take 30 seconds for the Pi to reboot and reconnect to Data Streamer.
* Press the button for 6 seconds and the Pi will shutdown using `sudo shutdown -h now`.
  * When the green light stops flashing on the Pi, it is safe to unplug it.

The (blue) button attached to D19 will send sensor data to the logger when logger_status = True.

## Data Value Functions

There are a few functions used to format data from sensor readings.

### Number Remap Range

Remap Number in Range works just like map() in the Arduino IDE

**`mapNum(i,OldMax,OldMin,NewMax,NewMin)`**

* `int i` - the number to map.
* `int OldMax` - the upper bound of the value’s current range.
* `int OldMin` - the lower bound of the value’s current range.
* `int NewMax` - the upper bound of the value’s target range.
* `int NewMin` - the lower bound of the value’s target range.

This is used for the soil moisture sensor to reverse the values and remap them to a 0% - 100% value.

### Zero Data Scrubber

For sensors that should never read a value of 0 you can use this function to replace it with a NULL value.

**`scrubData(l)`**

* `int l` - The number that you want to check for 0

This function will take in an integer variable, but it will return a string with a NULL value if the int is 0 or pass on the int as a string.

Note: Do not use this function with sensors that can output valid 0 value data like temperature or Humidity sensors. Light and sound sensors can read low values, but they should never be capable of reading a 0 value except under experimental circumstances.

### Sensor Data Smoothing

To smooth out data from sensors that are susceptible to noise or interference we can apply a Rolling Average and get a more accurate representation of sensor data.

* `rolling_average(measurement, measurements, size)`
  * `Int measurement` – The sensor value to smooth
  * `Int measurements` – Sensor readings array
  * `Int size` – Number of sample readings

The larger the `size` you sample, the smoother the readings, however, the larger your sample `size`, the longer it takes to calculate the average sensor reading each time you read the sensor.

Using `rolling_average()` requires an array for this function to store paste readings into. Create an array for each sensor that has data in need of smoothing. Sensors like the Capacitive Soil Moisture sensor tend to be noisy and will benefit from a sample `size` of 20 readings whereas the DHT11 Air Temp/Humid sensor may only require a sample `size` of 10 to be usable.

You can also set filters for data upper and lower thresholds by changing the values of ` upper_reasonable_bound ` and ` lower_reasonable_bound `.

## Advanced Users

If you are comfortable using the Raspberry Pi, have built project of your own, want to customize the FarmBeats application, or are just curious as to how things work under the hood, this is for you!

### Clone the repository

Start with a fresh Raspberry Pi OS (32-bit) image using [Raspberry Pi Imager](https://www.raspberrypi.org/software/), or add it to your current environment. Once booted open a terminal session.

Clone this repository and navigate to the farmbeats-datastreamer directory:

```bash
  git clone https://github.com/microsoft/farmbeatsforstudents.git
  cd farmbeatsforstudents/farmbeats-datastreamer
```

Now you are ready to explore the FarmBeats application.

**Note:** The FarmBeats application needs to under **root** privileges due to file permissions. This means you will need to run any IDEs as **root** as well. 

### Manually running the python application

If you have already installed FarmBeats using the [instructions above](https://github.com/microsoft/farmbeatsforstudents/tree/main/farmbeats-datastreamer#installation) you will need to either run `uinstall.sh`, or stop the farmbeats-datastreamer service first. This will prevent a dual instance of the application which will cause errors due to instances accessing the same files.

To stop the service:

```bash
  sudo systemctl stop farmbeats-datastreamer
```

Once you are done with your explorations and modifications, save your work and start the service:

```bash
  sudo systemctl start farmbeats-datastreamer
```

To check the status of the service:

```bash
  journalctl -u farmbeats-datastreamer
```

**Note:** Running `main.py` must been done as user **root**. The user **pi** does not have sufficient privileges.
