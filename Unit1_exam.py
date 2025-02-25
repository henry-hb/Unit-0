def check_first(code, letters):
    for i in letters:
        if(code[0] == letters[i]):
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
        "X" : "Nunavut or NOrthwest Territories",
        "Y" : "Yukon"
    }

    postal_code= input("What is your postal code")
    while(check_first(postal_code, first_char) != True):
        print("Not a valid first character. Try again")
        postal_code= input("What is your postal code")

if __name__ == "__main()__":
    main()