"""
pseudocode:
Initialize the table data
Print the table
Compute and print the column totals
"""


def main():
    populations = [
        [106,107,111,133,221.767,1766],
        [502,635,809,947,1402,3634,5268],
        [2,2,2,6,13,30,46],
        [163,203,26,408,547,729,628],
        [2,7,26,82,172,307,392],
        [16,24,38,74,167,511,809]
        ]

    continents = [
        "Africa",
        "Asia",
        "Australia",
        "Europe",
        "North America",
        "South America"
    ]

    years = [1750, 1800, 1850, 1900, 1950, 2000, 2050]
    

    #years
    print("    Years     ", end="")
    for i in years:
        print(i, end="   ")
    print("")
    #continent headings
    for i in continents:
        print(i)

if __name__ == "__main__":
    main()