import sys
import os
import copy # module to help with shallow and deep copying of python objects

import numpy # testing installing/importing of 3rd party/custom modules


# print out program heading (using multi-line statement)
programHeading = "PROGRAM BEGINS BELOW (Python Version {})".format(\
                sys.version[0:sys.\
                    version.index(" ")])
print(programHeading)
print('=' * len(programHeading))
programHeading = "PYTHON MODULES"
print(programHeading)
print('=' * len(programHeading))

# print system's module path
for path in sys.path: # loop through all the moduule search paths
    print("module path: {}".format(path))

# get the current working directory (CWD) for this app
print("Application Current Working Directory {directory}".\
    format(directory=os.getcwd())) # used keyword parameter

# ask the user if they want to change their CWD
changeCWD = input("""Do you want to change the app working directory?
Enter 'Y' or 'N' for yes or no \u27A4   """)
# check if user wants to change the CWD
if changeCWD == 'Y' : # user wants to change
    # change the current working directory
    os.chdir('c:\\Users')
    print("Working Directory Changed")
elif changeCWD == 'N' :
    print("Working Directory NOT Changed") # CWD not changed
else : 
    print("Wrong Input Value")

# get the new working directory
print("New Working Directory {directory}".format(directory=os.getcwd()))

# list the directories and files that exists in whatever CWD the user has choosen
print("Working Directory Contents (Files & Folders) ", os.listdir())

# ask the user if they want to make a new directory in the selected CWD
createDir = input("""Do you want to create a new directory in the current working directory?
Enter 'Y' or 'N' for yes or no \u27A4   """)
# check if user wants to create the new directory
if createDir == 'Y' : # user wants to create new directory
    # make the new directory frrom the user input
    try :
        os.mkdir(input("""Enter the new directory name \u27A4   """))
        print("New Directory Created")
    except :
        print("An error prevented directory from being created. maybe directory already exists")   
elif createDir == 'N' :
    print("New Directory NOT Created") # new directory not created
else : 
    print("Wrong Input Value")