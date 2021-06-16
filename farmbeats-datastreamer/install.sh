#!/bin/bash

printf "\n\n"
echo "##################################################"
echo "--------------------------------------------------"
echo "  STARTING FARMBEATS-DATASTREAMER INSTALLATION"
echo "--------------------------------------------------"
echo "##################################################"
printf "\n\n"

header() {
    printf "\n"
    echo "##################################################"
    echo "###     ${1}"
    echo "##################################################"
    printf "\n"
}

header "Your Pi will reboot after installation."

# setup pi for farmbeats datastreamer
header "raspberyy pi update and upgrade"
source ./scripts/02-farmbeats-update-upgrade.sh

header "installing python dependencies"
source ./scripts/03-farmbeats-python-dependencies.sh

header "installing remote desktop server"
source ./scripts/04-farmbeats-xrdp.sh

header "copying main farmbeats-datastreamer folder to /home/pi"
sudo cp -r ../farmbeats-datastreamer/ /home/pi

# farmbeats-datastreamer.service
header "moving farmbeats-datastreamer.service to systemd"
sudo cp /home/pi/farmbeats-datastreamer/services/farmbeats-datastreamer.service /etc/systemd/system

header "enabling farmbeats-datastreamer.service"
sudo chmod 664 /etc/systemd/system/farmbeats-datastreamer.service
sudo systemctl enable farmbeats-datastreamer.service

# farmbeats-interfaces.service
header "moving farmbeats-interfaces.service to systemd"
sudo cp /home/pi/farmbeats-datastreamer/services/farmbeats-interfaces.service /etc/systemd/system

header "enabling farmbeats-interfaces.service"
sudo chmod 664 /etc/systemd/system/farmbeats-interfaces.service
sudo systemctl enable farmbeats-interfaces.service

printf "\n\n"
echo "##################################################"
echo "--------------------------------------------------"
echo "  COMPLETED FARMBEATS-DATASTREAMER INSTALLATION"
echo "--------------------------------------------------"
echo "##################################################"
printf "\n\n"

printf "\n\n"
echo "*** SYSTEM WILL NOW REBOOT ***"
printf "\n\n"

sudo reboot now
