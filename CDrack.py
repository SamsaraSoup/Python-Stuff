#!/usr/bin/python

"""

This program works out how many CD racks you need when one CD rack holds 25 CD's

"""

__author__ = "Ben Ward"

import math
import os

# Set some variables
rack = 25
another = "y"


def rackinfo():
    import os

    os.system("clear")

    print("Our CD racks can hold 25 CD's")
    print
    print

# Loop starts here
while another == "y":
    rackinfo()

    cdnumber = int(input("How many CD's do you have: "))

    # amount = int(math.ceil(cdnumber / 25.0) * 25.0)    # This code rounds the amount of CD's up to the nearest 25
    # amount = amount / 25

    amount = int(math.ceil(cdnumber / 25) * 25)  # This code rounds the amount of CD's up to the nearest 25
    amount = amount / 25

    print("You will need", amount, " CD racks")
    print
    another = input("Would you like to calculate again? ")

    os.system("clear")
# Loop ends here
