# ------------------------------------------------------------ 
# Global variables 
# ------------------------------------------------------------ 
'''
caravans = ["Excellent", "Premium", "Prestige", "Nova", "Eco", 
            "Evolution", "Tourer"] 
names =["Livinitup", "Waltzing Matilda", "Home Sweet Home", 
        "Seldom Inn", "Seeyoulater", "The Long Haul", 
        "Happycampers", "On Tour", "Home & Away"]

def printAnyList (pList):
    print ("This input list has " + str (len (pList)) + " items.") 
    for item in pList:
        print (item)


printAnyList (names)
printAnyList (caravans)

# Activity 2
# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
theNumber = 0                   # Invalid input
theVegetable = ""               # Empty string

# ------------------------------------------------------------
# Subprograms
# ------------------------------------------------------------
# =====> Write the definition of the subprogram here
def shortVegetable(pVeg, pNum):
    print("orignal Veg",pVeg)
    if (len(pVeg) >= pNum):
        print (pVeg[0:pNum])
    else:
        print ("Number is longer than vegetable")


# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------

theNumber = int(input ("Enter your favourite number, less than 10 (0 to exit): "))
while (theNumber != 0):
    theVegetable = input ("Enter your favourite vegetable: ")

    # =====> Add a call to the subprogram, including passing arguments
    
    shortVegetable( theNumber,theVegetable)
    theNumber = int(input("Enter your favourite number, less than 10 (0 to exit): "))

# Activity 3
# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
caravans = ["Excellent", "Premium", "Prestige", "Nova", "Eco",
            "Evolution", "Tourer"]
totalSold = [93, 74, 28, 102, 77, 97, 106]
costCaravan = [33550.75, 27250.49, 25950.00, 24495.99,
               23750.25, 20595.95, 19195.03]
# ------------------------------------------------------------
# Subprograms
# ------------------------------------------------------------
def showAverage (pList):
    total = 0
    average = 0.0
    for item in pList:
        total = total + item
    average = total / len(pList)
    print (average)

# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
showAverage (totalSold)
showAverage (costCaravan)
print ("Goodbye")



# Homework Activity 2
# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
weeklyStats = [23, 15, 6, 5, 2, 0, 0,
               19, 15, 7, 3, 0, 3, 3]
messages = ["Error", "OK", "OK", "Error", "Error", "OK", "OK",
            "OK", "Error", "Error", "Error", "OK", "OK", "OK"]

# ------------------------------------------------------------
# Subprograms
# ------------------------------------------------------------
# =====> Write your subprogram here
def error_count(messages,target):
    count = 0
    
    for i in messages:
        if i == target:
            count += 1
    print(f"Error occurs {count} times.")
# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
# =====> Write your main program here

error_count(messages,'Error')
error_count(weeklyStats,0)
'''

# Homework Activity 1
# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
weeklyStats = [23, 15, 6, 5, 2, 0, 0,
               19, 15, 7, 3, 0, 3, 3]

# ------------------------------------------------------------
# Subprograms
# ------------------------------------------------------------
# =====> Write a definition for a subprogram named 'genStats'.
#        It has one input parameter named 'pList'.
def genStats(pList):
    min = 9999
    max = 0
    total = 0
    average = 0.0

    # ====> Write a 'for in list' loop to iterate over
    #       the input list.
    for item in pList:
        total = total + item
        if (item < min):
            min = item
        if (item > max):
            max = item

    # =====> Calculate the average based on 'total' and
    #        the length of the input list.
    #ive forgotten how to calculate
    #avg=(12+1+2)/3
    
    average = total/len(pList)

    print ("Min:", min, "Max:", max, "Average:","{:.2f}".format(average))

# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
# =====> Write a call to 'genStats' sending 'weeklyStats' as
#        the argument

genStats(weeklyStats)
