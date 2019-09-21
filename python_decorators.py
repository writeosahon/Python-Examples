import sys

# print out program heading (using multi-line statement)
programHeading = "PROGRAM BEGINS BELOW (Python Version {})".format(\
                sys.version[0:sys.\
                    version.index(" ")])
print(programHeading)
print('=' * len(programHeading))
programHeading = "PYTHON DECORATORS"
print(programHeading)
print('=' * len(programHeading))


# decorator function
def powersOf2(function):
    def inner_help(*args, **kwargs):
        sum = function(*args, **kwargs)
        return sum ** 2

    return inner_help

# function using the decorator / (user-defined decorator function)
@powersOf2
def powersOf2SumNumbers(*args):
    return sum(args)

print("Powers of 2: {}".format(powersOf2SumNumbers(5, 5, 10)))