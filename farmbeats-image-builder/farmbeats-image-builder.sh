#!/bin/bash

printf "\n\n"
echo "##################################################"
echo "--------------------------------------------------"
echo "           START FARMBEATS IMAGE BUILDER"
echo "--------------------------------------------------"
echo "##################################################"
printf "\n\n"

FBFS_GEN_DIR=${PWD}
FBFS_IMAGE_NAME="fbfs"
DEFAULT_IMG_VERSION=0.0.0
IMAGES_DIRECTORY=./images

# update URL/filenames to use newer/older releases
RASPBERRY_PI_OS_DOWNLOAD_URL=https://downloads.raspberrypi.org/raspios_armhf/images/raspios_armhf-2021-01-12/2021-01-11-raspios-buster-armhf.zip
RASPBERRY_PI_OS_DOWNLOAD=2021-01-11-raspios-buster-armhf
IMG_SRC=./${RASPBERRY_PI_OS_DOWNLOAD}.img

source ./src/setup.sh
source ./src/user-input.sh
source ./src/download-raspian.sh
source ./src/prepare-image.sh

### MOUNT IMAGE ###
if [ "$INTERACTIVE" = True ];then
    read -r -p "Mount image? [y/n]" response
else
    response="y"
fi
if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]];then
    source ./src/mount-image.sh
fi

### COPY FILES ###
if [ "$INTERACTIVE" = True ];then
    read -r -p "Copy files? [y/n]" response
else
    response="y"
fi
if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]];then
    source ./src/copy-files.sh
fi

### CHROOT ###
if [ "$INTERACTIVE" = True ];then
    read -r -p "Chroot? [y/n]" response
else
    response="y"
fi
if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]];then
    ###================================###
    header "START CHROOT"
    
    # pre configure
    source ./src/pre-chroot.sh
    
    # install farmbeats-datastreamer
    source ./src/install-datastreamer.sh

    header "END CHROOT"
    ###================================###
fi

### UNMOUNT IMAGE ###
if [ "$INTERACTIVE" = True ];then
    read -r -p "Unmount image? [y/n]" response
else
    response="y"
fi
if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]];then
    source ./src/unmount-image.sh
fi

### COMPRESS IMAGE ###
if [ "$INTERACTIVE" = True ];then
    read -r -p "Compress image? [y/n]" response
else
    response="y"
fi
if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]];then
    source ./src/compress.sh
fi

source ./src/cleanup.sh

printf "\n\n"
echo "##################################################"
echo "--------------------------------------------------"
echo "           END FARMBEATS IMAGE BUILDER"
echo "--------------------------------------------------"
echo "##################################################"
printf "\n\n"
