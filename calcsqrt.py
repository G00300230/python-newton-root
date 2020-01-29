#! /usr/bin/env python3

# Cuan O'Conchuir 29/02/2020
# Calculate Sqrt of a number.

def sqrt(x):
    """
    calculate the square root oof the arguement x
    """
    # check that z is positive
    if x < 0
        print("error negative value supplied")
        return -1

    # initial guess for the sqrt
    z = x/2.0

    # continuously improve the guess
    # adapted from https://tour.golang.org/flowcontrol/8
    while abs(x - (z*z)) > 0.000001:
        z = z - ((z*z - x)/(2*z))

    return z
myval = 63.0
print("The square root of", myval, "is", sqrt(myval))


