



















"""
# A1B
# C2D
# E3F


n = 8
value1 = ord("A")
value2 = 1
for i in range(n):
    for j in range(n):
        if j%2==1:
            print(value2, end=" ")
            value2 = value2 +1
            if value2>9:
                value2= 1
        else:
            print(chr(value1), end=" ")
            value1 +=1
            if value1 > ord("Z"):
                value1 = ord("A")
    print()



*
* *
* * *
* * * *
* * * 
* *
*

     
n = 4
for i in range(1,n):
    print("* "*i)

for j in range(n, 0,-1):
    print("* "*j)



*******
 *****
  ***
   *

n = 10
stars = 2*n-1
space = 0

for i in range(n):
    for j in range(space):
        print(" ", end=" ")


    for j in range(stars):
        print("*", end=" ")

    print()
    stars = stars -2
    space = space+1
        



    *
   **
 ****
*****
 ****
  ***
   **
    *



n = 7
spaces =n
stars =1

for i in range(n):
    for j in range(spaces):
        print(" ", end=" ")
    for k in range(stars):
        print("*", end=" ")
    print()
    spaces = spaces -1
    stars = stars + 1


spaces =1
stars =n 

for i in range(n):
    for j in range(spaces):
        print(" ", end=" ")
    for k in range(stars):
        print("*", end=" ")
    print()
    spaces = spaces +1
    stars = stars - 1

"""








'''



string = "Hi Hello How Are"
res = string.swapcase()

print(res)






n = 5

for i in range(n):
    for j in range(n):
        if j==0 or i==j or j==n-1:
            print("*", end=" ")
        else:
            print(" ", end= " ")
    print()



n = 5
stars = 1
space = n-1
value =1

for i in range(n):
    value = 0
    for j in range(space):
        print(" ", end= " ")
    for k in range(stars):
        print(value, end=" ")
        value +=1
        if value>9:
            value = 0

    print()
    space -=1
    stars +=2






n = 5
stars = 1
space = n-1
value =1

for i in range(n):
    value = 0
    for j in range(space):
        print(" ", end= " ")
    for k in range(stars):
        print(value, end=" ")
        value +=1
        if value>9:
            value = 0

    print()
    space -=1
    stars +=2
    




n = 5
stars = 1
space = n-1
value =1

for i in range(n):
    for j in range(space):
        print(" ", end= " ")
    for k in range(stars):
        print(value, end=" ")
        value +=1
        if value>9:
            value = 0

    print()
    space -=1
    stars +=2
    value +=1
    if value>9:
        value = 0




n = 5
stars = 1
space = n-1
value =1

for i in range(n):
    for j in range(space):
        print(" ", end= " ")
    for k in range(stars):
        print(value, end=" ")

    print()
    space -=1
    stars +=2
    value +=1
    if value>9:
        value = 0









n = 5
n = 2*n -1

for i in range(n):
    for j in range(n):
        if i>=j and i+j>=n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()



n = 5
stars = 1
space = n-1

for i in range(n):
    for j in range(space):
        print(" ", end= " ")
    for k in range(stars):
        print("*", end=" ")

    print()
    space -=1
    stars +=2





'''