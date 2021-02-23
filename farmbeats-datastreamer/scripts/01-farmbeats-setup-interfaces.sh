#!/bin/bash

# raspi-config settings (0=enable 1=disable)
if [ $(raspi-config nonint get_camera) -eq 1 ]; then
	sudo raspi-config nonint do_camera 0
fi

if [ $(raspi-config nonint get_ssh) -eq 1 ]; then
	sudo raspi-config nonint do_ssh 0
fi

if [ $(raspi-config nonint get_vnc) -eq 1 ]; then
	sudo raspi-config nonint do_vnc 0
fi

if [ $(raspi-config nonint get_spi) -eq 1 ]; then
	sudo raspi-config nonint do_spi 0
fi

if [ $(raspi-config nonint get_i2c) -eq 1 ]; then
	sudo raspi-config nonint do_i2c 0
fi

if [ $(raspi-config nonint get_serial_hw) -eq 1 ]; then
	sudo raspi-config nonint do_serial 1 1
	sudo raspi-config nonint set_config_var enable_uart 1 /boot/config.txt
fi

if [ $(raspi-config nonint get_onewire) -eq 1 ]; then
	sudo raspi-config nonint do_onewire 0
fi

if grep -q -E "gpiopin=5" /boot/config.txt; then
	echo "gpiopin=5 already set"
else
	echo "setting gpiopin=5"
	sudo sed /boot/config.txt -i -e "s/^dtoverlay=w1-gpio/dtoverlay=w1-gpio,gpiopin=5/"
fi

if [ $(raspi-config nonint get_rgpio) -eq 1 ]; then
	sudo raspi-config nonint do_rgpio 0
fi
