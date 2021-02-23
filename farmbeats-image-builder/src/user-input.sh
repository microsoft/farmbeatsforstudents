#!/bin/bash

###================================###
header "COLLECTING INPUT"

# get image version
read -r -p "Input image version: [0.0.0]" IMG_VERSION
IMG_VERSION=${IMG_VERSION:-${DEFAULT_IMG_VERSION}}
IMG_NEW=./${FBFS_IMAGE_NAME}.${IMG_VERSION}.img

# get expansion size
read -r -p "Input image expansion size in MB: [1024]" SIZE
SIZE=${SIZE:-1024}

###================================###
# confirm input
header "CONFIRM INPUT"
echo "Source image: ${IMG_SRC}"
echo "Output image: ${IMAGES_DIRECTORY}/${IMG_NEW}.zip"
echo "Expansion size for installations: ${SIZE}"

printf "\n\n"

read -r -p "Is this information correct? [y/n]" response
if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]
then
    echo   
else
    exit
fi
