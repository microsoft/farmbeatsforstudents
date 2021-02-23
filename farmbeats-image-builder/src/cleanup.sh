#!/bin/bash

###================================###
header "CLEANING UP"

comment "removing loopback device"
losetup -d ${LOOP}
losetup

comment "deleting ${IMG_NEW}"
rm ${IMG_NEW}
