import sys, gameboy, gameboyadv, genesis
validTypes = ['gb', 'gbc', 'gba', 'md']


def typeWrapper(file, type):
    typeSwitcher = {
        'gb': gameboy.gbBreakdown,
        'gbc': gameboy.gbBreakdown,
        'gba': gameboyadv.gbaBreakdown,
        'md': genesis.genBreakdown,
    }

    typeSwitcher.get(type)(file)


if len(sys.argv) <= 1:
    print("Please submit a valid game file to scrape info from\nError code 001: No file submitted")
    quit()

if len(sys.argv) > 2:
    print("Please use only one valid game file as your input\nAlternatively, make sure your submitted file is surrounded by quotation marks\nError code 003: Multiple inputs")
    quit()

with open(sys.argv[1], "rb") as file:

    typeCheck = sys.argv[1].split(".")
    if (typeCheck[-1]) not in validTypes:
        print("Please use a valid game file as your input\nError code 002: Invalid file type\nValid file types: " + str(validTypes) + "\nSubmitted file type: " + typeCheck[-1])
        quit()

    typeWrapper(file, typeCheck[-1])
