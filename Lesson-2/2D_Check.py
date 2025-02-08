"""
pseudocode:
Initialize the table data
Print the table
Compute and print the column totals
"""


def main():
    populations = [
        [106,107,111,133,221,767,1766],
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
        print(i, end="  ")
    print("")
    #continent headings
    for i in range(len(continents)):
        buffer_num = 14 - len(continents[i])
        buffer = ""
        #space between continent and first population
        for j in range(buffer_num):
            buffer = buffer + " "
        print(continents[i], end=buffer)
        #populations
        for k in range(len(populations[i])):
            space_num = 6 - len(str(populations[i][k]))
            space = ""
            #space between each population
            for m in range(space_num):
                space = space + " "
            print(populations[i][k], end=space)
        print("")
    for i in range(len(years)):
        year_total = 0
        for j in range(len(populations)):
            year_total += populations[j][i]
        print(f"The total population in {years[i]} was {year_total} million.")

if __name__ == "__main__":
    main()