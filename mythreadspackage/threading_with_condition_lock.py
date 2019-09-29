""" file contains a class that implements synchronised/thread-safe 
operations using condition-lock to ensure synchronised/threed-safe access to class members 
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
import abc
import random
from . import errors # user-defined module from within current user-defined package


# print out program heading (using multi-line statement)
programHeading = "PROGRAM BEGINS BELOW (Python Version {})".format(\
                sys.version[0:sys.\
                    version.index(" ")])
print(programHeading)
print('=' * len(programHeading))
programHeading = "PYTHON THREAD (CONDITION LOCK/SYNCHRONISATION)"
print(programHeading)
print('=' * len(programHeading))
#==================================================================


class IntNumberProvider(abc.ABC):
    """ class is used to provide integer numbers to the requesting client.

    This class and it's methods are thread-safe/synchronised. 
    The class cannot be instantiated. All it's methods are to be accessed through the class object
    """
    
    # static variable that indicates if class has numbers to give
    __hasnumber = False # flag indicates if class has number to provide
    __number = None # holds the number that has been generaqgted for provision  or None if no number
    _classlock = threading.Condition() # create a condition lock for the class
    
    
    # static abstract method public method
    @staticmethod
    @abc.abstractmethod
    def is_number_available() -> bool:
        """ static public method used to check if there is any number available for provision.
        return True if a number is available or False otherwise
         """

        with IntNumberProvider._classlock: # lock /synchronise access to class data
            IntNumberProvider._classlock.notify_all() # notify all waiting threads that lock is about to be released
            return IntNumberProvider.__hasnumber
    
    @staticmethod
    @abc.abstractmethod
    def addnumber():
        """ static public method used to create/generate number available for provision """
        with IntNumberProvider._classlock: # lock /synchronise access to class data

            # check if there is already a number available for provison or not.
            # 'if block' is run when the __hasnumber flag indicates there is no number available AND 
            # the __number class varaible is None
            if  (not IntNumberProvider.__hasnumber) and IntNumberProvider.__number is None:
                # generate a new number and store it
                IntNumberProvider.__number = next(iter(IntNumberProvider.__generatenumber()))
                # set the __hasnumber flag to True i.e. a number is available for provision
                IntNumberProvider.__hasnumber = True
            
            # notify all waiting threads that lock is about to be released
            IntNumberProvider._classlock.notify_all()
    
    @staticmethod
    @abc.abstractmethod
    def getnumber() -> int:
        """ static public method used to get number available for provision.
        
        method will return int if a number is available else it will 
        raise mythreadspackage.errors.NoNumberError.
        To prevent NoNumberError arising users should first call IntNumberProvider.addnumber 
        """
        with IntNumberProvider._classlock: # lock /synchronise access to class data

            # if there is no number available
            if  (not IntNumberProvider.__hasnumber) and IntNumberProvider.__number is None:
                IntNumberProvider._classlock.notify_all() # notify threads that lock is about to be released
                # raise error
                raise errors.NoNumberError("No number is available to provide")

            # since there is a number available    
            thenumber = IntNumberProvider.__number # get the available number
            IntNumberProvider.__number = None # reset the class __number property to None
            IntNumberProvider.__hasnumber = False # reset the __hasnumber flag to False

            IntNumberProvider._classlock.notify_all() # notify the waiting threads that lock is about to be released
            return thenumber # return the available number that was stored prior to reset


    @staticmethod
    @abc.abstractmethod
    def __generatenumber():
        """ static private helper generator function.
        Method returns an iterable
        method is used to generate a random int number. 
        This helper method is used by addnumber method 
        """
        yield random.randint(0, sys.maxsize) # generate random int
