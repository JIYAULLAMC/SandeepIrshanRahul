def log(func):
    def wrapper(*args):
        print("+++++++++++++++++++++++")
        print("---------------")
        res = func(*args)
        return res
    return wrapper


@log
def demo(a,b):
    return a+b

print(demo(1,2))

@log
def demo1(a,b):
    return a+b

print(demo1(1,2))

@log
def demo2(a,b):
    return a+b

print(demo2(1,2))

@log
def demo3(a,b):
    return a+b

print(demo3(1,2))