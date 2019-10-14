""" file contains examples on Python Python Tk GUI Programming.
 """

__version__ = '0.1 (2019-10-14)'
__author__ = 'UTOPIA SOFTWARE'

import sys
import multiprocessing
import logging
import os
import platform
import tkinter
import tkinter.ttk


# main function for running this program. 
def main():
    """ main function for the program. """

    # provide greetings for the program
    # print out program heading (using multi-line statement)
    programHeading = "PROGRAM BEGINS BELOW (Python Version {})".format(\
                    sys.version[0:sys.\
                        version.index(" ")])
    print(programHeading)
    print('=' * len(programHeading))
    programHeading = "PYTHON SIMPLE Tk GUI PROGRAMMING"
    print(programHeading)
    print('=' * len(programHeading))
    # end of greetings
    
    # create a main/parent window
    root = tkinter.Tk()
    root.title("Simple GUI") # parent window title
    root.geometry("300x400+250+250") #set the intial widthxheight and position from +left and  from +top
    
    label = tkinter.ttk.Label(root, text="Hello World")
    label.pack()
    
    button = tkinter.ttk.Button(root, text="Click Me")
    button.pack()
    
    entry = tkinter.ttk.Entry(root, text="Enter Field")
    entry.pack()

    root.mainloop()
    
# end of main() function        


# CHECK IF THE MODULE IS BEING EXECUTED AS THE MAIN SCRIPT BY THE INTERPRETER
# THIS SECTION IS VERY IMPORTANT
if __name__ == "__main__":

    # SET THE LOGGING DETAILS FOR THE APP (WITHIN THIS PROCESS - BECAUSE THE APP IS MULTI-PROCESS)
    logging.basicConfig(filename="LOGS.log", filemode="a", level=logging.INFO, \
        format="%(levelname)s %(asctime)s || %(pathname)s >>> %(message)s")
    
    # freeze the executable code (affects windows only)
    multiprocessing.freeze_support()

    # check the type for os the code is running on so 
    # we can set the default process type
    osname = platform.platform(aliased=True, terse=True).lower() # get the os name
    
    # check the os name
    if "window" in osname: # windows os
        multiprocessing.set_start_method("spawn")
    elif "linux" in osname: # linux distribution system
        multiprocessing.set_start_method("fork")
    elif "mac" in osname: # linux distribution system
        multiprocessing.set_start_method("fork")
    else:
        multiprocessing.set_start_method("fork")
    # END OF PYTHON PROGRAM BASIC SETUP

    # call the main() function
    main()