# Game-Info-Scraper
Python application for reading the file header of different types of game files and extracting various pieces of information.

# Usage
Using the command line, navigate to the location of main.py. Run 'python main.py "yourgamehere" - obviously replacing the appropriate field with the name of the file you want info scraped from. Make sure to include the quotation marks and the file extension.

# Supported file types
Game Boy and Game Boy Color (.gb)
Game Boy Advance (.gba)
Sega Genesis (.md)

# Notes
- Interestingly enough, Sega Genesis ROMs use the .md file type. Because of this, my program will accept ANY .md file, but will error out if it's not a valid Genesis ROM.
- Also interesting is that Game Boy and Game Boy Color seem to have the same file header.
- A great source for games (obviously for educational purposes, and NOT for playing...) is Vimm's Lair - https://vimm.net/?p=vault

# Future plans
- Add an actual UI (so usage doesn't have to be done through the command line)
- Support for further file types

# Information sources
- Game Boy and Game Boy Color
~ https://gbdev.gg8.se/wiki/articles/The_Cartridge_Header
~ https://raw.githubusercontent.com/gb-archive/salvage/master/txt-files/gbrom.txt

- Game Boy Advance
~ http://members.iinet.net.au/~freeaxs/gbacomp/#GBA%20Header
~ https://problemkaputt.de/gbatek.htm#gbamemorymap

- Sega Genesis
~ https://plutiedev.com/rom-header
