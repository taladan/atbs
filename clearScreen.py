#!/usr/bin/python3
# a utility to clear the terminal screen

def clear():
    # Windows
    if name == 'nt':
        _ = system('cls')
    # Mac/*Nix
    else:
        _ = system('clear')