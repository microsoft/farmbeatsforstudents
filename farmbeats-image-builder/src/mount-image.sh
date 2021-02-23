#!/bin/bash

###================================###
header "MOUNTING IMAGE"

comment "create mount point: /mnt"
mkdir -p /mnt
comment "create mount point: /mnt/rpi"
mkdir -p /mnt/rpi
comment "create mount point: /mnt/rpi/boot"
mkdir -p /mnt/rpi/boot

comment "mount partitions"
mount -o rw ${LOOP}p2 /mnt/rpi
mount -o rw ${LOOP}p1 /mnt/rpi/boot

comment "mount binds"
mount --bind /etc/resolv.conf /mnt/rpi/etc/resolv.conf
mount --bind /dev /mnt/rpi/dev/
mount --bind /dev/pts /mnt/rpi/dev/pts
mount --bind /sys /mnt/rpi/sys/
mount --bind /proc /mnt/rpi/proc/

comment "${LOOP} mounted at /mnt/rpi"
