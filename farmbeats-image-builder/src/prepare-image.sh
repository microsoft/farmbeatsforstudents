#!/bin/bash

###================================###
header "PREPARING IMAGE"

### EXPAND IMAGE ###
if [ "$INTERACTIVE" = True ];then
    read -r -p "Expand image: [y/n]" response
else
    response="y"
fi
if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ || ${AUTO} -eq 1 ]];then
    ###================================###
    header "EXPANDING IMAGE"
    comment "expanding ${IMG_NEW} by ${SIZE}MiB. This may take a minute"
    dd if=/dev/zero bs=1M count=${SIZE} >> ${IMG_NEW}
fi

comment "loading ${IMG_NEW} onto loopback device"
LOOP=$(losetup -Pf ${IMG_NEW} --show)
losetup

header "RUNNING DISK UTILITIES"

comment "checking filesystem"
e2fsck -f ${LOOP}p2

if [ ${EXPAND} ];then
    comment "resizing partition"
    parted ${LOOP} resizepart 2 100%

    comment "rechecking filesystem"
    e2fsck -f ${LOOP}p2

    comment "resizing filesystem to expanded partition"
    resize2fs ${LOOP}p2
fi

comment "loaded onto loopback device: ${LOOP}"
losetup
