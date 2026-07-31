import time

def shutdown_func():
    print ("Are you sure you wish to exit the program?")
    print("y/n")
    sel_exit = input(">")
    if sel_exit == ("y"):
        print("Shutting down the program...")
        time.sleep(2)
        exit()
    elif sel_exit == ("n"):
        print("Shutdown Aborted By User!")
        time.sleep(1)
        return
    else:
        print("Invalid Syntax!")
        time.sleep(1)
        return