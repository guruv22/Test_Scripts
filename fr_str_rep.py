#!/bin/python3

import math
import os
import random
import re
import sys

def repeatedString(s,n):
    if len(s) == 1:
        if s == 'a':
            return n
        else:
            return 0
    else:
        return(int(n/len(s))*s.count('a'))+s[:n%len(s)].count('a')

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()
    #
    # n = int(input())

    s = "kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm"
    n = 736778906400

    result = repeatedString(s, n)

    print(result)