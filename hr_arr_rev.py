n = int(input())

arr = list(map(int, input().rstrip().split()))
print(arr)
print(arr[::-1])
str = " ".join(map(str,arr[::-1]))
print(str)