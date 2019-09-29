""" file contains thread classes accessing a shared resource in a thread-safe manner 
"""

__version__ = '0.1 (2019-09-29)'
__author__ = 'UTOPIA SOFTWARE'


import sys
# USE THIS IMPORT OF THE THREADING MODULE BECAUSE IN VERSIONS OF PYTHON < 3.7 , THE 
# THREADING MODULE WAS OPTIONAL
try:
    import threading
except ImportError:
    import dummy_threading as threading    
import time
import os
from mythreadspackage import threading_with_condition_lock

# define GetNumberThread class
class GetNumberThread(threading.Thread):
    """ class is a Thread class used to get a number from the IntNumberProvider class.
    """

    def __init__(self, number_provider_class, **kwargs):
        """ constructor method for the  class """

        # call the super class i.e. Thread constructor method
        super().__init__(**kwargs)
        self.__numberprovider = number_provider_class # set the IntNumberProvider for this instance
    # end of method
    
    # run method where the thread executes
    def run(self): 
        while True: # create an infinite loop
            # lock/synchronise access to the IntNumberProvider class using its provider 'lock'
            with threading_with_condition_lock.IntNumberProvider._classlock: 
                
                # wait for a number to be available  
                threading_with_condition_lock.IntNumberProvider._classlock.\
                    wait_for(self.__numberprovider.is_number_available)
                # once a number is available continue the thread and get the number
                print("Number Gotten From Within {}: {}".\
                    format(threading.current_thread().name, self.__numberprovider.getnumber()))
            # let thread sleep for 3 seconds before continuing the loop        
            time.sleep(3)
    # end of method
# end of class

# define PutNumberThread class
class PutNumberThread(threading.Thread):
    """ class is a Thread class used to instruct the IntNumberProvider class to  
    make/provision a number for use.
    """

    def __init__(self, number_provider_class, **kwargs):
        """ constructor method for the  class """

        # call the super class i.e. Thread constructor method
        super().__init__(**kwargs)
        self.__numberprovider = number_provider_class # set the IntNumberProvider for this instance
    # end of method
    
    # run method where the thread executes
    def run(self):
        while True: # create an infinite loop
            # lock/synchronise access to the IntNumberProvider class using its provider 'lock'
            with threading_with_condition_lock.IntNumberProvider._classlock:
                
                # while there is a number available from the IntNumberProvider, 
                # the thread should keep waiting 
                while self.__numberprovider.is_number_available(): 
                    threading_with_condition_lock.IntNumberProvider._classlock.wait()
                # once there is no number available from the IntNumberProvider, provision 
                # one using the IntNumberProvider
                self.__numberprovider.addnumber()
                print("Number Put In From Within {}: {}".\
                    format(threading.current_thread().name, self.__numberprovider.currentnumber()))
            # let thread sleep for 2 seconds before continuing the loop                
            time.sleep(2)       
    # end of method
# end of class

# create a thread each from GetNumberThread and PutNumberThread classes
getthread = GetNumberThread(number_provider_class=threading_with_condition_lock.IntNumberProvider, \
                            name="GetThread")
putthread = PutNumberThread(number_provider_class=threading_with_condition_lock.IntNumberProvider, \
                            name="PutThread")

# start the execution of the created threads
getthread.start()
putthread.start()

# wait for both threads to complete execution
getthread.join()
putthread.join()
