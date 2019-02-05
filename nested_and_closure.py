def do_op(func, num):
    print ('came to do_op with func name: {}'.format(func.__name__))
    def inner(x):
        print('came to inner function with num={} and x={}'.format(num,x))
        return(func(num,x))
    return inner

def mul(num,multiplier):
    print('came to multiplier function')
    return (num * multiplier)

def div(num,divisor):
    print('came to divider function')
    return (num / divisor)

if __name__ == '__main__':
    mul_op = do_op(mul,8)
    print("Point 1:{}".format(mul_op.__name__))
    print (mul_op(2))

    div_op = do_op(div,8)
    print("Point 1:{}".format(mul_op.__name__))
    print(div_op(2))