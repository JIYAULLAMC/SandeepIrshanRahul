# pattern programming
'''
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 


row = 5
col = 5

for i in range(row):
    for j in range(col):
        print("*", end=" ")
    print()


# 1 1 1 1 1 1 1 
# 2 2 2 2 2 2 2 
# 3 3 3 3 3 3 3 
# 4 4 4 4 4 4 4 
# 5 5 5 5 5 5 5 
# 6 6 6 6 6 6 6 
# 7 7 7 7 7 7 7 



row = 7
col = 7


val = 1
for i in range(1,row+1):
    for j in range(1, col+1):
        print(val, end=" ")
    print()
    val +=1
    if val>9:
        val = 1

# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 


row = 5
col = 5


for i in range(1,row+1):
    val = 1
    for j in range(1, col+1):
        print(val, end=" ")
        val = val +1
        if val>9:
            val = 1
    print()


# A A A A A 
# B B B B B 
# C C C C C 
# D D D D D 
# E E E E E 


row = 5
col = 5

val = ord("A")
for i in range(1,row+1):    
    for j in range(1, col+1):
        print(chr(val), end=" ")
    print()
    val +=1
    if val>ord("Z"):
        val = ord("A")


# A B C D E 
# A B C D E 
# A B C D E 
# A B C D E 
# A B C D E 

row = 5
col = 5

for i in range(1,row+1):    
    val = ord("A")
    for j in range(1, col+1):
        print(chr(val), end=" ")
        val +=1
        if val>ord("Z"):
            val = ord("A")
    print()
   



row = 7
col = 7


val = row
for i in range(1,row+1):
    for j in range(1, col+1):
        print(val, end=" ")
    print()
    val -= 1
   


print("*"*20)

row = 7
col = 7


for i in range(1,row+1):
    val = col    
    for j in range(1, col+1):
        print(val, end=" ")
        val -=1
    print()
   
   

'''



row = 5
col = 5

val = ord('z')
for i in range(1,row+1):

    for j in range(1, col+1):
        print(chr(val), end=" ")
    print()
    val -=1

print("-"*15)
row = 5
col = 5

for i in range(1,row+1):
    val = ord('z')
    for j in range(1, col+1):
        print(chr(val), end=" ")
        val -=1
    print()
   
   


