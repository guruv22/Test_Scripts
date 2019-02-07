#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    max =0
    for num in set(ar):
        pairs = int((ar.count(num)/2))
        max = max + pairs
    return max

if __name__ == '__main__':

    # n = int(input())
    # ar = list(map(int, input().rstrip().split()))
    n = 10
    ar = [1, 1, 2, 2, 3, 3, 2, 2, 2, 2, 3]
    result = sockMerchant(n, ar)
    print(int(result))

