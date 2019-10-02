""" file contains ThreadPoolExecutor accessing a shared resource in a thread-safe manner.
threadPoolExecutor create thread in pools waiting for tasks to be given to them for execution
"""

__version__ = '0.1 (2019-10-02)'
__author__ = 'UTOPIA SOFTWARE'


import sys
# USE THIS IMPORT OF THE THREADING MODULE BECAUSE IN VERSIONS OF PYTHON < 3.7 , THE 
# THREADING MODULE WAS OPTIONAL
try:
    import threading
except ImportError:
    import dummy_threading as threading    
import time
import concurrent.futures # holds the THreadOolExecutor class
import os
from mythreadspackage import threading_with_condition_lock

# define GetNumber class
class GetNumber():
    """ class contains static method used to get a number from the IntNumberProvider class.
    """

    def __init__(self):
        """ constructor method for the  class """
        pass
    # end of method
    
    # static method where the threadpool executor worker should execute
    @staticmethod
    def getnumber(numberprovider): 
        while True: # create an infinite loop
            # lock/synchronise access to the IntNumberProvider class using its provider 'lock'
            with numberprovider._classlock: 
                
                # wait for a number to be available  
                numberprovider._classlock.\
                    wait_for(numberprovider.is_number_available)
                # once a number is available continue the thread and get the number
                print("Number Gotten From Within {}: {}".\
                    format(threading.current_thread().name, numberprovider.getnumber()))
            # let thread sleep for 3 seconds before continuing the loop        
            time.sleep(3)
    # end of method
# end of class

# define PutNumber class
class PutNumber(threading.Thread):
    """ class contains static method used to instruct the IntNumberProvider class to  
    make/provision a number for use.
    """

    def __init__(self):
        """ constructor method for the  class """
        pass
    # end of method
    
    # static method where the threadpool executor worker should execute
    @staticmethod
    def putnumber(numberprovider):
        while True: # create an infinite loop
            # lock/synchronise access to the IntNumberProvider class using its provider 'lock'
            with numberprovider._classlock:
                
                # while there is a number available from the IntNumberProvider, 
                # the thread should keep waiting 
                while numberprovider.is_number_available(): 
                    numberprovider._classlock.wait()
                # once there is no number available from the IntNumberProvider, provision 
                # one using the IntNumberProvider
                numberprovider.addnumber()
                print("Number Put In From Within {}: {}".\
                    format(threading.current_thread().name, numberprovider.currentnumber()))
            # let thread sleep for 2 seconds before continuing the loop                
            time.sleep(2)       
    # end of method
# end of class

# create the ThreadPoolExecutor
threadpool = concurrent.futures.ThreadPoolExecutor(2, thread_name_prefix="utopia_software")
# submit the tasks that will create a separate worker threads for each task
threadpool.submit(GetNumber.getnumber, threading_with_condition_lock.IntNumberProvider)
threadpool.submit(PutNumber.putnumber, threading_with_condition_lock.IntNumberProvider)
# instruct the threadpool to shutdown
threadpool.shutdown(wait=False)