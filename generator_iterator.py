""" file contains python generator function. 
Python generator function ALWAYS returns an Iterator object. 
A generator function is created by using 'yield' within the function """

import sys


# print out program heading (using multi-line statement)
programHeading = "PROGRAM BEGINS BELOW (Python Version {})".format(\
                sys.version[0:sys.\
                    version.index(" ")])
print(programHeading)
print('=' * len(programHeading))
programHeading = "PYTHON ITERATOR CLASS"
print(programHeading)
print('=' * len(programHeading))

# DEFINE GLOBAL VARIABLES HERE #

# END OF GLOBAL VARIABLES 

class Animal() :
    """ base Animal class"""
    
    # class/static attribute 
    animalCount = 0 # holds the number of animals that have been instantiated from this class
    animalsCreated = [] # holds the list of all animals instantiated so far

    def __init__(self, specieName):
        """ class constructor """
        # increase the animalCount static attribute by 1
        Animal.animalCount += 1 
        # define an instance attribute
        self.specieName = specieName # holds the name of the animal species
        self.iteratorCounter = 0 # set the iterator counter for this instance
        Animal.animalsCreated.append(self) # add the created animal to the animalCreated collection
    
    def changeSpecieName(self, newName):
        """ instance method changes the name of the animal species """
        self.specieName = newName # change the specie name for this animal instance
    
    # create generator function
    def getAnimalsInOrder(self):
        """ This is a generator function .
        Get an iterator object which yields every created animal in order """
        for animal in Animal.animalsCreated :
            yield animal
        

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
    Animal("cow") # create an animal instance

# print the number of animal created so far using the class attribute
print("Animals created so far: {}".format(Animal.animalCount))

# get the last animal in the animals list and change it's species name
Animal.animalsCreated[-1].specieName = "Eagle"
print("New Specie Name for Last Animal is: {specieName}".\
    format(specieName=Animal.animalsCreated[-1].specieName)) 

# create an instance of the sub-class Dog
Dog("Doggy")
print("New animal created from the {specieName} specie".\
    format(specieName=Animal.animalsCreated[-1].specieName))

# print the number of animal created so far using the class attribute
print("Animals created so far: {}".format(Animal.animalCount))

# print out the specie name of all animals created so far
for animal in Animal("Cat").getAnimalsInOrder():
    print("Animal Species: {}".format(animal.specieName))