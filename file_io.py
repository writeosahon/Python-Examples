import sys

# print out program heading
programHeading = "PROGRAM BEGINS BELOW (Python Version {})".format(sys.version[0:sys.version.index(" ")])
print(programHeading)
print('=' * len(programHeading))
programHeading = "FILE IO OPERATIONS"
print(programHeading)
print('=' * len(programHeading))

# define a function to get a file/stream object
def getFile(filepath):
    """ get the file/stream object from the 'filepath' provided """
    return open(filepath) # open the file from the filepath provide
# end of function

# define function to seek file to read from a particular location/position of the file
def seekFilePosition(fileObject, offsetPos = 0):
    """ set the file read pointer to a particular position with the file """
    fileObject.seek(offsetPos)
# end of function

# define function to read bytes from a file
def readInputFromFile(fileObject, readBytes = None):
    """ read the byte/data from the file object provided """

    if readBytes is None :
        return fileObject.read()
    else :
        return fileObject.read(readBytes)
# end of function


myfile = getFile('io-files/read-file.txt') # call function to create file
seekFilePosition(myfile, 0)
print(readInputFromFile(myfile)) # call function to read from the file
myfile.close()

# USING 'with' statement to automatically close file object/stream
with getFile('io-files/read-file.txt') as anotherFile :
    seekFilePosition(anotherFile)
    print(readInputFromFile(anotherFile)) # call function to read from the file
# end of'with' block

# USING 'with' statement and 'for' loop to read single line in a file at a time
with getFile('io-files/read-file.txt') as anotherFile :
    seekFilePosition(anotherFile, 0)
    for fileLine in anotherFile: # for loop prints out each line 
        print(fileLine, end="")