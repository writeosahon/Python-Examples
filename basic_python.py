# print out program heading
programHeading = "PROGRAM BEGINS BELOW"
print(programHeading)
print('=' * len(programHeading))

# handling tuples. tuples are not mutable
people = ({"name": "john"},)
person = people[0]["name"]
print("PERSON", person)

# define a simple function
def personal_function(name, age, sex = 'male'):
    """ function documentation contained here """
    # define a variable to hold the printed message
    printedMessage = 'hello {0}. You are {1} years old and a {2}'.format(name.upper(), age, sex)
    print(printedMessage)


vegetables = 'carrots'
print(vegetables)
vegetables = vegetables + ', {0}, {1}'
print(vegetables.format('fruits', 'beans'))

# test boolean and if statements
if 0 > 1 :
    print("0 greater than 1")
else:
    print("0 NOT greater than 1")
# end of if/else
print("thank you")

# call the defined function by positional paramerter
personal_function('john', 25)
personal_function('jane', 20, "female")

# call the defined function by named parameter
personal_function(age = 25, name = 'Paul')
personal_function(age = 19, sex = "female", name = 'Paulette')