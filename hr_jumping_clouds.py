#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
# def jumpingOnClouds(c):
#     num_hops = 0
#     index = 0
#     while index <= len(c)-2:
#         print("Index: {}".format(index))
#         if c[index + 1] == 0:
#             if (c[index + 2]) and c[index + 2] == 0:
#                 index = index + 2
#             else:
#                 index = index + 1
#             num_hops = num_hops + 1
#         else:
#             index = index + 2
#             num_hops = num_hops + 1
#         print("Num hops: {}".format(num_hops))
#     return num_hops

def jumpingOnClouds(c):
    num_hops = 0
    in_hop = False
    prev1 = -1
    prev2 = -2
    for index in range(len(c)):
        print("Index: {}; val: {}".format(index,c[index]))
        print("Prev index: {}".format(prev1))
        print("Num hops: {}".format(num_hops))
        print("In hop: {}".format(in_hop))

        if c[index] == 0:
            if prev1 != -1:
                if c[prev1] == 0:
                    if in_hop is True:
                        in_hop = False
                    else:
                        in_hop = True
                        num_hops = num_hops+1
                else:
                    num_hops = num_hops + 1
                    in_hop =False
        prev1 = prev1 + 1

    return num_hops


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # n = int(input())
    #
    # c = list(map(int, input().rstrip().split()))

    c = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
    result = jumpingOnClouds(c)
    print(result)
