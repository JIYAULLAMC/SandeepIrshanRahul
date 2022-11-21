class Validate:
    def __init__(self, varname):
        self.varname = varname

    def __get__(self, obj, cls):
        return obj.__dict__[self.varname]

    def __set__(self, obj, value):    
        obj.__dict__[self.varname] = value  # e1.__dict__["_fname"] = "stever"



class StringValidate(Validate):
    def __init__(self, varname,*, min_len, max_len):
        self.min_len = min_len
        self.max_len = max_len
        super().__init__(varname)

    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise TypeError("the fname should be string")
        if len(value)<self.min_len or len(value)>self.max_len:
            raise ValueError("the string len should between 5-10")
        super().__set__(obj,value)

class NumberValidate(Validate):
    def __init__(self, varname, *, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value
        super().__init__(varname)

    def __set__(self, obj, value):
        if not isinstance(value, (int,float)):
                raise TypeError("the should be number")
        if value<self.min_value or value>self.max_value:
            raise ValueError("the pay len should between spedified arange ")
        super().__set__(obj,value)







'''

        if self.varname == "_lname":
            if not isinstance(value, str):
                raise TypeError("the lname should be string")
            if len(value)<5 or len(value)>10:
                raise ValueError("the string len should between 5-10")
    
        if self.varname == "_pay":
            if not isinstance(value, (int,float)):
                raise TypeError("the pay should be number")
            if value<1000 or value>5000:
                raise ValueError("the pay len should between 1000-5000")

        if self.varname == "_age":
            if not isinstance(value, (int,float)):
                raise TypeError("the age should be number")
            if value<10 or value>50:
                raise ValueError("the age len should between 10-50")


'''