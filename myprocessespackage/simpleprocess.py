""" file contains the callable which is executed by a process """

import time

# create the function that will be run as the process
def run_method(process_count: object):
    # check if process-count is an int or a tuple
    if process_count.__class__ == int:  # process_count is an int
        print("running process {}".format(process_count))
    elif process_count.__class__ == tuple: # process_count is a tuple
        print("running process {}".format(process_count[1]))
    time.sleep(2) # cause the process to sleep/pause for 2 seconds
    print(f"process {process_count} completed!")
    return process_count