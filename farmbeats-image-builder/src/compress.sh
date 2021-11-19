#!/bin/bash

###================================###
header "COMPRESSING IMAGE"

comment "checking for zip"
if [ $(dpkg-query -W -f='${Status}' zip 2>/dev/null | grep -c "ok installed") -eq 0 ];then
	comment "zip not installed"
    comment "installing zip compression utility"
	apt-get install zip -y;
else
	comment "zip is installed"
fi

if [ ! -d "$IMAGES_DIRECTORY" ];then
    mkdir ${IMAGES_DIRECTORY}
fi

comment "zipping ${IMG_NEW}. This may take a few minutes"
zip ${IMAGES_DIRECTORY}/${IMG_NEW}.zip ${IMG_NEW}
