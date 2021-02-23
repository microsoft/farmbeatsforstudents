#!/bin/bash

###================================###
header "COMPRESSING IMAGE"

if [ ! -d "$IMAGES_DIRECTORY" ];then
    mkdir ${IMAGES_DIRECTORY}
fi

comment "zipping ${IMG_NEW}. This may take a few minutes"
zip ${IMAGES_DIRECTORY}/${IMG_NEW}.zip ${IMG_NEW}
