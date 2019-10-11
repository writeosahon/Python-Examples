""" file contains examples on Python Event-Driven/Async programming.

USE ASYNCIO IN PYTHON 3.5+
 """

__version__ = '0.1 (2019-10-11)'
__author__ = 'UTOPIA SOFTWARE'

import sys
import multiprocessing
import logging
import asyncio
import time
import os
import platform
import concurrent.futures
import itertools

from myprocessespackage import simpleprocess


# main function for running this program. This function will be run asynchronously in the event loop
async def main(process_pool: concurrent.futures.Executor):
    """ main function for the program. It is run asynchronously """

    # provide greetings for the program
    # print out program heading (using multi-line statement)
    programHeading = "PROGRAM BEGINS BELOW (Python Version {})".format(\
                    sys.version[0:sys.\
                        version.index(" ")])
    print(programHeading)
    print('=' * len(programHeading))
    programHeading = "PYTHON SIMPLE ASYNC/EVENT-DRIVEN PROGRAMMING"
    print(programHeading)
    print('=' * len(programHeading))
    # end of greetings
    
    # execute a simple process which returns the inputed number
    for number in itertools.count(1): # this loop countinues forever and returns increaments
        # get the current event loop and execute the task in a different process
        result = await asyncio.get_event_loop().\
            run_in_executor(process_pool, simpleprocess.run_method, number) # wait for process result
        print(f"This is the result {result}")
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

    #PROGRAM LOGIC BEGINS BELOW 
    # create an event loop for this thread
    asyncio.set_event_loop(asyncio.new_event_loop()) # NOTE: this code is technically not needed 
    event_loop = asyncio.get_event_loop() # get the event loop for this thread

    # create a process pool executor to help execute processes
    process_pool_executor = concurrent.futures.ProcessPoolExecutor(os.cpu_count())

    # submit the main function as a coroutine/task to the event loop
    event_loop.create_task(main(process_pool_executor))

    #run the event loop forever
    event_loop.run_forever()