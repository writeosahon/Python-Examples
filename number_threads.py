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

class GetNumberThread(threading.Thread):
    def __init__(self, number_provider_class, **kwargs):
        super().__init__(**kwargs)
        self.__numberprovider = number_provider_class
    # end of method
    
    def run(self):
        while True:
            with threading_with_condition_lock.IntNumberProvider._classlock:
                threading_with_condition_lock.IntNumberProvider._classlock.\
                    wait_for(self.__numberprovider.is_number_available)
                print("Number Gotten From Within {}: {}".\
                    format(threading.current_thread().name, self.__numberprovider.getnumber()))
            time.sleep(2)
    # end of method
# end of class

class PutNumberThread(threading.Thread):
    def __init__(self, number_provider_class, **kwargs):
        super().__init__(**kwargs)
        self.__numberprovider = number_provider_class
    # end of method
    
    def run(self):
        while True:
            with threading_with_condition_lock.IntNumberProvider._classlock:
                while self.__numberprovider.is_number_available():
                    threading_with_condition_lock.IntNumberProvider._classlock.wait()
                print("Number Put In From Within {}: {}".\
                    format(threading.current_thread().name, self.__numberprovider.addnumber()))
    # end of method
# end of class

# start a thread each from GetNumberThread and PutNumberThread classes
getthread = GetNumberThread(number_provider_class=threading_with_condition_lock.IntNumberProvider, \
                            name="GetThread")
putthread = PutNumberThread(number_provider_class=threading_with_condition_lock.IntNumberProvider, \
                            name="PutThread")

getthread.start()
putthread.start()

getthread.join()
putthread.join()
