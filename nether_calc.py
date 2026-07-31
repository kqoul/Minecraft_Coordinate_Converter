import math
import time

def overworld_to_nether():
    try:
        print("Enter the overworld X coordinates: ")
        overworld_input_x = input(">")
        overworld_input_helper_x = int(overworld_input_x)
        print("Enter the overworld Y coordinates: ")
        overworld_input_y = input(">")
        overworld_input_helper_y = int(overworld_input_y)
        print("Calculating..")
        time.sleep(3)
        result_x = overworld_input_helper_x/8
        result_y = overworld_input_helper_y/8
        print("X result is",result_x)
        print("Y result is",result_y)
    except ValueError:
        print("Invalid Syntax!")


def nether_to_overworld():
     try:
           print("Enter the nether X coordinates: ")
           nether_input_x = input("> ")
           nether_input_helper_x = int(nether_input_x)
           print("Enter the nether Y coordinates: ")
           nether_input_y = input("> ")
           nether_input_helper_y = int(nether_input_y)
           print("Calculating..")
           time.sleep(3)
           result_x = nether_input_helper_x*8
           result_y = nether_input_helper_y*8
           print("X result is",result_x)
           print("Y result is",result_y)
     except ValueError:
           print("Invalid Syntax!")