""" file contains example use of importing modules from user-define packages """

__version__ = '0.1 (2019-09-23)'
__author__ = 'UTOPIA SOFTWARE'

import sys
from testmodules import python_decorators


# print out program heading (using multi-line statement)
programHeading = "PROGRAM BEGINS BELOW (Python Version {})".format(\
                sys.version[0:sys.\
                    version.index(" ")])
print(programHeading)
print('=' * len(programHeading))
programHeading = "USER-DEFINED PACKAGES USAGE"
print(programHeading)
print('=' * len(programHeading))

numbers_to_sum = eval(input("""Enter the numbers you want to sum (separated by comma) \u27A4   """))

# format has number with thousand separator
print("POWERS OF 2 of number total({0:,d}) = {number:,d}".\
    format(sum(numbers_to_sum), \
        number=python_decorators.powersOf2SumNumbers(*numbers_to_sum)))

# format as currency with thousand separator
print("POWERS OF 2 of number total({0:,.2f}) = {number:,.2f}".\
    format(sum(numbers_to_sum), \
        number=python_decorators.powersOf2SumNumbers(*numbers_to_sum)))


# JUST TESTING LIST COMPREHENSION
x1 = [i + z for i in ["hello", "everyone"] for z in i ]
print(x1)