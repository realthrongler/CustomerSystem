# Minimal built in functions are to be used and the majority of functions must be
# created yourself

# More packages may be imported in the space below if approved by your instructor
import csv

def printMenu():
    print('''
          Customer and Sales System\n
          1. Enter Customer Information\n
          2. Generate Customer data file\n
          3. Quit\n
          Enter menu option (1-3)
          ''')
    
def enterCustomerInfo():
    '''
        This function takes the customer's information as inputs and stores them to potentially be written to a data file. 
        (See generateCustomerDataFile)
    '''
    firstName = str(input("Please enter the first name.\n"))
    lastName = str(input("Please enter the last name.\n"))
    city = str(input("Please enter the city of residence.\n"))
    #Validating postal code

    #TODO: Make a system that actually works using while loops and breaking with each validation
    #If the postal code returns true, we'll accept it and ask for the credit card, which will return true as well.
    if validatePostalCode():
        print("Postal code valid!")
        #Validating credit card
        if validateCreditCard():
            print("Credit card valid!")
        elif not validateCreditCard():
            print("Credit card invalid! Please try again.")
    elif not validatePostalCode:
        print("Postal code incorrect! Please enter a valid postal code.")

    

def validatePostalCode():
    '''
        This function reads from the CSV file containing the list of postal codes, 
        and determines whether a valid postal code has been entered.
    '''
    code = str(input("Please input the user's postal code.\n"))

    pcList = []

    with open('postal_codes.csv', 'r', newline='', encoding='ISO-8859-1') as csvfile:
        pcReader = csv.reader(csvfile, delimiter='|')
        next(pcReader, None) #skips the header
        for row in pcReader:
            pcList.append(row[0])

    if code in pcList:
        return True, code
def validateCreditCard():
    print("this is a valid card frfr")
'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''
def generateCustomerDataFile():
    pass    # Remove this pass statement and add your own code below

####################################################################
#       ADDITIONAL METHODS MAY BE ADDED BELOW IF NECESSARY         #
####################################################################




####################################################################
#                            MAIN PROGRAM                          #
#           DO NOT EDIT ANY CODE EXCEPT WHERE INDICATED            #
####################################################################

# Do not edit any of these variables
userInput = ""
enterCustomerOption = "1"
generateCustomerOption = "2"
exitCondition = "3"

# More variables for the main may be declared in the space below


while userInput != exitCondition:
    printMenu()                 # Printing out the main menu
    userInput = input();        # User selection from the menu

    if userInput == enterCustomerOption:
        # Only the line below may be editted based on the parameter list and how you design the method return
        # Any necessary variables may be added to this if section, but nowhere else in the code
        enterCustomerInfo()

    elif userInput == generateCustomerOption: 
        # Only the line below may be editted based on the parameter list and how you design the method return
        generateCustomerDataFile()

    else:
        print("Please type in a valid option (A number from 1-3)")

#Exits once the user types 
print("Program Terminated")
