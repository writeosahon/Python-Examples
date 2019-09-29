""" file contains simple examples on Python DateTime operations """

import sys
import datetime


# print out program heading (using multi-line statement)
programHeading = "PROGRAM BEGINS BELOW (Python Version {})".format(\
                sys.version[0:sys.\
                    version.index(" ")])
print(programHeading)
print('=' * len(programHeading))
programHeading = "PYTHON DATE-TIME OPERATIONS"
print(programHeading)
print('=' * len(programHeading))

my_date_delta = datetime.timedelta(weeks=2)
print("Date Differnce in days", my_date_delta.days)
