# # discripter is class containing __get__ and __set__ method

# class Demo2:

#     def __get__(self, obj, cls):
#         print("this is the discripter demo2 class")
#         return obj._pay

#     def __set__(self, obj, value):
#         print("this is the discripter demo2 set method ")
#         obj.__dict__['_pay'] = value



from validate import StringValidate, NumberValidate



class Employee:
    fname = StringValidate("_fname", min_len= 1, max_len = 100)
    lname = StringValidate("_lname", min_len = 1, max_len = 100)
    pay = NumberValidate("_pay", min_value = 10000, max_value = 50000)
    age = NumberValidate("_age", min_value = 20, max_value = 70)
    def __init__(self, fname, lname, pay, age):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.age = age 


e1 = Employee('steev', 'jobsssand', 10000, 23)


print("-------------------------")
print(e1)
print(e1.__dict__)
print(e1.fname)
print(e1.lname)
print(e1.pay)
print(e1.age)

# discripter attribute
# instance dictionary
# class dictionary
# super class