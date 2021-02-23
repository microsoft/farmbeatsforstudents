#!/bin/bash

###================================###
header "UNMOUNTING IMAGE"

comment "unmounting image"
umount /mnt/rpi/{dev/pts,dev,etc/resolv.conf,sys,proc,boot,}

comment "deleting mount point"
rm -r /mnt
