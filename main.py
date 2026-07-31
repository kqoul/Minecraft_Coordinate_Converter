import nether_calc
import dist
import time
import banner

def welcome():
    while True:
            print("Welcome to Nether - Overworld calculator!")
            print("Made by kqoul in python!")
            main()

def main():
    while True:
        print(banner.banner)
        print("1- Overworld to Nether, 2- Nether to Overworld, 3- Distance calculator ")
        sel_menu = input(">")
        sel_menu_helper = int(sel_menu)
        if sel_menu_helper == int(1):
            nether_calc.overworld_to_nether()
        elif sel_menu_helper == int(2):
            nether_calc.nether_to_overworld()
        elif sel_menu_helper == int(3):
             dist.distance()
        else:
            print("Invalid Syntax!")
            exit()

welcome()