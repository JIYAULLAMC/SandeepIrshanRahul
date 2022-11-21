
"""
# 1. Write a program to find the length of the string without using inbuilt function (len) 

#method-1
#by using built in function
print(len(string))

#method-2
#using for loop

length = 0
for char in string:
    length +=1

print(f"the length of string {string} is {length}")

#method-3
string = "hi hello mamata"

i = 0
while True:
    try:
        if string[i] :
            i +=1

    except IndexError:
        break
print(f"the length of string {string} is {i}")

#method-4
string = "hi hello world"

last_char = string[-1]
print(string.rfind(last_char)+1)




# 2. Write a program to reverse a string without using any inbuilt functions.

#method-1

string = "Hello Mamata"
res = reversed(string)



# method 2
string = "Hello Mamata"

res = ""
for char in string:
    res = char + res

print(res)



#method -3
string = "Hello Mamata"

res = ""
i = 0
while i<len(string):
    res = string[i] + res
    i+=1

print(res)


# method-4

string = "Hello Mamata"
res = string[: :-1]
print(res)



# method-5

string = "Hello Mamata"
count = 0
def index_of(item):
    global count
    count = count +1 
    return count-1

res = sorted(string, key= lambda item : index_of(item), reverse=True )
out = "".join(res)

print(out)



from functools import reduce


string = "Hello Mamata"
def func(a,b):
    return b+a

res = reduce(func, string)
print(res)


l1 = [1,2,3]
l2 = [3,4,5,5]

r1 = l1 + l2
print(r1)

print("1")
l1 = [1,2,3]
l2 = [3,4,5,5]
r2 = list(l1) + list(l2)
print(r2)

print("2")
l1 = [1,2,3]
l2 = [3,4,5,5]
l1.extend(l2)
print(l1)

print("3")
l1 = [1,2,3]
l2 = [3,4,5,5]
l2.extend(l1)
print(l2)


print("4")
l1 = [1,2,3]
l2 = [3,4,5,5]
res = [*l1, *l2]
print(res)

print("5")
l1 = [1,2,3]
l2 = [3,4,5,5]
res = [*l2, *l1]
print(res)

print("5")
l1 = [1,2,3]
l2 = [3,4,5,5]
res = []
for i in l1:
    res.append(i)

for j in l2:
    res.append(j)
print(res)


print("6")
l1 = [1,2,3]
l2 = [3,4,5,5]
res = []
for i in l1:
    res.insert(len(res),i)

for j in l2:
    res.insert(len(res), j)
print(res)


print("7")
l1 = [1,2,3]
l2 = [3,4,5,5]
res = []
for i in l1:
    res.insert(len(res),i)

for j in l2:
    res.insert(len(res), j)
print(res)

print("7")
l1 = [1,2,3, 6]
l2 = [3,4,5,5]
res = []
for i in l1:
    res += [i]

for j in l2:
    res += [j]
print(res)


print("8")
l1 = [1,2,3,6]
l2 = [3,4,5,5]
res = []
for i,j in zip(l1,l2):
    res += [i] + [j]
    # res += [i,j]

print(res)


print("9")
l1 = [1,2,3,6]
l2 = [3,4,5,5]
res = []
for i in range(0,len(l1)):
    res += [l1[i], l2[i]]
print(res)

print("10")
l1 = [1,2,3,6]
l2 = [3,4,5,5]
res = []
i = 0
while i<len(l1):
    res = res + [l1[i]]
    i +=1
i = 0
while i<len(l2):
    res = res + [l2[i]]
    i +=1

print(res)


#method11

l1 = [1,2,4]
l2 = [1,2,3,4,4]

res = list(*l1, *l2)
print(res)

# 3. Write a program to replace one string with another. e.g. "Hello World" replaces "world" with "Universe".

# method-1

string = "Hello World"

res = string[0:6] + "Universe"
print(res)


# method-2

string = "Hello World"

res =  string.replace("World", "Universe")
print(res)

# method-3

string = "Hello World"

words = string.split()
repl_list = [word if word !="World" else "Universe" for word in words  ]
res = " ".join(repl_list)

print(res)


# method-4
from re import sub

string = "Hello World"
res = sub("World", "Universe",string)

print(res)

# 4. How to convert a string to a list and vice-versa.


# to list




#method-1
string = "Hello World"
list_res = list(string)

print(list_res)

string_res = "".join(list_res)
print(string_res)


#method-2
string = "Hello World"

li = []
for char in string:
    li += [char]


print(li)

res = ""

for char in li:
    res += char

print(res)


#method-3
string = "Hello World"

li = []
i = 0
while i<len(string):
    li += [string[i]]
    i+=1

print(li)

res = ""

i = 0
while i<len(li):
    res += li[i]
    i+=1

print("res",res)



#method-4

from re import findall

string = "Hello World"

res = findall(r"[\d\w\s]", string) 

print(res)

string_res = "".join(res)

print(string_res)



#method-5

string = "Hello World"
res = [*string]
print(res)
string_res = "".join(res)
print(string_res)



# 5. Convert the string "Hello welcome to Python" to a comma separated string.


#method-1

string = "Hello wellcome to Python"

list_res = string.split(" ")
print(list_res)
string_res = ",".join(list_res)
print(string_res)




#method-2

string = "Hello wellcome to Python"
res  = string.replace(" ", ",")
print(res)


#method-3

from re import sub

string = "Hello wellcome to Python"
words = sub(" ", ",", string)
print(words)



#method-4

from re import sub

string = "Hello wellcome to Python"

res = ""
for i in string:
    if i  == " ":
        res += ","
    else:
        res += i

print(res)



#method-5

string = "Hello wellcome to Python"
res = []
word = ""
for char in string:
    if char ==" ":
        res.append(word)
        word = ""
    else:
        word += char

print(res)
out = ""
for word in res:
    out += word + ","
print(out)

#method-6

string = "Hello wellcome to Python"

print(string)
res =""
i = 0
while i<len(string):
    if string[i] == " ":
        res += ","
    else:
        res += string[i]
    i +=1

print(res)



#method-7

from re import findall
string = "Hello wellcome to Python"

print(string)

chars = findall(r"[a-zA-Z\s]", string)

print(chars)

res = ""
for char in chars:

    if char is " ":
        res += ","
    else:
        res += char

print(res)

"""