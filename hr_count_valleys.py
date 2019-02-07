#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    val_count = 0
    counter = 0
    in_val = False
    in_mount = False
    for char in s:
        counter = counter + 1 if char == 'U' else counter - 1
        print("Char: {}; In val: {}; counter: {}".format(char,in_val,counter))
        if counter < 0:
            if in_val is False:
                in_val = True
        if counter > 0:
            if in_mount is False:
                in_mount = True
        if counter == 0:
            if in_val:
                val_count = val_count + 1
            in_val = False
            in_mount = False

        print("val count: {}".format(val_count))
    return val_count

if __name__ == '__main__':
    # n = int(input())
    # s = input()
    n = 13
    s = "UDDDUDUU"
    result = countingValleys(n, s)
    print(result)
