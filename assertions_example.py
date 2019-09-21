import sys

# print out program heading (using multi-line statement)
programHeading = "PROGRAM BEGINS BELOW (Python Version {})".format(\
                sys.version[0:sys.\
                    version.index(" ")])
print(programHeading)
print('=' * len(programHeading))
programHeading = "PYTHON ASSERTIONS"
print(programHeading)
print('=' * len(programHeading))


# create some assertion condition
assertionCondition = False

try: # create a try block to catch the raised AssertionError
    assert assertionCondition, "My Custom Assertion Failed" # creates an assertion statement
except AssertionError as e: # catch the assertion error
    print(e) # print out the error

assert assertionCondition, "My Second Custom Assertion Failed" # create another assertion statement