# Raspberry Pi Pico 2 W auto updater

An autoupdater for the rasperry pi pico 2 W.

The target is the directory you wish to replace. 
In many cases it will be:
../repo name

## Use
*NOTE*


Import autoupdater. Then, use autoupdater.checkUpdates() or autoupdater.Update(target). checkUpdates() returns true or false depending on if there is an update, and Update(target) returns 0 or 1 depending on if the update has been succesful. 

If using an SD card, call Update(target) where target contains the mounting path to your sd card.

## Setup instructions

Change the path in path.txt to be your desired repository you will update from.

Example:

https://raw.githubusercontent.com/IcarusGU/Pico2w-autoupdater/main/

Or, if you wish to only use a certain folder within the repo:

https://raw.githubusercontent.com/IcarusGU/Pico2w-autoupdater/main/desiredFolder/

Ensure that there is a file named version.txt within the git repo you are updating from, and that the file contains the version number on the first line. Additionally, version.txt must be top level within whatever folder you are pathing to.

If it is desired, you may connect to wifi for this process by putting the desired wifi information within wifi.txt
Put the wifi ssid on the first line, and wifi password on the second.
Otherwise, it is assumed you are already connected to wifi.
If you do not wish to use this, ensure that wifi.txt is left blank.

### Dependencies

The autoupdater assumes urequests and network are preinstalled on the pico, as they are with most micropython installs. If they are not, please install them.

Additionally, for sd card support you must install the sdcard library.
