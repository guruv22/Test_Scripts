#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    # print((meal_cost + (tip_percent*int(meal_cost)/100) + (tax_percent*int(meal_cost)/100)))
    print(round(meal_cost + (tip_percent * int(meal_cost) / 100) + (tax_percent * int(meal_cost) / 100)))

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)