# Rpi Pico 2 W auto updater

An autoupdater for the rasperry pi pico 2 W.

Import autoupdater. Then, use autoupdater.checkUpdates() or autoupdater.Update(). checkUpdates() returns true or false depending on if there is an update, and Update() returns 0 or 1 depending on if the update has been succesful.

The updater will replace the contents of target.txt with the content specified in path if the version installed is lower than the version within the repo when Update() is called.

## Setup instructions

Change the path in path.txt to be your desired repository you will update from.
Then, edit version.txt to be your current version. Ensure that there is a top level file called version.txt within the git repo you are updating from.

If it is desired, you may connect to wifi for this process by putting the desired wifi information within wifi.txt
Otherwise, it is assumed you are already connected to wifi.

