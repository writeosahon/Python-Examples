""" file contains simple examples on Python Parallelism/MultiProcessing """

import sys
import multiprocessing
import time
import os
import platform
from myprocessespackage import simpleprocess

#==================================================================

#variable holds all the processes created
process_list = [] 

# CHECK IF THE MODULE IS BEING EXECUTED AS THE MAIN SCRIPT BY THE INTERPRETER
# THIS SECTION IS VERY IMPORTANT FOR MULTIPROCESSING CODE
if __name__ == "__main__":

    # print out program heading (using multi-line statement)
    programHeading = "PROGRAM BEGINS BELOW (Python Version {})".format(\
                    sys.version[0:sys.\
                        version.index(" ")])
    print(programHeading)
    print('=' * len(programHeading))
    programHeading = "PYTHON PARALLELISM/MULTIPROCESS"
    print(programHeading)
    print('=' * len(programHeading))
    
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
    
    # get the multiprocessing contet to be used in creating the set of process
    multiprocess = multiprocessing.get_context()


    # use a for loop to creating the process objects
    for(i) in range(1,4):
        # create the process objects
        process_list.append(multiprocess.Process(target=simpleprocess.run_method, \
                                                 name=f"MyProcess {i}" , args=(i,)))
        # start the last created thread
        process_list[i-1].start()

    # list all processes that are alive
    print("All Processes :", multiprocess.active_children())

    # use a for loop to wait for all process objects to complete execution
    for process in process_list:
        process.join() # wait for process to complete execution

    print("ALL PROCESSES COMPLETED!!")
