# Raspberry Pi Pico 2 W auto updater

An autoupdater for the rasperry pi pico 2 W.

The target is the directory you wish to replace. 
In many cases it will be:
../<repo name>

## Use

Import autoupdater. Then, use autoupdater.checkUpdates() or autoupdater.Update(<path to target>). checkUpdates() returns true or false depending on if there is an update, and Update(<path to target>) returns 0 or 1 depending on if the update has been succesful. 

If using an SD card, call UpdateSD(<path to target>)

## Setup instructions

Change the path in path.txt to be your desired repository you will update from.

Example:

https://raw.githubusercontent.com/IcarusGU/Pico2w-autoupdater/main/

Or, if you wish to only use a certain folder within the repo:

https://raw.githubusercontent.com/IcarusGU/Pico2w-autoupdater/main/desiredFolder

Ensure that there is a top level file named version.txt within the git repo you are updating from.

If it is desired, you may connect to wifi for this process by putting the desired wifi information within wifi.txt
Otherwise, it is assumed you are already connected to wifi.
