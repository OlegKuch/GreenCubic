# GreenCubic

The simple game written on Python/pygame.

## Contacts

[Discord](https://discord.gg/SwWweGb)

[VK](https://vk.com/greencubic)

## Installing

Download GreenCubic_installer.exe from this repo or [here](https://oleg4260.itch.io/greencubic).

### Windows

Start installer and install.

If you want to update GreenCubic, no need to delete old version. Just start installer, it will not ask you for install path and update game.

### Other platforms

You can use Wine to run GreenCubic_installer.exe and install the game.

## Build from source

### Windows

If you have 32-bit or old (Windows XP and older) Windows, GreenCubic will not work, you need to build it from source.

1. Install [Python](python.org) if you haven't it. (32 bit, if you have 32 bit windows, and 3.4 if you have Windows XP or older), do not forget to add to path and install pip.

2. Install modules by command `pip3 install pygame pypresence pyinstaller`

3. You can just run file GreenCubic.py and play, but you can make .exe: Run file build_exe.bat and wait. In "greencubic" folder you'll have all needed files.

4 (optional). You can install [Inno Setup](https://www.jrsoftware.org/isinfo.php) and use file GreenCubic.iss to make installer.

### Linux and other platforms

I don't know the way to make binary from python file in other platforms, but I think no need to build it.

#### Ubuntu, Debian, Mint

1. Install Python by command `sudo apt-get install python3` if you haven't it.

2. Install modules by command `pip install pygame pypresence pyinstaller`

3. Run file GreenCubic.py and play.
