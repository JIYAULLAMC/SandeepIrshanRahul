


class MyIter:
    def __iter__(self):
        self.num = 0 
        return self

    def __next__(self):
        num = self.num
        self.num +=2
        return num


out = MyIter()

iter(out)

print(next(out))
print(next(out))
print(next(out))
print(next(out))