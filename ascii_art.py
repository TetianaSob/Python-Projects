# ascii_art.py

import colorsys
from termcolor import colored


def print_art(msg, color):
    valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")
    if color not in valid_colors:
        color = "magenta"
    ascii_art = colorsys(msg)
    colored_ascii = colored(ascii_art, colors = color)
    print(colored_ascii)

msg = input("What would you like to print? ")
color = input("What color? ")
print(colored_ascii)

#What would you like to print? red
#What color? red

