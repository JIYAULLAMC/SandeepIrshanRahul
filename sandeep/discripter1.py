
class Employee(object):

    def __init__(self, fname, lname, pay, age):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.age = age

    
    def __getattribute__(self, name):
        return super().__getattribute__(name)

    
    def __setattr__(self, name, value):
        if name == "fname" :
            if not isinstance(value, str):
                raise TypeError ("fname should be of type string")
            if len(value)<5 or len(value)>10:
                raise ValueError("fname should be in between 5 to 10 chrs")
        if name == "lname":
            if not isinstance(value, str):
                raise TypeError ("lname should be of type string")
            if len(value)<5 or len(value)>10:
                raise ValueError("lname should be in between 5 to 10 chrs")
                
        if name == "pay":
            if not isinstance(value, (float, int)):
                raise TypeError("pay should be of type int or float")
            if value<1000 or value>5000:
                raise ValueError ("pay should be in between 1000 to 5000")
        if name == "age":
            if not isinstance(value, (float, int)):
                raise TypeError("age should be of type int or float")
            if value<20 or value>50:
                raise ValueError ("pay should be in between 1000 to 5000")
        return super().__setattr__(name, value)

    



e = Employee('stesss', 'jobbs', 3000, 25) # setting the attribute by the setattr method

print("fname->", e.fname)    #getattribute  by getattribute metho
print("lname->", e.lname)
print("pay->", e.pay)
print("age->", e.age)


e1 = Employee("jacob", "yonii", 2000, 28)

print(e.__dict__)
print(e1.__dict__)


# e2 = Employee("musk", "elon", 4000, 28)

# print(e2.__dict__)

# e3 = Employee(3000, 30, "bezoz", "jeff")

# print(e3.__dict__)


