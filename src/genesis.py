# Genesis games like to have a lot of random whitespace in their names, so this is used for filtering out said whitespace
def titleFilter(var):
    if var != '':
        return True
    else:
        return False


def genBreakdown(file):

    systemTypes = {
        "SEGA MEGA DRIVE": "Sega Mega Drive",
        "SEGA GENESIS": "Sega Mega Drive",
        "SEGA 32X": "Sega Mega Drive + 32X",
        "SEGA EVERDRIVE": "Sega Mega Drive (Everdrive extensions)",
        "SEGA SSF": "Sega Mega Drive (Mega Everdrive extensions)",
        "SEGA MEGAWIFI": "Sega Mega (Mega Wifi extensions)",
        "SEGA PICO": "Sega Pico",
        "SEGA TERA68K": "Sega Tera Drive (boot from 68000 side",
        "SEGA TERA286": "Sega Tera (boot from x86 side)"
    }

    softwareTypes = {
        "GM": "Game", "AI": "Aid", "OS": "Boot ROM (TMSS)", "BR": "Boot ROM (Sega CD)"
    }

    supportedDevices = {
        "J": "3-button controller", "6": "6-button controller", "0": "Master System controller", "A": "Analog joystick", "4": "Multitap", "G": "Lightgun", "L": "Activator",
        "M": "Mouse", "B": "Trackball", "T": "Tablet", "V": "Paddle", "K": "Keyboard or keypad", "R": "RS-232", "P": "Printer", "C": "CD-ROM (Sega CD)", "F": "Flopper drive", "D": "Download"
    }

    supportedRegions = {
        "0": "None", "1": "Japan", "2": "Invalid", "3": "Japan", "4": "Americas", "5": "Japan/Americas", "6": "Americas", "7": "Japan/Americas",
        "8": "Europe", "9": "Japan/Europe", "A": "Europe", "B": "Japan/Europe", "C": "Americas/Europe", "D": "Japan/Americas/Europe", "E": "Americas/Europe",
        "F": "Japan/Americas/Europe", "J": "Japan", "U": "Americas"
    }

    # System type
    file.seek(256)
    sysType = file.read(16).decode().strip()

    # Release information
    releaseDate = file.read(16).decode()

    # Game title. Genesis games like to pad their game titles with a lot of whitespace, so use a filtering function and
    # a subsequence for loop to remove it all
    file.seek(48, 1)
    title = file.read(48).decode().split(" ")
    filtered = filter(titleFilter, title)
    title = ""
    for x in filtered:
        title = title + x + ' '

    # Serial information
    serial = file.read(14).decode().strip()

    # Device support
    file.seek(2, 1)
    deviceSupport = file.read(16).decode().strip()

    # Localization information
    file.seek(80, 1)
    regionSupport = file.read(3).decode().strip()

    # Reporting
    print("Game Type: Sega Genesis")
    print("System Type: " + systemTypes.get(sysType, "Unexpected system type"))
    print("Copyright and Release Date: " + releaseDate)
    print("Title: " + title.rstrip())
    print("Serial Info: " + serial + " (" + serial[:2] + " = " + softwareTypes.get(serial[:2], "Unexpected software type") + ")")

    deviceSupportBreakdown = ""
    for x in deviceSupport:
        deviceSupportBreakdown = deviceSupportBreakdown + supportedDevices.get(x, "Unexpected device type") + ", "

    print("Supported devices: " + deviceSupportBreakdown[:-2])
    print("Supported regions: " + supportedRegions.get(regionSupport, "Unexpected region support"))
