# Fortnite Stretch Configurator
This is a tool designed to make runnning Fortnite in stretched resolution simple and easily reversible without dealing with manually editing ini files and the like.

You may still need to set your monitor resolution with NVIDIA Control Panel/AMD for the mouse to work properly, but through making this tool I have discovered that the resolution used by 72hrs (1154 x 1080) and other proportional resolutions do not require the monitor resolution to be set as well. This may also apply to other resolutions.

# **Usage**
- Download or clone the latest version of this repository and open run.bat
- This uses a venv environment to eliminate the need to install Python and other dependencies on your machine.
- The default config path is loaded by default
- Included shortcut removes the need to locate the game executable

Settings file is automatically backed up when launching the game. Reset Game Settings button restores this backup to make reverting your resolution simple and hassle free.

**NOTE:** You must choose to use FortniteClient-Win64-Shipping.exe for the executable. There are issues with BattleEye when running FortniteLauncher.exe. This will be addressed by switching to the Epic launcher's generated shortcut in a coming update

This is Windows only and I do NOT have a Mac to address differences. If someone wants to update this with Mac support they are free to do as they please.

# TODO
1. Clean UI
2. List of preset resolutions
3. Profit...
