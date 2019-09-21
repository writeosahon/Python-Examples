""" file contains examples on Python @property decorator in classes"""

import sys


# print out program heading (using multi-line statement)
programHeading = "PROGRAM BEGINS BELOW (Python Version {})".format(\
                sys.version[0:sys.\
                    version.index(" ")])
print(programHeading)
print('=' * len(programHeading))
programHeading = "PYTHON @PROPERTY DECORATOR IN CLASSES"
print(programHeading)
print('=' * len(programHeading))

# DEFINE GLOBAL VARIABLES #
animals = [] # holds all animals created
# END OF GLOBAL VARIABLES 

class Animal() :
    """ base Animal class"""
    
    # static attribute 
    animalCount = 0 # holds the number of animals that have been instantiated from this class

    def __init__(self, specieName):
        """ class constructor """
        # increase the animalCount static attribute by 1
        Animal.animalCount += 1 
        # define an instance attribute
        self.specieName = specieName # holds the name of the animal species
    
    # property decorator for specieName
    @property
    def specieName(self):
        """ method is used to set the specieName property of the instance """
        return (self._specieName + " ") * 2
    
    @specieName.setter
    def specieName(self, specieName):
        """ instance method changes the name of the animal species """
        self._specieName = specieName

    @specieName.deleter
    def specieName(self):
        """ instance method changes the name of the animal species """
        del self._specieName
    
    
# end of class

animals.append(Animal("Pigeon"))

print("Animal Specie: {}".format(animals[-1].specieName))