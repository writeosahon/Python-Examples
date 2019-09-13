""" 
grocery list program. 
making use of lists, functions, loops """

# print out program heading
programHeading = "GROCERY LIST PROGRAM BEGINS BELOW"
print(programHeading)
print('=' * len(programHeading))

groceryList = [] # holds grocery list items

def addGroceryListItem (item = ""):
    """ FUNCTION ADDS ITEMS TO A GROCERY LIST COLLECTION i.e. groceryList """ 
    if item != "" :
        groceryList.append(item) # add item to the grocery list if it is not an empty string
        return item # return the item provided

def printGroceryList(): 
    """ FUNCTION PRINTS OUT THE AVAILABLE GROCERY LIST """
    print("Grocery List of {1} Item(s): {0}". format(groceryList, len(groceryList)))
    """ end of function """

def printSortedGroceryList():
    """ FUNCTION PRINTS OUT THE SORTED AVAILABLE GROCERY LIST """
    print("Sorted Grocery List: {0}".format(sorted(groceryList)))
    """ end of function """

receiveInput = True # boolean variable to determine if grocery input should still be received

while receiveInput : # check if input should be received
    groceryInput = input("enter grocery item. enter empty string to stop entry: ") # collect input
    
    if groceryInput == "" : # if gricery input is an empty string, terminate loop
        receiveInput = False
    else: # add input to grocery list
        addGroceryListItem(groceryInput)
    """ end of while loop """

# print out the current grocery list and sorted grocery list
printGroceryList()
printSortedGroceryList()
