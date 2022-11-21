
from re import findall
with open("C:\\Users\\JiyaUlla\Desktop\\pythonfiles\\myfolder\\text.txt") as fileobj:
    count = 0
    for line in fileobj:
        mathes = findall(r"\b[0-9]+\b",line)
        print(mathes)
        count += len(mathes)



print(count)
