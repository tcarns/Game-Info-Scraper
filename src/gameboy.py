def gbBreakdown(file):

    gbLicenseeCodes = {
        '00': 'None', '01': 'Nintendo R&D1', '08': 'Capcom', '13': 'Electronic Arts', '18': 'Hudson Soft', '19': 'b-ai', '20': 'kss', '22': 'pow', '24': 'PCM Complete', '25': 'san-x',
        '28': 'Kemco Japan', '29': 'seta', '30': 'Viacom', '31': 'Nintendo', '32': 'Bandai', '33': 'Ocean/Acclaim', '34': 'Konami', '35': 'Hector', '37': 'Taito', '38': 'Hudson',
        '39': 'Banpresto', '41': 'Ubisoft', '42': 'Atlus', '44': 'Malibu', '46': 'angel', '47': 'Bullet-Proof', '49': 'irem', '50': 'Absolute', '51': 'Acclaim', '52': 'Activision',
        '53': 'American sammy', '54': 'Konami', '55': 'Hi tech entertainment', '56': 'LJN', '57': 'Matchbox', '58': 'Mattel', '59': 'Milton Bradley', '60': 'Titus', '61': 'Virgin',
        '64': 'LucasArts', '67': 'Ocean', '69': 'Electronic Arts', '70': 'Infogrames', '71': 'Interplay', '72': 'Broderbund', '73': 'sculptured', '75': 'sci', '78': 'THQ',
        '79': 'Accolade', '80': 'misawa', '83': 'lozc', '86': 'Tokuma Shoten Intermedia', '87': 'Tsukuda Original', '91': 'Chunsoft', '92': 'Video system', '93': 'Ocean/Acclaim',
        '95': 'Varie', '96': 'Yonezawa/s\'pal', '97': 'Kaneko', '99': 'Pack-In-Video', 'A4': 'Konami (Yu-Gi-Oh!)'
    }

    gbOldLicenseeCodes = {
        '00': 'None', '01': 'Nintendo', '08': 'Capcom', '09': 'Hot B', '0A': 'Jaleco', '0B': 'Coconuts Japan', '0C': 'Elite Systems', '13': 'Electronic Arts', '18': 'Hudson Soft',
        '19': 'ITC Entertainment', '1A': 'Yanoman Corporation', '1D': 'Japan Clary Business', '1F': 'Virgin Interactive', '24': 'PCM Complete', '25': 'San-X', '28': 'Kotobuki System',
        '29': 'SETA Corporation', '30': 'Infogrames', '31': 'Nintendo', '32': 'Bandai', '34': 'Konami', '35': 'Hector', '38': 'Capcom', '39': 'Banpresto Co., Ltd.',
        '3C': 'Entertainment Int', '3E': 'Gremlin Graphics', '41': 'Ubisoft', '42': 'Atlus', '44': 'Malibu', '46': 'Angel (Bandai)', '47': 'Spectrum Holobyte', '49': 'Irem',
        '4A': 'Virgin', '4D': 'Malibu', '4F': 'U.S. Gold', '51': 'Acclaim', '52': 'Activision', '53': 'American Sammy', '54': 'GameTek', '55': 'Park Place Productions',
        '56': 'LJN', '57': 'Matchbox', '59': 'Milton Bradley', '5A': 'Mindscape', '5B': 'Romstar', '5C': 'Naxat Soft', '5D': 'Tradewest', '60': 'Titus Software', '61': 'Virgin',
        '67': 'Ocean of America, Inc.', '69': 'Electronic Arts', '6E': 'Elite Systems Ltd.', '6F': 'Electro Brain', '70': 'Infogrames', '71': 'Interplay', '72': 'Broderbund',
        '73': 'Sculptered Soft', '75': 'The Sales Curve', '78': 'THQ', '79': 'Accolade', '7A': 'Triffix Entertainment', '7C': 'MicroProse', '7F': 'Kemco',
        '80': 'Misawa Entertainment', '83': 'LOZC G. Amusements', '86': 'Tokuma Shoten', '8B': 'Bullet-Proof Software', '8C': 'Vic Tokai', '8E': 'Ape', '8F': 'I\'Max',
        '91': 'Spike Chunsoft', '92': 'Video System', '93': 'Tsuburava', '95': 'Varie', '96': 'Yonezawa / S\'Pal', '97': 'Kaneko', '99': 'Arc System Works', '9A': 'Nihon Bussan',
        '9B': 'Tecmo', '9C': 'Imagineer', '9D': 'Banpresto', '9F': 'Nova', 'A1': 'Hori Electric', 'A2': 'Bandai', 'A4': 'Konami', 'A6': 'Kawada', 'A7': 'Takara',
        'A9': 'Technōs Japan', 'AA': 'Broderbund', 'AC': 'Toei Animation', 'AD': 'Toho', 'AF': 'Namco', 'B0': 'Acclaim', 'B1': 'ASCII or Nexoft', 'B2': 'Bandai', 'B4': 'Enix Corporation',
        'B6': 'HAL Labs', 'B7': 'SNK', 'B9': 'Pony Canyon', 'BA': 'Culture Brain', 'BB': 'SunSoft', 'BD': 'Sony Imagesoft', 'BF': 'Sammy', 'C0': 'Taito', 'C2': 'Kemco',
        'C3': 'SquareSoft', 'C4': 'Tokuma Shoten', 'C5': 'Data East', 'C6': 'Tonkin House', 'C8': 'Koei', 'C9': 'UFL', 'CA': 'Ultra', 'CB': 'Vap', 'CC': 'Use', 'CD': 'Meldac',
        'CE': 'Pony Canyon', 'CF': 'Angel (Bandai)', 'D0': 'Taito Corporation', 'D1': 'Sofel', 'D2': 'Quest', 'D3': 'Sigma Ent. Inc.', 'D4': 'Kodansha', 'D6': 'Naxat Soft',
        'D7': 'Copya Systems', 'D9': 'Banpresto', 'DA': 'Tomy Corporation', 'DB': 'LJN', 'DD': 'NCS', 'DE': 'Human', 'DF': 'Altron', 'E0': 'Jaleco Entertainment', 'E1': 'Towa Chiki',
        'E2': 'Uutaka', 'E3': 'Varie', 'E5': 'Epoch', 'E7': 'Athena', 'E8': 'Asmik', 'E9': 'Natsume', 'EA': 'King Records', 'EB': 'Atlus', 'EC': 'Epic/Sony Records', 'EE': 'IGS',
        'F0': 'A Wave', 'F3': 'Extreme Entertainment Group', 'FF': 'LJN'
    }

    gbROMSize = {
        b'\x00': '32 kilobytes', b'\x01': '64 kilobytes', b'\x02': '128 kilobytes', b'\x03': '256 kilobytes', b'\x04': '512 kilobytes', b'\x05': '1 megabyte', b'\x06': '2 megabytes',
        b'\x07': '4 megabytes', b'\x08': '8 megabytes', b'\x52': '1.1 megabytes', b'\x53': '1.2 megabytes', b'\x54': '1.5 megabytes'
    }

    gbRAMSize = {
        b'\x00': 'None', b'\x01': '2 kilobytes', b'\x02': '8 kilobytes', b'\x03': '32 kilobytes', b'\x04': '128 kilobytes', b'\x05': '64 kilobytes'
    }

    gbDestinationCode = {
        b'\x00': 'Japanese', b'\x01': 'Non-Japanese'
    }

    file.seek(308)
    title = file.read(15).decode()

    file.seek(1, 1)
    licenseeCode = file.read(2)
    if licenseeCode == b'\x00\x00':
        licenseeCode = '00'
    else:
        licenseeCode = licenseeCode.decode()

    file.seek(2, 1)
    ROMSize = file.read(1)

    RAMSize = file.read(1)

    destination = file.read(1)

    oldCode = False
    oldLicenseeCodeCheck = file.read(1).hex()
    if oldLicenseeCodeCheck != '33':
        oldCode = True
        licenseeCode = oldLicenseeCodeCheck

    print("Game Type: Game Boy OR Game Boy Color")
    print("Game Title: " + title)

    if oldCode:
        print("Licensee: " + gbOldLicenseeCodes.get(licenseeCode, "Unexpected licensee code"))
    else:
        print("Licensee: " + gbLicenseeCodes.get(licenseeCode, "Unexpected licensee code"))

    print("ROM Size: " + gbROMSize.get(ROMSize, "Unexpected ROM size"))
    print("RAM Size: " + gbRAMSize.get(RAMSize, "Unexpected RAM size"))
    print("Destination: " + gbDestinationCode.get(destination, "Unexpected destination code"))
