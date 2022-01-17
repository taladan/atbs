#!/usr/bin/python3
# a utility to clear the terminal screen
from os import system, name

def clear():
    # Windows
    if name == 'nt':
        _ = system('cls')
    # Mac/*Nix
    else:
        _ = system('clear')