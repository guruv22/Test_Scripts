class Findsum(object):
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if isinstance(other.n,int):
            return 100
        # return(self.n + other.n)

obj1 = Findsum(3)
obj2 = Findsum(2)
# print(5+5)
print(obj1+obj2)

