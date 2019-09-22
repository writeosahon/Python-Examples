""" file contains simple examples on Python Classes """

import sys


# print out program heading (using multi-line statement)
programHeading = "PROGRAM BEGINS BELOW (Python Version {})".format(\
                sys.version[0:sys.\
                    version.index(" ")])
print(programHeading)
print('=' * len(programHeading))
programHeading = "PYTHON SIMPLE CLASSES"
print(programHeading)
print('=' * len(programHeading))

# DEFINE GLOBAL VARIABLES #
animals = [] # holds all animals created
# END OF GLOBAL VARIABLES 

class Animal() :
    """ base Animal class"""
    
    # class/static attribute 
    animalCount = 0 # holds the number of animals that have been instantiated from this class

    def __init__(self, specieName):

        """ class constructor """
        # increase the animalCount static attribute by 1
        Animal.animalCount += 1 
        # define an instance attribute
        self.specieName = specieName # holds the name of the animal species
    
    def changeSpecieName(self, newName):
        """ instance method changes the name of the animal species """
        self.specieName = newName # change the specie name for this animal instance
        
# end of class

# creating sub-class
class Dog(Animal):
    """ definition for Dog class. This class inherits from Animal class """
    def __init__(self, specieName):
        ''' class constructor '''
        super().__init__(specieName) # call the super class constructor
# end of class


# print the animal count after creating instance of Animal within a for loop
for index in range(12) :
    animals.append(Animal("cow")) # create an animal instance and add it to the animals list
# print the number of animal created so far using the class attribute
print("Animals created so far: {}".format(Animal.animalCount))

# get the last animal in the animals list and change it's species name
animals[-1].specieName = "Eagle"
print("New Specie Name for Last Animal is: {specieName}".format(specieName=animals[-1].specieName)) 

# create an instance of the sub-class Dog
animals.append(Dog("Doggy"))
print("New animal created from the {specieName} specie".format(specieName=animals[-1].specieName))

# print the number of animal created so far using the class attribute
print("Animals created so far: {}".format(Animal.animalCount))

# get the last animal in the animals list and change it's species name
animals[-1].specieName = "Dog"
print("New Specie Name for Last Animal is: {specieName}".format(specieName=animals[-1].specieName)) 
print(isinstance(animals[-1], Dog))
print(Dog == animals[-1].__class__)
print(Dog.__dict__)