# has a relation ship
'''
creating the object of one class inside another class is known as has a relation ship
'''


class One:
    def __init__(self):
        self.a1 = 10
        self.b1 = 20

    def m1(self):
        print("i am m1 method of class One ")


class Two:
    def __init__(self):
        self.a2 = 100
        self.b2 = 200
        # creating object for class one
        self.o1 = One()

    def m2(self):
        print("i am m2 method of class Two")


t1 = Two()



'''
> t1.a2
100
>>> t1.b2
200
>>> t1.o1
<__main__.One object at 0x000002A1C7410C40>
>>> t1.m2
<bound method Two.m2 of <__main__.Two object at 0x000002A1C73CD100>>
>>> t1.m2()
i am m2 method of class Two
>>> t1.o1.a1
10
>>> t1.o1.b1
20
>>> t1.o1.m1()
i am m1 method of class One
>>>


'''