from re import findall, finditer

#print the line if the line is start and ends with the same word
sentence1 = "hi this is hello world how are you hi"
sentence2 = "hi this is hello world how are you hello"


matches1 = findall(r"(hi)$", sentence1)
matches2 = findall(r"^(hi)", sentence1)
matches = findall(r"^(hi)\s.*\1$",sentence1)

print(matches1)
print(matches2)

print("*"*20)
print(matches)

if True:
    print("helo")
    for i in range(10):
        print("hi")
        print("wow")




        









