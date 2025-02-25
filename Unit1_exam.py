#checks if first letter of postal code equals any keys in provinces
def check_first(code, letters):
    for i in letters:
        if(code[0:1].upper() == i):
            return True
    return False
#checks if the second digit of postal code equals 0
def check_second(code):
    if(code[1:2] == "0"):
        return "Rural"
    return "Urban"
#checks if 1,3,5 are letters and 2,4,6 are numbers
def check_validity(code):
    odds = []
    odds.append(str(code[0:1]))
    odds.append(str(code[2:3]))
    odds.append(str(code[4:5]))
    evens = []
    evens.append(str(code[1:2]))
    evens.append(str(code[3:4]))
    evens.append(str(code[5:]))
    for i in odds
        if (i.isAlpha()):
            for j in evens:
                if(j.isDigit()):
                    return True
            return True
    return False

def main():
    first_char = {
        "A" : "Newfoundland",
        "B" : "Nova Scotia",
        "C" : "Prince Edward Island",
        "E" : "New Brunswick",
        "G" : "Quebec",
        "H" : "Quebec",
        "J" : "Quebec",
        "K" : "Ontario",
        "L" : "Ontario",
        "M" : "Ontario",
        "N" : "Ontario",
        "P" : "Ontario",
        "R" : "Manitoba",
        "S" : "Saskatchewan",
        "T" : "Alberta",
        "V" : "British Columbia",
        "X" : "Nunavut or Northwest Territories",
        "Y" : "Yukon"
    }

    #catches to see if code is correct length
    postal_code=input("What is your postal code? ")
    while(not len(postal_code.strip()) == 6):
        print("Postal code is not the correct length to be valid in Canada. It should be 6 characters. Try again")
        postal_code=input("What is your postal code? ")
    #checks to see if the characters are correct in the right indices
    while(not check_validity(postal_code)):
        print("Postal code is not the correct characters to be valid in Canada. \nThe 1st 3rd and 5th characters should be letters, and the 2nd 4th and 6th characters should be numbers. Try again")
        postal_code=input("What is your postal code? ")
    #catches to see if first character is valid
    while(not check_first(postal_code, first_char)):
        print("Not a valid first character. Try again")
        postal_code=input("What is your postal code? ")
    #catches if second digit is valid
    while(not postal_code[1:2].isdigit()):
        print("Not a valid second digit. It should be a number. Try again")
        postal_code=input("What is your postal code? ")
    #sets province and development to the characteristic indicated by code
    province = first_char[postal_code[0:1]]
    development = check_second(postal_code)
    print(f"Your postal code is {postal_code}, and you live in {development} {province}.")



if __name__ == "__main__":
    main()
