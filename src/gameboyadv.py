def gbaBreakdown(file):

    gameCodeBreakdownFirst = {
        'A': 'Normal game; Older titles (mainly 2001..2003)',
        'B': 'Normal game; Newer titles (2003..)',
        'C': 'Normal game; Not used yet, but might be used for even newer titles',
        'F': 'Famicom/Classic NES Series (software emulated NES games)',
        'K': 'Yoshi and Koro Koro Puzzle (acceleration sensor)',
        'P': 'e-Reader (dot-code scanner)',
        'R': 'Warioware Twisted (cartridge with rumble and z-axis gyro sensor)',
        'U': 'Boktai 1 and 2 (cartridge with RTC and solar sensor)',
        'V': 'Drill Dozer (cartridge with rumble)'
    }

    gameCodeBreakdownLast = {
        'J': 'Japan', 'P': 'Europe/Elsewhere', 'F': 'French', 'S': 'Spanish', 'E': 'USA/English', 'D': 'German', 'I': 'Italian'
    }

    file.seek(160)
    title = file.read(12).decode()
    gameCode = file.read(4).decode()
    makerCode = file.read(2).decode()

    print("Game Type: Game Boy Advance")
    print("Game Title: " + title)

    print("\nGame Code: " + gameCode + "\nBreakdown\n---------")
    print(gameCode[0] + ': ' + gameCodeBreakdownFirst.get(gameCode[0], 'Unexpected game code element'))
    print(gameCode[
          1:3] + ': Usually an abbreviation of the game title (eg. "PM" for "Pac Man") (unless that game code was already used for another game, then TT is just random))')
    print(gameCode[3] + ': ' + gameCodeBreakdownLast.get(gameCode[3], 'Unexpected destination/language element'))

    print("\nMaker Code: " + makerCode + "\nIdentifies the (commercial) developer. For example, \"01\" = Nintendo.\nDeveloper note: Need a list of decoded maker codes " +
          "(i.e. maker codes mapping to actual developers, other than Nintendo) Hard to find. (Although, seeing all those codes for Game Boy/Game Boy Color, maybe I don't want to do that...")
