"""
Daily problem 10

Author: Hoang Phuong Mai
"""

def print_latin_square():
    """
    Function that creates a Latin Square.
    """
    # let users enter the order
    order = int(input("Enter the order of the Latin Square: "))
    
    # create the Latin Square
    for i in range(1, order+1):
        for j in range(i-1, order):
            print(j, end = ' ')
        for k in range(0, i-1):
            print(k, end = ' ')
        print()

     