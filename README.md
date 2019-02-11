# lazy-mac
A simple script to break the procrastination loop 🥊.
Use the script to set a countdown timer and Mac will turn screen off 💻 or quit all applications ⭕️ or shutdown completely ❌ after time runs out regardless of what you are doing.
## Usage
After installation, type `lazy-mac` commands in terminal as follow:

`number-of-minutes` is an integer represents countdown timer in __minutes__
* Set countdown to turn screen off: `lazy-mac -sleep number-of-minutes`
* Set countdown to quit all applications: `lazy-mac -quitall number-of-minutes`
* Set countdown to shutdown: `lazy-mac -shutdown number-of-minutes`
* To quit timing at any point, enter `q`
* To view list of arguments: `lazy-mac -help`

## Installation:
Copy __lazy-mac__ executable file to `usr/local/bin` , remove the file to uninstall
## Warning:
* `-quitall` and `-shutdown` closes all applications. __Unsaved data maybe lost__. Hence use this script with caution and only when necessary
* This is a CLI script which requires Terminal to be running during the countdown. Turning off Terminal effectively terminates the script
## Tested:
* MacOS Mojave
* 15'' MBP 2018
