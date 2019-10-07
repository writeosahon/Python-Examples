""" file contains the callable which is executed by a process. 
File contains usage of pipe connections by a process (amongst other things) """

import time
import random
import multiprocessing
import logging

# SET THE LOGGING DETAILS WITHIN THIS PROCESS - BECAUSE THE APP IS MULTI-PROCESS
logging.basicConfig(filename="LOGS.log", filemode="a", level=logging.INFO, \
        format="%(levelname)s %(asctime)s || %(pathname)s >>> %(message)s")

# create the function that will be run as the process.
# function using pipe connections to communicate with the parent process
def run_method(pipe_connection: object, process_count: int):

    # check if process-count is an int or a tuple
    if process_count.__class__ == int:  # process_count is an int
        pass
    elif process_count.__class__ == tuple: # process_count is a tuple
        raise ValueError("wrong value provided")
    time.sleep(random.randint(1,4)) # cause the process to sleep/pause for random seconds (seconds < 5)
    logging.info("running process %s", str(process_count)) # write a simple log message
    pipe_connection.send("hello from process {}".format(process_count).title())
    return process_count