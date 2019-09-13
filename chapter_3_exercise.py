""" this exercise prints various travel instructions to the user based on the 
number of miles the user wishes to travel """

# get the number of miles user wishes to travel
numberOfMiles = round(float(input("how many miles do you want to travel? ")))

# check what mode of transportation should be used
if numberOfMiles < 3:
    print("You should walk. It's just {0} miles".format(numberOfMiles))
elif numberOfMiles >=3 and numberOfMiles < 300:
    print("You should drive the {0} miles".format(numberOfMiles))
else:
    print("You should fly the {0} miles".format(numberOfMiles))