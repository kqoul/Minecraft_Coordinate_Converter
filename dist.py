import time

def distance():
    try:
        print("Enter the bigger coordinate: ")
        d1_input = input(">")
        d1_input_helper = int(d1_input)
        print("Enter the smaller coordinate: ")
        d2_input = input(">")
        d2_input_helper = int(d2_input)
        print ("calculating..")
        time.sleep(3)
        result = d1_input_helper - d2_input_helper
        print("the distance is:", result,"blocks")
        time.sleep(2)
        return
    except ValueError:
        print("Invalid Syntax")