""" file contains examples on Python Event-Driven/Async programming.

We use async generators in running event driven code

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
import random


# define an aync generatore function
async def getrandom_number() :
    """ function is used to generate random int asynchronously """

    # run an infinite loop to continue generating random numbers
    while True: 
        await asyncio.sleep(2) # let this task sleep for a while
        yield random.randint(0, sys.maxsize) # yield a random int


# main function for running this program. This function will be run asynchronously in the event loop
async def main():
    """ main function for the program. It is run asynchronously """

    # provide greetings for the program
    # print out program heading (using multi-line statement)
    programHeading = "PROGRAM BEGINS BELOW (Python Version {})".format(\
                    sys.version[0:sys.\
                        version.index(" ")])
    print(programHeading)
    print('=' * len(programHeading))
    programHeading = "PYTHON ASYNC GENERATOR EVENT-DRIVEN PROGRAMMING"
    print(programHeading)
    print('=' * len(programHeading))
    # end of greetings
    
    # use an async for-loop to get the generated random int
    async for number in getrandom_number():
        # print out the returned number
        print("Random Number: {}".format(number))

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

    # submit the main function as a coroutine/task to the event loop
    event_loop.create_task(main())

    try: # place this code in a try block to handle any exceptions

        #run the event loop forever
        event_loop.run_forever()
    except KeyboardInterrupt as keyboard_interrupt:
        print("Program Termination Requested")
    
    # CLEANUP PROCEDURES BEGIN BELOW
    # check if the asyncio.all_tasks() method is supported. method present in Python 3.7+
    if asyncio.all_tasks is not None: 
        pending_tasks = asyncio.all_tasks(loop=event_loop) # get all pending tasks
    else:
        pending_tasks = asyncio.Task.all_tasks() # get all pending tasks
    
    # cancel all pending tasks
    for task in pending_tasks:
        task.cancel()
    
    # run all the pending tasks once more, so they can cancel
    cleanup_task = asyncio.gather(*pending_tasks, return_exceptions=True)
    # run and wait for the cleanup task to complete
    event_loop.run_until_complete(cleanup_task)
    # check if the event_loop is srill running
    if event_loop.is_running():
        event_loop.stop() # stop it
    # close the run finally
    event_loop.close()
print("PROGRAM SUCESSFULLY TERMINATED\U0001F44D")