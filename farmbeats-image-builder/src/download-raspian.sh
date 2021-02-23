#!/bin/bash

### DOWNLOAD IMAGE ###
if [ ! -f $IMG_SRC ];then
    header "DOWNLOADING RASPBERRY PI OS"
    comment "Downloading Raspberry Pi OS: ${RASPBERRY_PI_OS_DOWNLOAD_URL}"
    wget ${RASPBERRY_PI_OS_DOWNLOAD_URL}

    comment "Unzipping ${RASPBERRY_PI_OS_DOWNLOAD}.zip. This may take a few minutes"
    unzip ./${RASPBERRY_PI_OS_DOWNLOAD}.zip 
    #-d ${IMAGES_DIRECTORY}
    
    comment "Deleting ${RASPBERRY_PI_OS_DOWNLOAD}.zip"
    rm ./${RASPBERRY_PI_OS_DOWNLOAD}.zip
fi

### COPY IMAGE ###
comment "Copying ${IMG_SRC} to ${IMG_NEW}. This may take a few minutes"
cp ${IMG_SRC} ${IMG_NEW}
