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
    #Getting customer information

    firstName = str(input("Please enter the first name.\n")).capitalize()
    lastName = str(input("Please enter the last name.\n")).capitalize()
    city = str(input("Please enter the city of residence.\n")).capitalize()
    
    global data_dictionary
    data_dictionary = {}

    data_dictionary["First name"] = firstName
    data_dictionary["Last name"] = lastName
    data_dictionary["City"] = city

    #Booleans to break the while loops below, to ensure the user inputs a valid postal code/credit card
    codeVerified = False
    cardVerified = False

    while codeVerified == False:
        codeVerified = validatePostalCode()
    print("Postal code validated!")

    while cardVerified == False:
        cardVerified = validateCreditCard()
    
def validatePostalCode():
    '''
        This function reads from the CSV file containing the list of postal codes, 
        and determines whether a valid postal code has been entered.
    '''
    global postal_Code
    postal_Code = str(input("Please input the first 3 letters of a valid postal code.\n")).strip().upper()

    pcList = []

    with open('postal_codes.csv', 'r', newline='', encoding='ISO-8859-1') as csvfile:
        pcReader = csv.reader(csvfile, delimiter='|')
        next(pcReader, None) #skips the header
        for row in pcReader:
            pcList.append(row[0])

    if postal_Code in pcList:
        data_dictionary["Postal code"] = postal_Code
        return True
    else:
        print("Postal code error. Please input the first 3 letters of a valid postal code.")
        return False

def validateCreditCard():
    '''This function asks the user to input a credit card number and uses the Luhn algorithm to
    verify whether or not it is a valid credit card number'''
    cardInput = str(input("Please input a valid credit card number.\n"))

    #Checking for the user inputting nothing
    if cardInput.strip() == "":
        print("Please enter a number.")
        return False
    cardNumber = list(cardInput)
    
    #credit card number validation
    for i in range(len(cardNumber)):
        if cardNumber[i].isalpha():
            print("Please enter the credit card number only, no letters.\n")
            return False
    
    #reversal of credit card number
    cardNumber.reverse()
    reversedNumber = cardNumber
    
    #Checking to see if all the credit card numbers are zero
    zero_Check = 0
    for i in range(len(cardNumber)):
        zero_Check += int(cardNumber[i])
    if zero_Check == 0:
        print("Please enter a credit card number that is not entirely zeroes.")
        return False

    #digits in odd indices
    odd_digits = []
    for i in range(0, len(reversedNumber), 2): 
        odd_digits.append(reversedNumber[i])

    #digits in even indices
    even_digits = []
    for i in range(1, len(reversedNumber), 2): 
        even_digits.append(reversedNumber[i])
    
    #sum of digits in odd indices
    sum1 = 0
    for i in range(len(odd_digits)):
        #Handling spaces in between the numbers
        try:
            sum1 += int(odd_digits[i])
        except:
            print("There was an error. Please input a valid credit card number without spaces.")
            validateCreditCard()
    
    #sum of digits in even indices
    sum2 = 0
    for i in range(len(even_digits)):
        #Handling spaces in the number
        try:
            #Handling digits that, when doubled, are higher than 9
            number = int(even_digits[i]) * 2
            if number == 10:
                number = 1
            elif number == 12:
                number = 3
            elif number == 14:
                number = 5
            elif number == 16:
                number = 7
            elif number == 18:
                number = 9
            sum2 += number
        except:
            print("There was an error. Please enter a valid credit card number without spaces.")

    finalSum = sum1 + sum2
    checkSum = str(finalSum)
    
    if checkSum[-1] == "0":
        print("Credit card validated!")
        data_dictionary["Credit card"] = cardInput
        print(f"Data saved!")
        customerData.append(data_dictionary)
        return True 
    else:
        print("This credit card number is invalid.")
        return False

def generateCustomerDataFile():
    '''This function generates a csv file and writes into it the data entered by the user.
    For convenience, it writes all the saved customer data into a CSV file at once, to save time
    when working with high numbers of customers'''

    file_name = str(input("Please input a file name with the extension \".csv\" for the data to be written to.\n"))
    try:
        with open(str(file_name), "w", newline="") as csvfile:
            #initializing CSV writer
            writer = csv.DictWriter(csvfile, fieldnames=["First name", "Last name", "City", "Postal code", "Credit card"], delimiter="|")
            
            #Write the fieldnames in the first row
            writer.writeheader()
            try:
                #Writing dictionary into CSV file
                writer.writerows(customerData)
                print("Data file generated!")
            except:
                print("There was an error. Please make sure the CSV file you are trying to write into does not have any conflicting IDs.")    
            #Emptying dictionary when written into file
            customerData.clear()
    except:
        print("There was an error. Please try again, and make sure the name of the file is not already taken.")

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
customerData = []
#This template is giving me brain damage

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
