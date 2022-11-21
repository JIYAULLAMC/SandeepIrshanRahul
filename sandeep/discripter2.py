class Employee:
    def __init__(self, fname, lname,pay, age):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.age = age

    @property
    def fname(self):
        return self._fname

    @fname.setter
    def fname(self, value):
        if not isinstance(value, str):
            raise TypeError("fname should be of type string")
        if len(value)< 5 or len(value)> 10:
            raise ValueError("fname should have 5-10 chrs")
        self._fname = value

    @property
    def lname(self):
        return self._lname

    @lname.setter
    def lname(self, value):
        if not isinstance(value, str):
            raise TypeError("lname should be of type string")
        if len(value)< 5 or len(value)> 10:
            raise ValueError("lname should have 5-10 chrs")
        self._lname = value

    @property
    def pay(self):
        return self._pay

    @pay.setter
    def pay(self, value):
        if not isinstance(value, (int,float)):
            raise TypeError("pay should be of type int or float")
        if value> 5000 or value< 1000:
            raise ValueError("pay should have between 1000-5000 ")
        self._pay = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, (int,float)):
            raise TypeError("age should be of type int or float")
        if value> 50 or value< 10:
            raise ValueError("age should have between 10-50 ")
        self._age = value




e1 = Employee("steve", "jobss", 3000, 20)
print(e1.fname)
print(e1.lname)
print(e1.pay)
print(e1.age)
print(e1.__dict__)