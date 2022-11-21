

inp = [ 1023, 1007,    10872, 26561565656, 2323 ]
# out [4, 4, 5]


# res = []
# for i in inp:
#     res.append(len(str(i)))

# print(res)

# res = []
# for num in inp:
#     count = 0
#     flag = True
#     while flag:
#         count +=1
#         num = num//10
#         if num == 0:
#             flag = False
#     res += [count]
# print(res)




num = 125420
even_count = 0
odd_count = 0
zero_count = 0
for digit in str(num):
    if int(digit) %2 == 0:
        even_count +=1
    elif int(digit) %2 ==1:
        odd_count +=1
    else:
        zero_count +=1

print(even_count, end=" ")
print(odd_count, end=" ")
print(zero_count, end=" ")

print()

even_count = 0
odd_count = 0
zero_count = 0

num = 32432423324
while num:
    rem = num%10
    if rem %2 == 0:
        even_count +=1

    elif rem%2 ==1:
        odd_count +=1
    else:
        zero_count +=1
    num = num//10
print(even_count, end=" ")
print(odd_count, end=" ")
print(zero_count, end=" ")



even_count = 0
odd_count = 0
zero_count = 0

num = 32432423324
while num:
    rem = num%10
    if rem %2 == 0:
        even_count +=1

    elif rem%2 ==1:
        odd_count +=1
    else:
        zero_count +=1
    num = num//10
print(even_count, end=" ")
print(odd_count, end=" ")
print(zero_count, end=" ")


num = input("Enterr number: ")

print(num)