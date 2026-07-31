import time

def distance():
    try:
        print("Enter the bigger coordinate X: ")

        d1_input_x = input(">")
        d1_input_helper_x = int(d1_input_x)
        print("Enter the bigger coordinate Y: ")
        d1_input_y = input(">")
        d1_input_helper_y = int(d1_input_y)
        print("Enter the smaller coordinate X: ")
        d2_input_x = input(">")
        d2_input_helper_x = int(d2_input_x)
        print("Enter the smaller coordinate Y: ")
        d2_input_y = input(">")
        d2_input_helper_y = int(d2_input_y)
        print ("calculating..")
        time.sleep(3)
        result_x = d1_input_helper_x - d2_input_helper_x
        result_y = d1_input_helper_y - d2_input_helper_y
        print("the distance is:", result_x, "blocks in X and", result_y, "blocks in Y")
        time.sleep(2)
        return
    except ValueError:
        print("Invalid Syntax")