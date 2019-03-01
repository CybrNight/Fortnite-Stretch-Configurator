# Fortnite Stretch Configurator
This is a tool designed to make runnning Fortnite in stretched resolution simple and easily reversible without dealing with manually editing ini files and the like.

You may still need to set your monitor resolution with NVIDIA Control Panel/AMD for the mouse to work properly, but through making this tool I have discovered that the resolution used by 72hrs (1154 x 1080) and other proportional resolutions do not require the monitor resolution to be set as well. This may also apply to other resolutions.

# **Usage**
- Download or clone the latest version of this repository and open run.bat
- This uses a venv environment to eliminate the need to install Python and other dependencies on your machine.

1. Locate the path to the game executable
2. Locate the path to GameUserSettings.ini (C:\Users\(user)\AppData\Local\FortniteGame\Saved\Config\WindowsClient\GameUserSettings.ini)
3. Enter resolution and press Launch & Apply

**NOTE:** You must choose to use FortniteClient-Win64-Shipping.exe for the executable. There are issues with BattleEye when running FortniteLauncher.exe

This is Windows only and I do have a mac to address differences if any. If someone wants to update this with Mac support they are free to do as they please.

# TODO
1. Update program to grab both the config and executable from registry or something
2. Clean UI
3. Possibly build Windows executable wiith py2app or similar library
4. Profit...
