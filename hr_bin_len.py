#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    num_ones_set = {len(x) for x in re.findall("1+", str(bin(n)))}
    print(max(num_ones_set))

