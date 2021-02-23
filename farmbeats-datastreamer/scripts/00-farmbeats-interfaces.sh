#!/bin/bash

FILE=/home/pi/farmbeats-datastreamer/scripts/fbfs-resolution
if [ -f "$FILE" ]; then
    echo "fbfs-resolution already set"
else
	#set interfaces
	source /home/pi/farmbeats-datastreamer/scripts/01-farmbeats-setup-interfaces.sh
	#set default resolution for remote desktop/vnc
	sudo raspi-config nonint do_resolution 2 85
	#add first run flag
	sudo touch $FILE
	sudo reboot now
	exit
fi

source /home/pi/farmbeats-datastreamer/scripts/01-farmbeats-setup-interfaces.sh
source /home/pi/farmbeats-datastreamer/scripts/04-farmbeats-xrdp.sh

exit
