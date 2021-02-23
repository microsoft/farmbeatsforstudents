#!/bin/bash

comment "Installing FarmBeats For Students - Data Streamer"

cat << EOF | chroot /mnt/rpi /bin/bash --login

source /home/pi/farmbeats-datastreamer/scripts/02-farmbeats-update-upgrade.sh
source /home/pi/farmbeats-datastreamer/scripts/03-farmbeats-python-dependencies.sh
source /home/pi/farmbeats-datastreamer/scripts/04-farmbeats-xrdp.sh

# farmbeats-datastreamer.service
sudo cp /home/pi/farmbeats-datastreamer/services/farmbeats-datastreamer.service /etc/systemd/system
sudo chmod 664 /etc/systemd/system/farmbeats-datastreamer.service
sudo systemctl enable farmbeats-datastreamer.service

# farmbeats-interfaces.service
sudo cp /home/pi/farmbeats-datastreamer/services/farmbeats-interfaces.service /etc/systemd/system
sudo chmod 664 /etc/systemd/system/farmbeats-interfaces.service
sudo systemctl enable farmbeats-interfaces.service

exit
EOF
