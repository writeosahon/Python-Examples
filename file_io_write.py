import sys

# print out program heading
programHeading = "PROGRAM BEGINS BELOW (Python Version {})".format(sys.version[0:sys.version.index(" ")])
print(programHeading)
print('=' * len(programHeading))
programHeading = "FILE IO (WRITE) OPERATIONS"
print(programHeading)
print('=' * len(programHeading))

myfile = open('io-files/write-file.txt', mode='a', newline=None) # call function to create file
print("Print Line", file=myfile, flush=True) # call function to write to the file
myfile.write("Write Line\n")
myfile.write("===================================================\n")
myfile.close()

# USING 'with' statement to automatically close file object/stream
with open('io-files/write-file.txt', mode='a', newline=None, encoding="utf-8")  as anotherFile :
    print("Print Line", file=anotherFile, flush=True) # call function to write to the file
    anotherFile.write("Write Line\n")
    anotherFile.write("===================================================\n")
# end of'with' block
