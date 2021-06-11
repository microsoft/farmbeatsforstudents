[https://github.com/microsoft/farmbeatsforstudents/tree/main/farmbeats-image-builder](https://github.com/microsoft/farmbeatsforstudents/tree/main/farmbeats-image-builder)

# FarmBeats Image Builder

The FarmBeats Image Builder is a tool used to produce a custom Raspberry Pi OS SD card image for the FarmBeats for Students Grove Smart Agriculture Kit.

## SD card image releases

**Note:** If you just want to burn the latest SD card image, new releases are always available here:
[https://aka.ms/fbfsimage](https://aka.ms/fbfsimage)

## Prerequisites

This is a shell script that runs on a Raspberry Pi 4 B. This is required so that the image can be virtualized with the correct architecture (ARM).

## Running farmbeats-image-builder.sh

To run the shell script first clone this repository:

```bash
    git clone https://github.com/microsoft/farmbeatsforstudents.git
```

Then navigate to the repo:

```bash
    cd farmbeatsforstudents/farmbeats-image-builder
```

To run the image builder in interactive mode use:

```bash
    sudo ./farmbeats-image-builder.sh --interactive
```

The first time it is best to use --interactive so you get a feel for what the script does. Alternatively you can run it in --noninteractive mode, which will still require input upfront (image name, size, etc) but the majority of the install will run without user input repquired.

```bash
    sudo ./farmbeats-image-builder.sh --noninteractive
```

## How the build process works

The bash script will prompt the user for an image version number and the size to expand the image prior to installing farmbeats-datastreamer. Using this input, the build script loads a Raspberry Pi OS image file onto a loopback device, expands the image partition, and mounts the image into a local folder. A few virtualized directories from the host are attached and the script then installs packages, files, and services onto the image. Once insallation is complete, the image is then compressed and place in the `images/` folder. You are now ready to write to an SD card.

## Build files

The following files are used to build the image:

* 'farmbeats-image-builder.sh`
  * The main shell script

* `setup.sh`
  * reads command line arguments
  * defines echo format

* `user-input.sh`
  * Prompts user for
    * image version number (0.0.0) default)
    * image expansion size (1024 MB default)

* `download-raspian.sh`
  * Downloads the 2021-01-11 Raspbeery Pi OS Buster for arm image archive
  * Extracts image archive to the root folder
  * The image version can be changed in `farmbeats-image-builder.sh` in teh root folder.

* `prepare-image.sh`
  * Expand image partition
  * Load image as a loopback device
  * Check file system
  * Resize partition
  * Recheck file system
  * Expand file system to expanded partition

* `mount-image.sh`
  * Creates a mount point for the image (local system directory)
  * Mounts the `root` and `boot` partitions
  * Binds virtualized directories from the host so image can boot

* `copy-files.sh`
  * Copies `farmbeats-datastreamer` directory onto mounted image`

* `pre-chroot.sh`
  * Sets language and localiaztion settings so that packages can install properly

* `install-datastreamer.sh`
  * Update and upgrade Raspbberry Pi OS
  * Install python dependencies
  * Installs Remote Desktop (xrdp)
  * Install and configure services:
    * farmbeats-datastreamer
      * Runs `farmbeats-datastreamer/main.py` at startup
    * farmbeats-interfaces
      * On first boot checks that `xrdp` is installed and the following interfaces are enabled:
        * Camera
        * SSH
        * SPI
        * I2C
        * Serial port (uart)
        * OneWire
        * Remote GPIO

* `unmount-image.sh`
  * Unmounts the image partitions and bindings from the mount points

* `compress.sh`
  * Compresses image into a `zip` archive

* `cleanup.sh`
  * Removes loopback device
  * Deletes working image file
