




n = 4
value = 1
for i in range(0, n):
    if i%2 == 0:
        for j in range(1, n+1):
            print("*", end=" ")
        print()
    else:
        for j in range(1,n+1):
            print(value, end=" ")
        value +=1
        print()




'''
n = 5

for i in range(1,n+1):
    print("  "*(n-i)+"* "*i)




n = 5

for i in range(1,n+1):
    print("  "*(n-i)+"* "*i)

n = 5

for i in range(1,n+1):
    print("* "*i)



n = 5

value = ord("A")

for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print(chr(value), end=" ")
            value += 1
        else:
            print(" ", end=" ")      
        if value> ord("Z"):
            value = ord("A")

    print()


n = 5

value = ord("A")

for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print(chr(value), end=" ")
            value += 1
        else:
            print(" ", end=" ")      
        if value> ord("Z"):
            value = ord("A")

    print()



n = 5

for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()



n = 5

for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()




n = 5

i = 0
while i<n:
    j=0
    while j<n:
        print("*", end=" ")
        j+=1
    print()
    i+=1

n = 8


value = ord('A') 
if value >ord("Z"):
    value = ord('A')

for i in range(n):
    for j in range(n):
        if i+j == n:
            print(chr(value), end=" ")
        else:
            print(" ", end=" ")
    value -=1
    if value<=ord("A"):
        value=ord("Z")
    print()
n = 16


n = 30


value = ord('A') 
if value >ord("Z"):
    value = ord('A')

for i in range(n):
    for j in range(n):
        if i+j == n-1:
            print(chr(value), end=" ")
        else:
            print(" ", end=" ")
    value +=1
    if value>=ord("Z")+1:
        value=ord("A")
    print()




n = 16

value = 15
if value >9:
    value = 0

for i in range(n):
    for j in range(n):
        if i+j == n-1:
            print(value, end=" ")
        else:
            print(" ", end=" ")
    value +=1
    if value>=9:
        value=0
    print()


n = 8

for i in range(n):
    for j in range(n):
        if i+j <= n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()




n = 8

for i in range(n):
    for j in range(n):
        if i+j >= n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()




# 1
# 22
# 333
# 4444



n = 15

value = 1

for i in range(n):
    for  j in range(n):
        if i>=j:
            print(value, end=" ")
        else:
            print(" ", end=" ")
    
    value = value +1
    if value>9:
        value = 1
    print()



# A
# BB
# CCC
# DDDD


n = 30

value = ord("A")

for i in range(n):
    for j in range(n):
        if i>=j:
            print(chr(value), end=" ")
        else:
            print(" ", end= " ")
    print()
    value = value +1
    if value > ord('Z'):
        value = ord('A')



# 1
# 12
# 123
# 1234




n = 15
value = 0
for i in range(n):
    value = 0
    for j in range(n):
        if i>=j:
            print(value, end=" ")
        else:
            print(" ", end=" ")

        value = value+ 1
        if value >9:
            value = 0
    print()


# a
# ab
# abc
# abcd



# 3
# 22
# 111




n = 17
if n>9:
    value = 9 
for i in range(n):
    for j in range(n):
        if i>=j:
            print(value, end=" ")
        else:
            print(" ", end=" ")

    value = value -1
    if value < 0:
        value = 9
    print()




# c
# bb
# aaa




n = 30
value = ord("A") + n -1
if value > ord("Z"):
    value = ord("Z")

for i in range(n):
    for j in range(n):
        if i>=j:
            print(chr(value), end=" ")
        else:
            print(" ", end=" ")
    value = value -1

    if value < ord("A"):
        value = ord("Z")
    print()


# a 
#  b
#   c
#    d





n = 30

value = ord("A") + n -1

if ord("A") + n -1 > ord("Z"):
    value = ord("A")

for i in range(n):
    for j in range(n):
        if i==j:
            print(chr(value), end=" ")
        else:
            print(" ", end=" ")
    value = value + 1

    if value > ord("Z"):
        value = ord("A")
    print()


# d
#  c
#   b
#    a






n = 10

for i in range(n):
    for j in range(n):
        if i<=j :
            print("*", end=" ")

        else:
            print(" ", end=" ")
    print()

n = 10

for i in range(n):
    for j in range(n):
        if i>=j :
            print("*", end=" ")

        else:
            print(" ", end=" ")
    print()


n = 10

for i in range(n):
    for j in range(n):
        if i==j :
            print("*", end=" ")

        else:
            print(" ", end=" ")
    print()



row = 5
value = ord('A') + row -1
if value> ord('Z'):
    value = ord('Z')

for i in range(row):
    for j in range(col):
        print(chr(value), end=" ")  
    print()

    value = value -1
    if value <ord("A"):
        value = ord("Z")



row = 8
value = row
if value > ord('A'):
    value = ord("Z")
else:
    value = ord('A')+row -1


for i in range(row):
    for j in range(col):
        print(chr(value), end=" ")
    print()
    value = value-1
    if value< ord('A'):
        value = ord('Z')




row = 8
val = row
if val>9:
    val = 9

for i in range(row):
    for j in range(col):
        print(val, end=" ")
    print()
    val= val-1
    if val<0:
        val = 9
'''