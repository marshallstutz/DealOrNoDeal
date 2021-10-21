#deal or no deal
import random

# All case values, in order
baseCases = [.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750,
1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]
allCases = []
case = 0
caseValue = 0



# Find the total value of all cases, probably not used
totalVal = 0
for x in range(len(baseCases)):
    totalVal += baseCases[x]

# Function for initializing the gameOver
def initialize():
    print("***********************************")
    print("Starting new game")
    print("***********************************")
    #Initializing user case and user case value
    case = 0
    caseValue = 0

    # Copy the random cases into a new array called random cases and randomize it using a mathod from random
    randomCases = baseCases.copy()
    random.shuffle(randomCases)
    # Create a 2d array called allCases which will contain the case number and value
    global allCases
    allCases = []
    for x in range(len(randomCases)):
        allCases.append([x+1, randomCases[x]])

# removes case from allCases
def removeCase(x):
    for y in range(len(allCases)):
        if allCases[y][0] == x:
            allCases.pop(y)
            return

# Function to print the contents of allCases, used for debugging
def printAllCases():
    for x in range(len(allCases)):
        print(allCases[x])

# prints the list of available cases
def printCases():
    for x in range(len(allCases)):
        print(allCases[x][0], end = ' ')
    print()

# Function to return a dollar formatted string when give int
def getStr(val):
    return "${:,.2f}".format(val)

# gets the value of a case
def getCaseValue(x):
    for y in range(len(allCases)):
        if allCases[y][0] == x:
            return allCases[y][1]

# Get and validate the user input for selecting a case to open
def getNextCase():
    while True:
        try:
            tempCase = int(input("Pick a case to open: "))
        except ValueError:
            print("Response must be a number")
            continue
        for x in range(len(allCases)):
            if allCases[x][0] == tempCase:
                return tempCase
        print("Number chosen was not an available case to choose")

# Function to get next case and remove it
def getAndRemoveCase():
    #print cases
    printCases()

    #get user input for case to remove
    nextCase = getNextCase()
    print("Case " + str(nextCase) + " chosen. Value is " + getStr(getCaseValue(nextCase)))
    removeCase(nextCase)

# Shows all values for remaining cases, plus the user chosen case
def showCaseValues():
    caseValues = []
    for x in range(len(allCases)):
        caseValues.append(allCases[x][1])
    caseValues.append(caseValue)
    caseValues.sort()
    print("Remaining case values: ", end = ' ')
    for x in range(len(caseValues)):
        print(getStr(caseValues[x]), end = ' ')
    print()

# Gets number of cases needed to open bases on how many are left
def getCasesToOpen():
    x = len(allCases)
    if x == 25:
        return 6
    if x == 19:
        return 5
    if x == 14:
        return 4
    if x == 10:
        return 3
    if x == 7:
        return 2
    if x < 6 and x > 1:
        return 1
    if x == 1:
        return 0

# Function to get the bankers offer
def getBankersOffer():
    totalCaseValue = 0
    for x in range(len(allCases)):
        totalCaseValue = totalCaseValue + allCases[x][1]
    totalCaseValue = totalCaseValue + caseValue
    averageCaseValue = totalCaseValue / (len(allCases) + 1)
    #return average case value for now unless I get more motivated to put in a more realistic calculation
    return averageCaseValue

# Function for user input of bank offer
def getYesNo():
    while True:
        response = input("The bankers offer is " + getStr(getBankersOffer()) + ". Do you accept? (y/n) ")
        if response == 'y' or response == 'Y':
            return 1
        if response == 'n' or response == 'N':
            return 0
        else:
            print("Unknown input. Please type 'y' or 'n' to respond to the banker.")

# Function for user input of final 2 cases
def getYesNoFinal():
    while True:
        response = input("Do you wish to trade cases with the last remaining case? (y/n) ")
        if response == 'y' or response == 'Y':
            return 1
        if response == 'n' or response == 'N':
            return 0
        else:
            print("Unknown input. Please type 'y' or 'n' to respond to the banker.")

# Function to get the initial case
def getFirstCase():
    while True:
        try:
            case = int(input("Pick a case between 1 and 26: "))
        except ValueError:
            print("Response must be a number")
            continue
        if case < 1 or case > 26:
            print("Number entered must be between 1 and 26")
        else:
            #number is valid
            return case



while True:
    initialize()
    # Get the case the user wants to pick
    case = getFirstCase()

    print("Case " + str(case) + " chosen.")
    #remove the user chosen case from the allCases list and set the user case value
    caseValue = getCaseValue(case)
    removeCase(case)

    gameOver = 0
    while gameOver == 0:
        casesToOpen = getCasesToOpen()
        if casesToOpen == 0:
            tempValue = []
            tempValue.append(caseValue)
            tempValue.append(allCases[0][1])
            tempValue.sort()
            print("The final two case values are " + getStr(tempValue[0]) + " and " + getStr(tempValue[1]))
            final = getYesNoFinal()
            if final == 1:
                print("You traded cases. You won " + getStr(allCases[0][1]) + ", and if you didn't trade you would have won " + getStr(caseValue))
            else:
                print("You didn't trade cases. You won " + getStr(caseValue) + " and if you did trade you would have won " + getStr(allCases[0][1]))
            gameOver = 1
            continue
        print("You need to open " + str(casesToOpen) + " case(s)")
        count = 0
        while count < casesToOpen:
            getAndRemoveCase()
            count = count + 1

        showCaseValues()
        #print("The banker offers " + str(getBankersOffer()) + ". Accept? (y/n)")
        gameOver = getYesNo()
