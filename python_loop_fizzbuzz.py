#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#
i = 0
n = 0


def fizzBuzz(n):
    # Write your code here

    for i in range(n):

        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz")
            return

        elif n % 3 == 0:
            print("Fizz")
            return

        elif n % 5 == 0:
            print("Buzz")
            return

        else:
            print(n)
            return


if __name__ == "__main__":
    n = int(input("Input a number: "))

    fizzBuzz(n)
