
def fib(max):
    a = 0
    b = 1

    for _ in range(max):
        yield(a)
        c = a+b
        a = b
        b = c
        print ("a={}".format(a))

if __name__ == "__main__":
    print(list(fib(10)))
