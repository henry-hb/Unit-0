def find_average_price(price1,price2):
    return (price1+price2)/2

def cube_volume(side_length):
    """returns the volume of a cube
    """
    volume = side_length * side_length * side_length
    return round(volume, 2)


# exception for not printing inside functions
def main():
    '''price1 = float(input ("What is the price? "))
    price2 = float(input ("What is the price? "))
    avg_price = find_average_price(price1,price2)
    # .2f rounds to 2 decimal places
    print(f"The average price of ${price1} and ${price2} is ${avg_price:.2f}.")
    '''

    cube_wid = float(input("What is the width of the cube? "))
    cube_vol = cube_volume(cube_wid)
    print(cube_vol)

if __name__ == '__main__':
    main()