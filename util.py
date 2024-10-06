import os

def pause():
    input("Press the <ENTER> key to continue...")

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')