""" file contains examples on Python MultiProcessing Pool """

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
    programHeading = "PYTHON MULTIPROCESSING POOL"
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

    # create the process pool
    multiprocess_pool = multiprocess.Pool(processes=os.cpu_count() * 2, maxtasksperchild=2)
    # use a for loop to creating the process objects. Number of processes == number of cpus
    for(i) in range(1, os.cpu_count() + 1):
        # create the tasks for the process objects in the pool
        multiprocess_pool.apply_async(func=simpleprocess.run_method, args=(i,), \
            callback=lambda x: print(f"Result {x}"), error_callback=lambda x: print(f"Error {x}"))
    
    # create a collection of tasks (all at once) for the process objects in the pool
    multiprocess_pool.map_async(func=simpleprocess.run_method, iterable=enumerate(range(1, 4)),\
            callback=lambda x: print(f"Result {x}"), error_callback=lambda x: print(f"Error {x}"))    
    
    # create a collection of tasks (all at once using imap) for the process objects in the pool
    imap_result = multiprocess_pool.imap(func=simpleprocess.run_method, \
        iterable=enumerate(range(1, 4)), chunksize=3)    
    
    for answer in imap_result:
        print("process imap result {}".format(answer))

    # close the multiprocessing pool    
    multiprocess_pool.close()
    # wait for all process to exit
    multiprocess_pool.join()

