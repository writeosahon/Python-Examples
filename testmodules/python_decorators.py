""" module that provides the powers of 2 for a number 

The module tests out package importation as this module is located in 
package.
"""

__version__ = '0.1 (2019-09-23)'
__author__ = 'UTOPIA SOFTWARE'

import sys


# decorator function
def _powersOf2(function):
    """ decorator function to get the power of 2 of a number """

    def inner_help(*args, **kwargs):
        sum = function(*args, **kwargs)
        return sum ** 2

    return inner_help

# function using the decorator / (user-defined decorator function)
@_powersOf2
def powersOf2SumNumbers(*args):
    """" returns the power of 2 from a sum of numbers provided as argument(s) """
    return sum(args)
