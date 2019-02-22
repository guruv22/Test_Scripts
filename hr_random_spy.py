import random

n = 7
used_row_list = []
used_col_list = []
exclude_list = []
spy_array = []

def get_rand_int(max_val):
    while True:
        rand_index = random.randint(0, max_val)
        if rand_index not in exclude_list:
            exclude_list.append(rand_index)
            return rand_index

for i in range(n):
    col_arr = []
    for j in range(n):
        col_arr.append('*')
    spy_array.append(col_arr)

for i in range(n):
    ind = get_rand_int(n-1)
    for j in range(n):
        if j == ind:
            spy_array[i][j] = 'S'

print(spy_array)
output_list = []
for row in spy_array:
    for index,col in enumerate(row):
        if col == 'S':
            output_list.append(index+1)
print(" ".join(map(str,output_list)))



