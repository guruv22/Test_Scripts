#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []
    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))



    arr = [\
            [1, 2, 3, 4, 5, 6],\
            [8, 9, 1, 2, 3, 4],\
            [5, 6, 7, 8, 9, 1],\
            [2, 3, 4, 5, 6, 7],\
            [8, 9, 1, 2, 3, 4],\
            [5, 6, 7, 8, 9, 1]\
            ]

    # print(arr)
    hg_sum_list = []
    hg_sum = 0
    for row_index, row in enumerate(arr):
        if row_index < len(row)-2:
            # print(str(row_index)+":"+str(row))
            for col_index, col in enumerate(row):
                if col_index < len(row) - 2:
                # print(str(col_index)+":"+str(col))
                    hg_sum_list.append(arr[row_index][col_index] + arr[row_index][col_index+1] + arr[row_index][col_index+2] + \
                                       arr[row_index + 1][col_index + 1] + \
                                       arr[row_index + 2][col_index] + arr[row_index + 2][col_index + 1] + arr[row_index + 2][col_index + 2])
                    # print([arr[row_index][col_index],arr[row_index][col_index+1],arr[row_index][col_index+2],\
                    #        arr[row_index+1][col_index+1],\
                    #        arr[row_index+2][col_index],arr[row_index+2][col_index+1],arr[row_index+2][col_index+2]])

print(hg_sum_list)
print(max(hg_sum_list))