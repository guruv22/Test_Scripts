class singleton():
    _instance = None
    def __new__(cls, a, b):
        if not cls._instance:
            cls._instance = super(singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, a, b):
        self.a = a
        self.b = b

if __name__ == '__main__':
    obj1 = singleton(2,3)
    obj2 = singleton(4,5)
    obj3 = singleton(6,7)
    print ("{},{},{}".format(obj1, obj1.a, obj1.b))
    print ("{},{},{}".format(obj2, obj2.a, obj2.b))
    print("{},{},{}".format(obj1, obj1.a, obj1.b))
    print ("{},{},{}".format(obj1, obj1.a, obj1.b))
    print ("{},{},{}".format(obj3, obj3.a, obj3.b))
    print("{},{},{}".format(obj2, obj2.a, obj2.b))



