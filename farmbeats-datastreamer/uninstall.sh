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
header "removing main farmbeats-datastreamer directory"
sudo rm -r /home/pi/farmbeats-datastreamer/

# farmbeats-datastreamer.service
header "disabling farmbeats-datastreamer.service"
sudo systemctl disable farmbeats-datastreamer.service

# farmbeats-interfaces.service
header "disabling farmbeats-interfaces.service"
sudo systemctl disable farmbeats-interfaces.service

printf "\n\n"
echo "##################################################"
echo "--------------------------------------------------"
echo "  COMPLETED FARMBEATS-DATASTREAMER UNINSTALL"
echo "--------------------------------------------------"
echo "##################################################"
printf "\n\n"

echo "Press any key to exit."
read waitforkey
