class RecordCalls:
    def __init__(self,name, number):
        self.name = name
        self.number = number


    def __call__(self):
        print(f"{self.name} and {self.number}")


s1 = RecordCalls("Manju", 100)

s1()





class RecordCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count +=1
        print(self.count)
        return self.func(*args, **kwargs)


@RecordCalls   #RecordCalls(add())
def add(a,b):
    return a+b

print(add(1,2))

@RecordCalls
def sub(a,b):
    return a-b

print(sub(3,4))




class Get_last_digit:
    def __call__(self, value):
        return value[-1]


g = Get_last_digit()

# def get_last_chr(value):
#     return value[-1]


items = ["aaaa", "cccc", "gggg", "bbbb", "kkkk" ,"dddd"]
# s = sorted(items, key= get_last_chr)
# s = sorted(items, key=lambda item : item[-1])
# s = sorted(items, key=Get_last_digit())
s = sorted(items, key=g)
print(s)

