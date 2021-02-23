#!/bin/bash

printf "\n\n"
echo "##################################################"
echo "--------------------------------------------------"
echo "  UNINSTALLING FARMBEATS-DATASTREAMER"
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

# remove main application files
header "removing main farmbeats-datastreamer folder"
sudo rm -r /home/pi/farmbeats-datastreamer/

# farmbeats-datastreamer.service
header "disabling farmbeats-datastreamer.service"
sudo systemctl disable farmbeats-datastreamer.service

header "removing farmbeats-datastreamer.service from systemd"
sudo rm /etc/systemd/system/farmbeats-datastreamer.service

# farmbeats-interfaces.service
header "disabling datastreamer.service"
sudo systemctl enable farmbeats-interfaces.service

header "removing farmbeats-interfaces.service from systemd"
sudo mv /home/pi/farmbeats-datastreamer/services/farmbeats-interfaces.service /etc/systemd/system

printf "\n\n"
echo "##################################################"
echo "--------------------------------------------------"
echo "  COMPLETED FARMBEATS-DATASTREAMER UNINSTALL"
echo "--------------------------------------------------"
echo "##################################################"
printf "\n\n"

echo "Press any key to exit."
read waitforkey
