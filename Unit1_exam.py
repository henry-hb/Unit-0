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
    if():
        pass

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
    print(province)
    print(development)



if __name__ == "__main__":
    main()