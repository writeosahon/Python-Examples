""" file contains simple examples on Python threading/Concurrency """

import sys
# USE THIS IMPORT OF THE THREADING MODULE BECAUSE IN VERSIONS OF PYTHON < 3.7 , THE 
# THREADING MODULE WAS OPTIONAL
try:
    import threading
except ImportError:
    import dummy_threading as threading    
import time
import os

# print out program heading (using multi-line statement)
programHeading = "PROGRAM BEGINS BELOW (Python Version {})".format(\
                sys.version[0:sys.\
                    version.index(" ")])
print(programHeading)
print('=' * len(programHeading))
programHeading = "PYTHON THREADING/CONCURRENCY"
print(programHeading)
print('=' * len(programHeading))
#==================================================================

#variable holds all the thread created
threads_list = [] 

# create the function that will be run as the thread
def run_method(thread_count: int): 
    print("running thread {}".format(thread_count))
    time.sleep(2) # cause the thread to sleep/pause for 2 seconds
    print(f"thread {thread_count} completed!")

# use a for loop to creating the thread objects
for(i) in range(1,4):
    # create the thread obhjects
    threads_list.append(threading.Thread(target=run_method, args=(i,)))
    # start the last created thread
    threads_list[i-1].start()

# list all threads that are alive
print("All Threads :", threading.enumerate())

# use a for loop to wait for all thread objects to complete execution
for thread in threads_list:
    thread.join() # wait for thread to complete execution

print("ALL THREADS COMPLETED!!")