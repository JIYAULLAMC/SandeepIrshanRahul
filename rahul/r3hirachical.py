# two child classess one parent class
class Persone:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def work(self):
        print("yes we will work ")

class Stuent(Persone):  
    def __init__(self,name,age, fees):
        Persone.__init__(self,name, age)
        self.fees = fees

    def study(self):
        print("yes we will study ")


class Teacher(Persone):  
    def __init__(self,name, age,salary):
        Persone.__init__(self,name, age)
        self.salary = salary

    def tech(self):
        print("yes we will tech ")

s1 = Stuent("mamata", 20, 1200)
t1 = Teacher("mohamad", 30, 300)

print(s1.study())   # method from student class
print(s1.work())   # method from person class
print(s1.name)   # state from person calss
print(s1.age)    #  state from person class
print(s1.fees)   # state from student class

print(t1.tech())   # method from techer class
print(t1.work())   # method from person class
print(t1.name)   # state from person calss
print(t1.age)    #  state from person class
print(t1.salary)   # state from techer class
