# a = "abc"
# b = "abc"
# print(a)
# print(b)
# print(id(a))
# print(id(b))
# print("----------------")
# # print(id(a+"x"))
# # print(id(b+"x"))
#
# print(a+"x")
# print(b+"x")
# print(id(a+"x"))
# print(id(b+"x"))

# print(id(a+"x"))
# print(id(b+"x"))


# a = "abc"
# b = "abc"
#
# # print(a+"x")
# # print(b+"x")
# # print(a+"x" == b+"x")
# # print(a+"x" is b+"x")
# print(a)
# print(b)
# print(id(a))
# print(id(b))
# print(a == b)
# print(a is b)
# print("----------------")
# # print(id(a+"x"))
# # print(id(b+"x"))
#
# print(a+"x")
# print(b+"x")
# print(id(a+"x"))
# print(id(b+"x"))




# i = 4
# d = 4.0
# s = 'HackerRank '
# # Declare second integer, double, and String variables.
# j = input("Enter integer: ")
# e = input("Enter float: ")
# t = input("Enter string: ")
# print(i+int(j))
# print(round((d+float(e)),2))
# print(s+t)


# Read and save an integer, double, and String to your variables.

# Print the sum of both integer variables on a new line.

# Print the sum of the double variables on a new line.

# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.



# #!/bin/python3
#
# import math
# import os
# import random
# import re
# import sys
#
#
# if __name__ == '__main__':
#     n = int(input())
#     for i in range(1,11):
#         print("{} x {} = {}".format(n, i, n*i))

# import string
# a = list(string.ascii_lowercase)
# b = "how are you"
#
# # print(set(list(a)))
# out_list = set(a) - set(list(b))
# # print(''.join(out_list))
#
# x = set(list(b))
# y = list(b)
#
# # x[0] = 'a'
# y[0] = 'a'
# print (y[0])

# str = "abcdef"
# print(str[::-1])
#
#
# a = ['a', 'b', 'c']
# print(''.join(a))


# str=input("Enter the string:\n")
# print("{} {}".format(str[::2],str[1::2]))

# class Demo:
#     def __new__(cls):
#         print("Demo's __new__() invoked")
#         return super(Demo,cls).__new__(cls)
#
#     def __init__(self):
#         print("Demo's __init__() invoked")
#
# class Derived_Demo(Demo):
#     def __new__(cls):
#         print("Derived_Demo's __new__() invoked")
#         return super(Derived_Demo,cls).__new__(cls)
#
#     def __init__(self):
#         print("Derived_Demo's __init__() invoked")
#
# obj1 = Derived_Demo()
# obj2 = Demo()


# def getMoneySpent(keyboards, drives, b):
#     #
#     # Write your code here.
#     #
#     max_amt = 0
#
#     for kb in keyboards:
#         for dr in drives:
#             tot = kb + dr
#             if tot > max_amt and tot <= b:
#                 max_amt = tot
#
#     if max_amt == 0:
#         return -1
#     else:
#         return max_amt
#
#
# if __name__ == '__main__':
#     b = 10
#
#     n = 2
#
#     m = 3
#
#     keyboards = [3, 1]
#
#     drives = [5, 2, 8]
#
#     #
#     # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
#     #
#
#     moneySpent = getMoneySpent(keyboards, drives, b)
#     print(moneySpent)


#!/bin/python3

import sys

# n = int(input().strip())
# a = list(map(int, input().strip().split(' ')))

