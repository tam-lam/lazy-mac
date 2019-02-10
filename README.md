# lazy-mac
A simple script to break the procrastination loop 🥊.
Use the script to set a countdown timer and Mac will turn screen off 💻 or quit all applications ⭕️ or shutdown completely ❌ after timer runs out regradless of what you are doing.
## Usage
After installation, type `lazy-mac` commands in terminal as follow:

`number-of-minutes` is an integer represents countdown timer in __minutes__
* Set countdown to turn screen off: `lazy-mac -sleep number-of-minutes`
* Set countdown to quit all application: `lazy-mac -quitall number-of-minutes`
* Set countdown to shutdown: `lazy-mac -shutdown number-of-minutes`
* To quit timing at any point, enter `q`
## Installation:
Copy __lazy-mac__ executable file to `usr/local/bin` , remove the file to uninstall
## Warning:
* `-quitall` and `-shutdown` closes all application. __Unsaved data maybe lost__. Hence use this script with caution and only when necessary
## Tested:
* MacOS Mojave
* 15'' MBP 2018
