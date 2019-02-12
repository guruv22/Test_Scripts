import re

str = "sjfgkj010101986756201010kdgj101010101dgkjhkgd101010hgggj"
# str = "a1010d"
found_0 = 0
found_0_prev = 0
found_1 = 0
found_0_prev = 0
pat_repeat = 0
list_of_substr = []
for i,s in enumerate(str):
    # print("s: {}; found_0: {}; found_1: {}; pat_repeat: {}".format(s,found_0,found_1,pat_repeat))
    if s == '1':
        found_1 = 1
        if str[i-1] == 1:
            pass
        if pat_repeat == 0:
            pat_repeat = 1
            continue
        if found_0 > 0 and pat_repeat > 0:
            pat_repeat = pat_repeat + 1
    elif s == '0':
        found_0 = 1
        if pat_repeat == 0:
            pat_repeat = 1
            continue
        if found_1 > 0 and pat_repeat > 0:
            pat_repeat = pat_repeat + 1
    else:
        found_1 = 0
        found_0 = 0
        if pat_repeat > 0:
            list_of_substr.append(pat_repeat)
            pat_repeat = 0
            
# print(list_of_substr)
# print(max(list_of_substr))


match = re.findall(r'[1+0+1+]+',str)
print((match))
