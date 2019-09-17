import sys
import numpy


# print out program heading (using multi-line statement)
programHeading = "PROGRAM BEGINS BELOW (Python Version {})".format(\
                sys.version[0:sys.\
                    version.index(" ")])
print(programHeading)
print('=' * len(programHeading))
programHeading = "PYTHON MODULES"
print(programHeading)
print('=' * len(programHeading))

# print system's module path
for path in sys.path: # loop through all the moduule search paths
    print("module path: {}".format(path))
