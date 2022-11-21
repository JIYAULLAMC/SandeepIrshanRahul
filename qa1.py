"""

# 6. Write a program to print alternate characters in a string.

string = "Hello mamta how are you "
# method 1

print(string[: : 2])


string = "Hello mamta how are you "
# method 2

res = ""

for i in range(0,len(string),2):
    res += string[i]


print(res)


string = "Hello mamta how are you "
# method 3

res = ""

for i in range(0,len(string)):
    if i %2 ==0:
        res += string[i]

print(res)


string = "Hello mamta how are you "
# method 4

res = ""

i =0

while i<len(string):
    res += string[i]
    i+=2

print(res)

string = "Hello mamta how are you "
# method 5
res = ""

i =0

while i<len(string):
    if i%2 == 0:
        res += string[i]
    i+=1

print(res)



string = "Hello mamta how are you "
# method 6
res = [string[i] for i in range(len(string))  if i%2==0]
print(res)

out = "".join(res)

print(out)



# 7. Write a Program to print ascii values of the characters present in a string.







# method-1
string = "hello mamta"
res = []
for char in string:
    res.append(ord(char))

print(res)


# method-2

string = "hello mamta"
res = [ord(char) for char in string ]

print(res)


# method-3

def ascii_value(char):
    return ord(char)

string = "hello mamta"
res = [ascii_value(char) for char in string ]

print(res)


# method-4

def ascii_value(char):
    return ord(char)

string = "hello mamta"
res = list(map(ascii_value, string))

print(res)






# method-5

def ascii_value(char):
    return ord(char)

string = "hello mamta"
res = list(map(ascii_value, string))

print(res)


var = ["a", "b", "c", "d", "e", "f", "g", "h","i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


ascii_char_pair = {item:ord(item) for item in var }
asciir_capital_pair = {chr(ord(item)-32): ord(item)-32 for item in var}
all_ascii_value = {**ascii_char_pair, **asciir_capital_pair}

string = "Hi hello mamata"
char_ascii_value_pair={}

for char in string:
    if char== " ":
        continue
    else:
        char_ascii_value_pair[char] =  all_ascii_value[char]
print(char_ascii_value_pair)



# 8. Write a function to convert upper case to lower case and vice-versa without using inbuilt methods.


#method-1

string = "hello How ARe you"
res = ""
diffrence = ord("A") - ord("a")
for i in string:
    if "a"<=i<="z":
        res += chr(ord(i)+diffrence)

    elif "A"<=i<="Z":
        res += chr(ord(i)-diffrence)
    else:
        res += i

print(res)



# method-2
string = "hello How ARe you"

print(string)
res = string.swapcase()
print(res)


#mehod-3
string = "hello How ARe you"
res = ""
def case_converter(char):
    if char.isupper():
        return chr(ord(char) + 32)
    elif char.islower():
        return chr(ord(char)-32)
    else:
        return char

for char in string:
    res += case_converter(char)

print(res)



#method 3

string = "hello How ARe you"
res = ""
def case_converter(char):
    if char.isupper():
        return char.upper()
    elif char.islower():
        return char.lower()
    else:
        return char

for char in string:
    res += case_converter(char)

print(res)


#method-4

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


string = "Helo How MamTa"
res = ""

for char in string:
    if char in lower_case:
        char_index = lower_case.index(char)
        res += upper_case[char_index]

    elif char in upper_case:
        char_index = upper_case.index(char)
        res += lower_case[char_index]
    else:
        res += char

print(res)


string = "Helo How MamTa"



def is_anagram(word1, word2):
    if set(word1) == set(word2):
        return True
    else:
        return False




words= ["listen", "hello", "eat", "desserts", "silent", "peek", "ate", "keep", "tea", "stressed"] 

anagram_words = []
for l_word in words:    
    for r_word in words:
        if r_word == l_word:
            pass
        else:
            if is_anagram(l_word, r_word):
                anagram_words.append((l_word, r_word))

print(anagram_words)









# 9. Write a program to swap two numbers without using the 3rd variable.

#method-1

num1 = 10
num2 = 20

num1, num2 = num2, num1

print(num1)
print(num2)

#method-2

num1 = 10
num2 = 20

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print(num1)
print(num2)


#method-3

num1 = 10
num2 = 20

num1 = num1^num2
num2 = num1^num2
num1 = num1^num2

print(num1)
print(num2)


#method-4

num1 = 10
num2 = 20

num1 = num1*num2
num2 = num1//num2
num1 = num1//num2

print(num1)
print(num2)


#method-5

num1 = 10
num2 = 20

temp = num1
num1 = num2
num2 = temp

print(num1)
print(num2)

"""

#method-6

num1 = 10
num2 = 20

temp = num1
num1 = num2
num2 = temp

print(num1)
print(num2)


# 10. Write a program to merge two different lists.

# list1 = [1,2,3,4]
# list2 = ["a", "b", "c"]
# list3 = list1 + list2
# print(list3)


