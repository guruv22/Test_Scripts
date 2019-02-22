import math

num = int(input())
for num_ip in range(num):
    n = int(input())
    if (n == 1):
        print ("Not prime")
    elif (n == 2):
        print ("Prime")
    else:
        sq_rt = math.ceil(math.sqrt(n))
        for i in range(2, sq_rt+1):
            # print("sq rt: {};i: {}".format(sq_rt,i))
            if (n % i is 0):
                print("Not prime")
                break
        else:
            print("Prime")