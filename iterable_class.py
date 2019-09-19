""" file contains iterable Python Class.
i.e a class that implements the iterator protocol """

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

    def __iter__(self):
        """ implements the __iter__() method as part of the iterator protocol.
        Use to iterator over the collection of created animals """
        
        self.iteratorCounter = 0 # set the iterator counter to zero
        return self # return the this class instance
    
    def __next__(self):
        """ implements the __next__() method as part of the iterator protocol"""

        # check if this another item can be delivered from the animalsCreated list
        if(self.iteratorCounter < len(Animal.animalsCreated)): # iterCounter < animalsCreated list length
            self.iteratorCounter += 1 # increase the iteratorCounter by 1
            return Animal.animalsCreated[self.iteratorCounter -1] # return thre animal in the specified index
        else: # iterCounter >= animalsCreated list length
            raise StopIteration # raise this exception to stop the iteration

    
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
for animal in Animal("Cat"):
    print("Animal Species: {}".format(animal.specieName))