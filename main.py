import nether_calc
import dist
import time
import banner
import shutdown
import data

def welcome():
    while True:
            print("Welcome to Nether - Overworld calculator!")
            print("Made by kqoul in python!")
            print("Version:",data.version)
            main()

def main():
    while True:
        print(banner.banner)
        print(banner.selection_menu_banner)
        sel_menu = input(">")
        sel_menu_helper = int(sel_menu)
        if sel_menu_helper == int(1):
            nether_calc.overworld_to_nether()
        elif sel_menu_helper == int(2):
            nether_calc.nether_to_overworld()
        elif sel_menu_helper == int(3):
             dist.distance()
        elif sel_menu_helper == int(4):
             shutdown.shutdown_func()
        else:
            print("Invalid Syntax!")
            time.sleep(1)
            exit()

welcome()