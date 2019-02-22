a = [4, 1, 2, 3, 9]
num_swaps = 0
for i in range(len(a) - 1):
    for j in range(len(a) -i -1):
        # print("j".format(j))
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            print(a)
            num_swaps += 1
print("sorted array: {}".format(a))
# print('Array is sorted in {} swaps.'.format(num_swaps))
# print('First Element: {}'.format(a[0]))
# print('Last Element: {}'.format(a[-1]))


for i in range(len(a)):
    print(i)