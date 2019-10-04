""" file contains the callable which is executed by a process """

import time

# create the function that will be run as the process
def run_method(process_count: int): 
    print("running process {}".format(process_count))
    time.sleep(2) # cause the process to sleep/pause for 2 seconds
    print(f"process {process_count} completed!")