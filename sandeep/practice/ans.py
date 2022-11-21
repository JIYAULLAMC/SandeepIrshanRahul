# 1. Write a program to find the length of the string without using inbuilt function (len) 

string = "hello"

length = 0
for i in string:
    length +=1
print(length)


# 2. Write a program to reverse a string without using any inbuilt functions.

string = "hello"

res = ""
for ch in string:
    res = ch + res
print(res)


# 3. Write a program to replace one string with another. e.g. "Hello World" replaces "world" with "Universe".

string = "Hello World"
res = string[: 6] + "Universe"
print(res)


# 4. How to convert a string to a list and vice-versa.

string = "hello"
print(string)
# to list
list1 = list(string)
print(list1)

#to string
string1 = "".join(list1)
print(string1)

# 5. Convert the string "Hello welcome to Python" to a comma separated string.

string = "Hello wellcome to Python"
words = string.split()
res = ",".join(words)
print(res)

# 6. Write a program to print alternate characters in a string.

string = "Hello mamta how are you "

print(string[: : 2])

# 7. Write a Program to print ascii values of the characters present in a string.

string = "hello mamta"
for i in string:
    if i==" ":
        continue
    else:
        print(ord(i))


# 8. Write a function to convert upper case to lower case and vice-versa without using inbuilt methods.



string = "hello How ARe you"
res = ""
diffrence = ord("A") - ord("a")
print(diffrence)
for i in string:
    if "a"<=i<="z":
        res += chr(ord(i)+diffrence)

    elif "A"<=i<="Z":
        res += chr(ord(i)-diffrence)
    else:
        res += i

print(res)

# 9. Write a program to swap two numbers without using the 3rd variable.

num1 = 10
num2 = 45

num1 = num1+ num2
num2 = num1-num2
num1 = num1 - num2
print(num1)
print(num2)
# 10. Write a program to merge two different lists.

list1 = [1,2,3,4]
list2 = ["a", "b", "c"]
list3 = list1 + list2
print(list3)



# *11. Write a program to read a random line in a file. (ex. 50, 65, 78th Line)

from platform import java_ver
import random
file_data = []
with open(r"C:\Users\JiyaUlla\Desktop\python\sandeep\mytext.txt", 'r') as r_obj:
    for line in r_obj:
        file_data.append(line)

random_line = random.choice(file_data)
print(random_line)


# **12. Write a program to read random lines in a file. (ex. I want read all lines 18th to 15th Line)

import random
file_data = []
with open(r"C:\Users\JiyaUlla\Desktop\python\sandeep\mytext.txt", 'r') as r_obj:
    for line in r_obj:
        file_data.append(line)

random_line = random.choices(file_data, k=2)
print(random_line)


# **13 Program to print the last "N" lines of a file.


file_data = []
with open(r"C:\Users\JiyaUlla\Desktop\python\sandeep\mytext.txt", 'r') as r_obj:
    for line in r_obj:
        file_data.append(line)

last = 3
start_point = len(file_data)-3
for index, line in enumerate(file_data, start=1):
    if index>start_point:
        print(line)



# **14. Write a program to check if the given string is Palindrome or not without using reversed method.


given_str = "aba"
res = ""
for ch in given_str:
    res = ch + res


if given_str == res:
    print("palindrom string ")
else:
    print("not a palindrome string ")

# **15 write a program to search for a character in a given string and return the corresponding index.


given_string = "hello mamata"
ch = "m"
for i in range(len(given_string)):
    if ch == given_string[i]:
        print(i)



# 6. Write a program to get the below output

from collections import defaultdict
from platform import java_ver 
sentence = "hello world welcome to python programming hi there"

# ={'h': ['hello', 'hi'], 'w': ['world', 'welcome'], 't': ['to', 'there'], 'p': ['python', 'programming'] }

res = defaultdict(list)
words = sentence.split()

for word in words :
    res[word[0]] = res[word[0]] + [word]
print(res)

# *17 Write a to replace all the characters with - if the character occurs more than once in a stringes **python

string = 'hellohai' 
# 0/P should be '-e--o-ai'

res = ""
for ch in string:
    if string.count(ch)>1:
        res = res + "-"
    else:
        res = res + ch

print(res)

# 18 write a decorator that returns only positive values of subtraction

def return_positive(func):
    def wrapper(num1,num2):
        res  = func(num1,num2)
        return abs(res)
    return wrapper

@return_positive
def sub(a,b):
    return a-b

print(sub(10,20))


# 20 Write a function which takes a list of strings and integers. If the item is a string it should print as is and if he item is integer or float it should reverse it.

list1 = ["abcd", 1.23, "dsgsdf", 23, 78923, "mamata"]

for item in list1:
    if isinstance(item, str):
        print(item)
    elif isinstance(item, (int, float)):
        value = str(item)
        up_value = value[: :-1]
        print(float(up_value)) 
    
# 22 Write a Custom class which can access the values of dictionaries using d['a'] and d.a


class Mydict:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getattribute__(self, name):
        return super().__getattribute__(name)

    def __getitem__(self, name):
        if name == "name":
            return self.name
    
d = Mydict("mamata", 10)


print(d.name)
print(d["name"])


# 23 Write a python program to get the below outputes

sentence = "Hi How are you"
# o/p should be "iH wohl era uoy"

words = sentence.split()
res = ""
for word in words:
    res = res + word[: :-1] + " "
print(res)
    

# 24 Write a python program to get the below outputes
# entence = "Hi How are you" p should be "ouy era woh iH"

sentence = "Hi How are you"
# o/p should be "iH wohl era uoy"

words = sentence.split()
res = ""
for word in words:
    res = word[: :-1] + " " + res
print(res)

# 25 Write a Lambda function to add two numbers (a, b)
add = lambda a, b: a+b

print(add(1,2))

# 26 What is the output of the followinges

a= [1, 2, 3]

b = [4, 5, 6] 
# print(int([a, b])) -# type error
# print(int((a, b)))  # type error

# 27 How to remove duplicates from the list without using inbuilt functions 
items = [1, 2, 3, 4, 1, 2, 3, 4, 5]
print(list(set(items)))


# 28 Find the longest word in the sentences 
sentence = "Hello world. Welcome to Python"
words = sentence.split()

max_word = words[0]
for word in words:
    if len(word)>len(max_word):
        max_word = word
print(max_word)



# 29 write a program to reverse the values in the dictionary if the value is of type Strings 
# 
d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}

for key,value in d.items():
    if  isinstance(value, str):
        d[key] = value[: :-1]
print(d)

# 31 How to get the elements that are in list b but not in list as

a= [1, 2, 3] 
b= [1, 2, 3, 4]

res = []
for item in b:
    if item not in a:
        res = res + [item]

print(res)



# 32 A function takes variable number of positional arguments as input. How to check if the arguments that are passed is more than 5


def greater_five(*args):
    if len(args) >5:
            return "contain items greater than 5"
    
    else:
        return "items are less than 5"


print(greater_five(1,2,3,4,))
print(greater_five(1,2,3,4,5,6))



# 33 Count the number of occurrences of "CRITICAL", "INFO" and "ERROR" Lines in a log file. python Assume Below is the contents of the log file

no_critical_lines = no_info_lines = no_error_lines= no_other_lines = 0

with open(r"C:\Users\JiyaUlla\Desktop\python\sandeep\examdata.txt") as r_obj:
    for line in r_obj:
        clean_line = line.split(":")
        if clean_line[0] == "CRITICAL":
            no_critical_lines +=1
        elif clean_line[0] == "INFO":
            no_info_lines +=1
        elif clean_line[0] == "ERROR":
            no_error_lines +=1
        else:
            no_other_lines +=1

print(f"no_other_lines{no_other_lines}  no_critical_lines {no_critical_lines}, no_info_lines {no_info_lines}, no_error_lines {no_error_lines}")

print("-"*30)

# 34 Write a function to reverse any iterable without using reverse function.

nums = [1,2,3,4,5]

res = []
for num in nums:
    res.insert(0,num)
print(res)


# *35 Write a function to print the below output.*
#func("TRACXN", 0)  # Should print RCN 

def func(string, value):
    res = ""
    for i in range(len(string)):
        if i %2 == 1:
            res += string[i]
    return res
print(func("TRACXN",0))

# #func("TRACXN", 1) # Should print TAX

def func(string, value):
    res = ""
    for i in range(len(string)):
        if i %2 == 0:
            res += string[i]
    return res
print(func("TRACXN",0))

# 36 Sum all the numbers in the below string.* 
s = "Sony12India567Pvt2ltd" # eg.1+2+5+6+7+2
res = 0
for i in s:
    if "0"<=i<="9":
        res += int(i)
print(res)

# 37 Write a program to sum all the numbers in below string 
from re import findall
string = "Sony12India567Pvt2ltd" # eg.12+567+2
nums = findall(r"\d+", string)
res = 0
for num in nums:
    res += int(num)
print(res)

# 38 Print all the numbers in the below listes

nums = ['abc', '123', 'hello', '23']
for item in nums:
    if '0'<=item[0]<='9':
        print(item)

# 39 Program to print the number of occurrences of characters in a String without using inbuilt functions. >>

word ='helloworld'
ch_count_pair = {ch : word.count(ch) for ch in word}
print(ch_count_pair)

# 40 Program to print only the repeated characters and count of the same.

word= 'helloworld'
repeated_chrs = {ch : word.count(ch) for ch in word if word.count(ch)>1}
print(repeated_chrs)






# 41 Write a program to get alternate characters of a string in list format. 

s = 'helloworld'
res = [s[i] for i in range(len(s)) if i%2==1]
print(res)

# 42 Write a program to get square of list of number's using lambla function.

a = [1, 2, 3, 4, 5]

res = [i**2 for i in a]
print(res)

# 43 Write a function that accepts two strings and returns True if the two strings are anagrams of each other.**


def func(str1, str2):

    for i in str1:
        if i not in str2:
            return "not an angram string"

    for j in str2:
        if j not in str1:
            return "not an angram string"

    return "anagram strings"

print(func("adbc", "abcd"))


# 44 Write, a program to iterate through list and build a new list, only if the items of the list has even number of characters
names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon'] 

new_list = []

for name in names:
    if len(name)%2==0:
        new_list.append(name)

print(new_list)


# 45 Write a program to iterate through list and build a new dictionary, only if the items of the list has even num # of characters.** 


names  =['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', "facebook", "amazon"]

new_list = []

for name in names:
    if len(name)%2==0:
        new_list.append(name)

print(new_list)



# **46 Write a program which squares the numbers in a list using map objectes

a = [1, 2, 3, 4, 5]

res = list(map(lambda item: item**2,a))

print(res)


# *47 Count number of lines in a file without loading the file to the memory*

with open(r"C:\Users\JiyaUlla\Desktop\python\sandeep\mytext1.txt", 'r') as r_obj:
    count = 0
    for i in r_obj:
        count +=1
    print(count)



# *48 Printing line and line no's in a file*
with open(r"C:\Users\JiyaUlla\Desktop\python\sandeep\mytext1.txt", 'r') as r_obj:
    for line in r_obj:        
        print(line)

# **49 Write a Program to print the sum of entire list and sum of only internal lists 


L= [[1,2,3], [4,5,6], [7,8,9]]


summ = 0
for lis in L:
    for item in lis:
        summ = summ + item

print(summ)



# 50 Write a program to reverse the list as below
mylist = ['hi', 'hello', 'python']

res = []

for i in mylist:
    res = [i] + res

print(res)

from re import findall



# 50 write a program to reverse the list as below

words = ["hi", "hello", "python"]
res = ["python", "hello", "hi"]

'---------------------ans---------------------'

result = sorted(words , key= lambda item : len(item), reverse=True )
print(result)



# 51 Write a program to update the tupless 
tup1 = (1, 2, 3, 4) 
tup2 = (100, 200, 300) 
output= (1, 2, 3, 4, 100, 200, 300)

'---------------------ans---------------------'

result = tup1 + tup2
print(result)

# **52 Write a program to replace value present in nested dictionary. 
dict1 = {'a': 100, 'b': {'m': 'man', 'n': 'nose', 'o': 'ox', 'c': 'cat'}} 
#Replace "nose" with "net"

'---------------------ans---------------------'

dict1['b']['n'] = 'net'
print(dict1)

# 53  Write a program to count the number of white spaces in a file.

'---------------------ans---------------------'

space_count = 0
with open(r"C:\Users\JiyaUlla\Desktop\python\sandeep\mytext.txt", "r") as r_obj:
    for line in r_obj:
        space_list = findall("\s", line)
        space_per_line = len(space_list)
        space_count += space_per_line

print("total space in file",space_count)

# 54 Grouping anagrams.
# list1= ["listen", "hello", "eat", "desserts", "silent", "peek", "ate", "keep", "tea", "stressed"] 


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


# *55 What is the difference between defaultdict and normal dictionary...

# narmal dict :
# 1) collection data type used to store key value pair which does not create default key value
# 2) built-in python feature
# default dict :
# 1) collection data type used to store key value pair which have will create the default key value 
# 2) to use we have to import from the collections


# *56 Explain property decorator in python.
# property decorator help to convert functional attribute to the state attribute of class

# 57 What is Mutable and Immutable datatypes.
# mutable :-
# list
# set 
# dictionary
# *) mutable above data types allow to access and modify their items

# immutable :-
# string
# tuple 
# *) immutable above data types allow to access but not modify their items

# *58 Explain get() method in dictionaries.**

# get method takes key as an argument and return the values present with its key from dictionary

# 59 Write a list comprehension to get a list of even numbers from 1-50

result = [num for num in range(1,51) if num%2==0]
print(result)


# 60 Find the longest non-repeated substring in the below stringes

s = "This is a Programming language and Programming is fun"
words = s.split()
non_rep_words = [word for word  in words if words.count(word) == 1 ]
sorted_words = sorted(non_rep_words)
print("second largest non-repeating word",sorted_words[-1])


# +61 Write a program to find the duplicate elements in the list without using inbuilt functions 
names = ['apple', 'google', 'apple', 'yahoo', 'google']

result =list(set([name for name in names if names.count(name)>1]))
print(result)

# 62 Write a program to count the number occurrences of each item in the list without using any inbuilt functions** 
names = ['apple', 'google', 'apple', 'yahoo', 'google', 'facebook', 'gmail', 'yahoo']

result = {}
for name in names:
    if name in result:
        result[name] += 1
    else:
        result[name]=1
print(result)

# 63 Write a function to check if the number is Prime*

num = 6

def is_prime(num):
    for i in range(2,num):
        if num%i==0:
            print("not a prime")
            break
    else:
        print('prime')

is_prime(num)


# 64 How to create a tuple of numbers from 0 to 10 using range function**

nums = tuple(num for num in range(10))
print(nums)


# 65 Write a program to find the largest number in the list without using any inbuilt functions 

numbers = [10, 20, 30, 40, 50, 5, 15, 25]

large = 0
for num in numbers:
    if num>large:
        large = num
print("largest number ", large)


# 66 Write a method that returns the last digit of an integer. For example, the call of get_last_digit(3572) should return 2

def get_last_digit(num):
    return num%10

print(get_last_digit(3572))

def get_last_digit(num):
    return int(str(num)[-1])

print(get_last_digit(123))

# 67 Write a program to find most common words in a given list. 
words=[ 'Look', 'into', 'my', 'eyes', 'look', "into", "my", "eyes", "the", 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", "look", "around", "the", 'eyes', 'look', 'into', 'my', "eyes", "you're", "under"]

words_count_pair = {word:words.count(word) for word in words }
sort_words_count = sorted(words_count_pair, key = lambda item : words_count_pair[item])

print(sort_words_count[-1])

# 68 Make a function named tail that takes a sequence (Like a list, string, or tuple) and a number n and returns the last n elements from the given sequence, as a list.

def tail(sequence,n):
    return list(sequence[-1:-(n+1):-1])[: :-1]

print(tail((1,2,3,5,3,3,43,2,4,6,3,2,4,5,6,7,),3))


#write a program to know a number is perfect square or not
from math import sqrt, floor
num = 8

sqrt_num = sqrt(num)
floor_num = floor(sqrt_num)
if floor_num == sqrt_num:
    print(num, "perfect number")
else:
    print(num, "not a perfect num")


# 70 Write a program to get all the duplicate items and the number of times the item is repeated in the list.**


names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'facebook', 'apple', 'gmail', 'gmail', 'gmail', 'gmail']

duplicate_names = {name: names.count(name) for name in names if names.count(name)>1}

print(duplicate_names)



# 71 Write a program to count the number of occurrences of each word in a file.
from collections import defaultdict

word_count_pair = defaultdict(int)

with open(r"C:\Users\JiyaUlla\Desktop\python\sandeep\mytext.txt") as r_obj:
    for line in r_obj:
        words = line.split()
        for word in words:
            word_count_pair[word] +=1

print(word_count_pair)



# **72 Write a program to count the number of occurrences of vowels in a file.


from re import findall

total_vowels = 0
with open(r"C:\Users\JiyaUlla\Desktop\python\sandeep\mytext.txt") as r_obj:
    for line in r_obj:
        vowels_per_line = findall(r'[aeiouAEIOU]', line)
        total_vowels += len(vowels_per_line)

print(total_vowels)




# **73 Write a program to print all numeric values in a liste

items = ['apple', 1.2, 'google', '12.6', 26, '100']

for item in items:
    if isinstance(item, (int, float)):
        print(item)


# 75 Write a program to count the occurrence of a particular word in the files

def w_count(given_word):
    word_count = 0
    with open(r"C:\Users\JiyaUlla\Desktop\python\sandeep\mytext.txt", "r") as f_obj:
        for line in f_obj:
            words = line.split()
            word_count += words.count(given_word)

    return word_count

print(w_count('good'))


from collections import defaultdict

# 76 Write a program to map a product to a company and build a dictionary with company and list of products paires all 

products = ['iPhone', 'Mac', 'Gmail', 'Maps', 'iwatch', 'Windows', 'ios', 'Google Drive', 'One Drive']

apple_products = google_products = msft_products = other_products = []

register_apple_products = ["iPhone", "Mac", "iwatch", 'ios']
register_google_products = ["Gmail","Maps", "Google Drive"]
register_msft_products = ["Windows","One Drive"]

company_product_pair = defaultdict(list)

for product in products:
    if product in register_apple_products:
        company_product_pair['apple_products'] +=  [product]
    elif product in register_google_products:
        company_product_pair['google_products'] +=  [product]
    elif product in register_msft_products:
        company_product_pair['msft_products'] +=  [product]
    else:
        company_product_pair['other_products'] +=  [product]

print(company_product_pair)



# 77 Write a program to rotate items of the list >>

names = ["apple", "google", "yahoo", "gmail", "facebook", "flipkars", "amazon"]


temp= names[0]
for i in range(len(names)-1):
    names[i] = names[i+1]
names[-1]=temp

print(names)
    
        
# 78 Write a program to rotate characters in a stringes I
from re import findall

name = "jiya"
list_chr = findall(r"[\w]",name)

temp= list_chr[0]
for i in range(len(list_chr)-1):
    list_chr[i] = list_chr[i+1]
list_chr[-1]=temp

print("".join(list_chr))

# 79 Write a program to count the number of white spaces in a given stringes

from re import findall

string = "hello world how are you !"

white_space_count = findall(r"[\s]", string)
print(len(white_space_count))


# 80 Write a program to print only non-repeated characters in a stringes
string = "hello world how are you !"

print([ch for ch in string if string.count(ch)<=1])


# 81 What is the difference between a list and a tupless

# list : mutable  , takes more memory
# tuple : immutable  , takes less memory



# 82 Write a program to print all the consonants in a given stringes
from re import findall
string = 'helloworld'

print(findall(r"[^aeiouAEIOU]", string))


# 83 Write a program to count the number of commented lines in a text filess

count = 0
with open(r"C:\Users\JiyaUlla\Desktop\python\sandeep\mytext.txt") as r_file:
    for line in r_file:
        if line[0] == "#":
            count +=1

print(count)





# **84 Write a program to check if the year is leap year or notes
year = 2002

if (year%4 ==0 or year %400==0) and not year %100==0:
    print("is a leap year")
else:
    print("not a leap year ")



# *85 Liner Search*
# search one by one item of any sequence called linear search



# **86 Difference between xrange and ranges
# both are same xrange used in python 2 but range is used python 3


# 87 Write a program to count no of capital letters in a string
sentence = "Hi How are You Welcome to Python"

from re import findall
cap_letters = findall(r"[A-Z]", sentence)


# 88 Write a program to get the below output
# * 
# * *
# * * *
# * * * *

n = 5
for i in range(1,n+1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()
print(len(cap_letters))

# 89 Write a program to get the below outputes

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# oupt = 
# [1, 2]
# [3, 4]
# [5, 6]
# [7, 8]
# [9]

res = []
temp = []
for num in nums : 
    if len(temp)==2:
        res.append(temp)
        temp = []
        temp.append(num)
    else:
        temp.append(num)
else:
    res.append(temp)

print(res)


# 98 write a program to check if the elements in the second list is series of continuation of the items in the first

list1 = [10, 12, 14, 16, 18] 
list2 = [20, 22, 24, 26, 28]

temp = list1[0] - list2[0]
if len(list1) == len(list2):
    for l1_item, l2_item in zip(list1, list2):
        if l1_item  - l2_item == temp:
            continue
        else:
            print("series has some missmatch nums ")

else:
    print("some missmatch")


list1 = [0, 5, 10, 15] 
list2 =  [20, 25, 30, 35, 41]

temp = list1[0] - list2[0]
if len(list1) == len(list2):
    for l1_item, l2_item in zip(list1, list2):
        if l1_item  - l2_item == temp:
            continue
        else:
            print("series has some missmatch nums ")
else:
    print("some missmatch")


list1 = [10, 20, 30, 40] 
list2 = [50, 40, 60, 70]


temp = list1[0] - list2[0]
if len(list1) == len(list2):
    for l1_item, l2_item in zip(list1, list2):
        if abs(l1_item -l2_item) == temp:
            continue
        else:
            print("series has some missmatch nums ")
else:
    print("some missmatch")


# 91 What is the difference between append() and extend() method in listes

# append will add the individual item to the end of list 
# exitend will add all the items of  list to the list 

# 92 Write a program to find the first repeating character in a stringes

string = "hi there how are you"
unique_ch = []

for ch in string:
    if ch not in unique_ch:
        unique_ch.append(ch)

    else:
        print(ch)
        break 


# +93 write a program to find the index of nth occurrence of a sub-string in a stringes

from re import finditer
string = "Hi hello  world how are you hello how are you "

myobj = finditer(r"hello", string)
last_obj = list(myobj)
print(last_obj[-1])


# 94 Write a program to print prime numbers from 1 to 50

for num in range(1,50):        
    for i in range(2,num):
        if num %i ==0:
            break
    else:
        print(num)

#95 Write a program to sort a list which has mix of both odd and even numbers, the sorted list should have odd numbers first and then even numbers in sorted orderss 
nums = [3, 4, 1, 7, 2, 12, 8, 6, 9, 111]

# out =  [1, 3, 7, 9, 11, 2, 4, 6, 8, 12]

even_list = [num for num in nums if num%2==0 ]
sorted_even_list = sorted(even_list)

odd_list = [num for num in nums if num%2==1]
sorted_odd_list = sorted(odd_list)

result = sorted_odd_list + sorted_even_list

print(result)


# 96 Write a program to sort a list which has mix of both odd and even numbers, in the sorted List, odd numbers should e in ascending order and even numbers should be in descending orderss
nums = [3, 4, 1, 7, 2, 12, 8, 6, 9, 11]

output = [1, 3, 7, 9, 11, 12, 8, 6, 4, 2]

odd_list = [num for num in nums  if num%2==1]
sorted_odd_list = sorted(odd_list)

even_list = [num for num in nums  if num%2==0]
reverse_sorted_even_list = sorted(even_list, reverse=True)

result = sorted_odd_list + reverse_sorted_even_list

print(result)


# 97 Write a program to count the number of occurrences of non-special characters in a given stringes 
string =  "hello@world! welcome!!! Pythons hi how are you & where are you?"

from re import findall

res = len(findall(r"[\w]", string))
print(res)


# 98 Grouping Flowers and Animals in the below listes
from collections import defaultdict
items=['lotus-flower', 'lilly-flower', 'cat-animal', 'sunflower-flower', 'dog-animal']

result = defaultdict(list)

for item in items:
    name, category = item.split("-")
    result[category] += [name]

print(result)

# 99 Grouping files with same extensions 
from  collections import defaultdict
files = ['apple.txt', 'yahoo.pdf', 'gmail.pdf', 'google.txt', 'amazon.pdf', 'facebook.txt', 'flipkart.pdf']

result = defaultdict(list)

for file in files:
    name, file_type = file.split(".")
    result[file_type] += [name]

print(result)



# 100 Filter only those characters except digitss 

from re import findall

string = '@hello12world34welcome! 123'

result = findall(r"([a-zA-Z]|[^\w])", string)

print(result)



# **101 Count number of words in a sentence. ignore special characters. 
sentence = "Hi there! How are you:) How are you doing today!"

from re import findall

words = findall(r"\b[a-zA-Z0-9]+\b", sentence)
print(len(words))


# *182 Grouping even and odd numbers*
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

# o/p should be (1: [1, 3, 5, 7, 9], 0:[1 2, 4, 6, 8, 101])

from collections import defaultdict

result = defaultdict(list)

for number in numbers:
    if number %2 ==0:
        result[0]= result[0]+[number,]
    else:
        result[1]= result[1]+[number,]

print(result)


# *103 Find all max numbers from the below list

numbers = [1, 2, 3, 0, 4, 3, 2, 4, 2, 1, 0, 4]
max_number = 0

for num in numbers:
    if num>max_number:
        max_number = num

max_nuumbers = [num for num in numbers if num == max_number]

print(max_nuumbers)

# 104 Find all max length words from the below sentences >> 
sentence = "hello world hi apple you yahoo to you"

max_word_length = 0

words = sentence.split()

for word in words:
    if len(word)>max_word_length:
        max_word_length = len(word)

all_max_length_words = [word for word in words if len(word)== max_word_length]

print(all_max_length_words)



# 105 Find the range from the following strings 
from unittest import result
sentence =  '0-0, 4-8, 20-20, 43-45'
#Output Should be 10, 4, 5, 6, 7, 8, 20, 43, 44, 45, 46]

words = sentence.split(",")
row_result = []

for word in words:   
    chrs = word.split("-")
    lower_range, higher_range = [int(ch) for ch in chrs]
    all_nums = [num for num in range(lower_range, higher_range)]
    row_result += [num for num in range(lower_range, higher_range)] + [lower_range,higher_range]

result =sorted(list(set(row_result)))
print(result)

# 106 Can we override a static method in python?
# yes

# +107 Write a function which returns the sum of lengths of all the iterables 

def total_length(*args):
    all_collection_len = 0
    for col in args:
        all_collection_len += len(col)
    return all_collection_len



print(total_length([1, 2, 3], (4, 5), ['apple', 'google', 'yahoo', 'gmail', 'Flipkart'], {1, 2, 3 }, {'a': 1, 'b': 2}) )
# o/p: 15


# 108 Replace whitespaces with newline character in the below stringes >> 
sentence = "Hello world welcome to python"

words = sentence.split()
result = "\n".join(words)
print(result)


# 109 Replace all vowels with "" >>
from re import findall

sentence = "hello world welcome to python"
chars = findall(r"[^aeiouAEIOU]", sentence)
res = "".join(chars)

print(res)

# 110 Replace all occurances of "Java" with "Python" in a filess

with open(r"C:\Users\JiyaUlla\Desktop\python\sandeep\mytext.txt", "r") as r_obj:
    with open(r"C:\Users\JiyaUlla\Desktop\python\sandeep\mytext1.txt", "w") as w_obj:
        for line in r_obj:
            w_obj.write(line.replace("java","python"))





# **111 Maximum sum of 3 numbers and Minimum sum of 3 numbersss 

numbers = [10, 15, 20, 25, 30, 35, 40, 15, 15]

sorted_nums = sorted(numbers)

sum_of_minimum_three =  sorted_nums[0] + sorted_nums[1] + sorted_nums[2]
sum_of_maximum_three =  sorted_nums[-1] + sorted_nums[-2] + sorted_nums[-3]


print(sum_of_minimum_three)
print(sum_of_maximum_three)


# **112 Write a program to get the output as belowes

inp = "python@#$%pool"
# o/p should be ['PYTHON, POOL']

from re import findall

words = findall(r"\b[\w]+\b", inp)
result = [word.upper() for word in words ]
print(result)


# 113 Write a program to print all the number which are ending with 5

numbers = ['1', '12', '123', '12345', '125', '985', '55', '5', '95655', '55555']

result = []
for num in numbers:
    int_num = int(num)
    if int_num%10==5:
        result.append(int_num)

print(result)

# 114 Write a program to get the indexes of each item in the below lists

names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'google', 'gmail', 'gmail', 'gmail']
#  output should be >> {'apple': [0, 2], 'google': [1, 5], yahoo: [3, 4], 'gmail': [6, 7, 8]}

from collections import defaultdict

result = defaultdict(list)

for i in range(len(names)):
    result[names[i]] += [i,]

print(result)


# *115 Write a program to print "Bangalore" 10 times without using "for" loop*

print("banglore "*10)
    
# **116 Write a program to print all the words which starts with letter 'h' in the given strings 
string = 'hello world hi hello universe how are you happy birthday'

string = string.split()

for word in string:
    if word[0]=='h':
        print(word)


# 117 Write a program to sum all even numbers in the given stringes

sentence = 'hello 123 world 567 welcome to 9724 python'

total = 0
for ch in sentence:
    if "0"<=ch<="9":        
        int_ch = int(ch)
        if int_ch %2==0:
            total += int_ch

print(total)

# 118 Write a program to add each number in wordi to number in word2

word1 = 'hello 1 2 3 4 5'

word2 = 'world 5 6 7 8 9'

# e.g. 1+5, 2+6, 3+7, 4+8, 5+9
def word_remover(word1):
    words = word1.split()
    words.remove(words[0])
    new_words = [int(word) for word in words]
    return new_words

def summ_of_numbers():
    all_nums1 = word_remover(word1)
    all_nums2 = word_remover(word2)

    for i in range(len(all_nums1)):
        print(all_nums1[i]+ all_nums2[i])

summ_of_numbers()


# 119 Write a program to filter out even and odd numbers in the given stringes python

from re import findall
sentence = 'hello 123 world 456 welcome to python498675634'

nums = findall(r"\d", sentence)
odd_nums = [int(num) for num in nums if int(num)%2==1]
even_nums = [int(num) for num in nums if int(num)%2==0]

print(odd_nums)
print(even_nums)


# *120 Write a program to print all the number which are starting with 8

numbers = ['857', '987', '8', '128', '888888', '547', '7674', '89', '589', '388888', '2889']

nums_start_with_8 = [num for num in numbers if num[0] =="8"]
print(nums_start_with_8)



# 21 Write a program to remove duplicates from the list without using set or empty 

from functools import reduce
list1 = [1, 2, 3, 4, 1, 2, 3, 4, 3, 4, 41]
res =   [list1[ind] for ind in range(len(list1)) if ind == list1.index(list1[ind]) ]
print(res)


# 122 Print all the missing numbers from 1 to 10 in the below list

lis1 = [1,7,2, 3,6,]

lis2 = [num for num in range(1,11)]
for i in lis2:
    if i not in lis1:
        print(i)

# **123 Write a python program to get the below output

l1 = [1, 2, 3]
l2= ['a', 'b', 'c']
# o/p ['la', 'ib', 'ic', '2a', '2b', '2c', '3a', '3b', '3c']
# res = list(map(lambda item : [str(item)+i for i in l2], l1))

# print(res)
res = []
for item in l2:
    for var in l1:
        res += [str(var)+item]
print(res)


# 124 Write a python program to get the below output

# **125 What is the output of the below function call
class Demo: 
    def greet (self):
        print("hello world")

    def greet(self): 
        print("hello universe")

d= Demo()
d.greet()

# 126 In the list below, find all the number pairs which results in 10 either when added or subtracted python >> 

nums= [3, 5, 4, 8, 11, 1, -1, 6]

res = []
for num in nums:
    for item in nums:
        if num - item == 10 or item-num == 10:
            res += [(num, item)]

print(res)


# 127 Write a decorator to prefix +91 to the original phone numbers
def phonprefix(func):

    def wrapper(num):
        add = "+91 "
        var = func(num)
        if var[0:4] == add:
            return num 
        else :
            return add + var
    return wrapper

@phonprefix
def myphone(num):
    if len(str(num)) != 10:
        raise Exception ("invalid number")
    return num

print(myphone('7418529639'))

# 128 Write a program to get the below 
outputes ={"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

#o/p should be ['b', 'd']

res = []
for key,value in outputes.items():
    if key =='b' or key=="d":
        res +=[key]

print(res)

# 129 Can we have multiple __init_ methods in a class

# yes we can but it will overide latest one will be given priority
# we shoule have multiple __init__methos while calling multiple super classes 



# 130 Why python is Object Oriented?
# it is featue of python  have class instance method and states 
# we can impliment oops concepts such as inheritence polymophisum abstraction and encapsultion
# se we can say it Object oriented 

# 131 What are .pyc files
# .pyc files are the python  files which will store the bytecode  (machine code ) of python file

# 132 Reverse a list without using any built-in functions and slicing

list1 = [1, 2, 3, 4, 5 ]

list2 = []
for i in list1:
    list2.insert(0,i)
    
print(list2)


# 133 Write a program to get the below output

inp="10.20.38.40"
#o/p="40.30.20.10"
res = ""

for i in inp:
    res = i + res

print(res)


# 134 What is the difference between while loop and for loop.

# while loop is used for infinite iterations
# for loop is used for specific lenght of iterations

# 135 What are magic methods?
# protocols which followed during the construction any concepts such oop
# function object called magic methods

# 136 What is pylint.
#  pylint is tool help to write the python program c
#check for errors 
# coding standards
# give suggetions ect...
# rules and regulation


# 137 What is the output of the below program.
var  = [1, 2, 3, 4] * 2
print(var)
res = [1,2,3,4,1,2,3,4]
# 138 What is the difference between the is and == operators

# is basically checkes for memory address of any object
# == checks the content present in any objet



# 139 What is "self" in class.

# self is just a act as argument but it actuall hold the address of objection which
# is passed to it while creating object for any specified class


# 140) What is assert statement. What is the difference between assert and if/else statement.

# 141) What is the difference between a module, a package, and a library

# simple python file -> module
# python file folder contain -> __init__.py file called package
# one or more package and python file called as --> library 

# 142) write a program to get the below output using while loop

# 1

# 12

# 123

# 1234

row = 4
i = 1
while i<=4:
    j=1
    while j<=i:
        print(j, end="")
        j = j+1
    print()
    i = i+1


# 43 write a program to get the below output
items = ['$123.45', '$434.23', '$567.89']

# >>> # o/p [123.45, 434.23, 567.89]

from re import findall 
res = []
for item in items:
    var = findall(r"\d+\.\d+",item)
    res += var
print(res)

# 144) Generator function for Fibonacci series program


def func(num):
    a = 0
    b = 1    
    count = 1
    while count <=num:
        yield a
        a,b = b,a+b
        count += 1
        
obj = func(5)
for i in obj:
    print(i)

# 145) Write a program to print common character present in all the items of the below list 
items = [ "glory", "glass", "sight", "fight"]

for item in items:
    for ch in item:
        if ch in items[0] and ch in items[1] and ch in items[2] and ch in items[3]:
            print(ch)
            break
       

# 146) Function should accept a list and if any number divisible by 3 then modify to 33 or else keep it as it is

def func(lists):
    for  i in range(len(lists)):
        if lists[i] % 3 == 0:
            lists.pop(i)
            lists.insert(i, 33)

    return lists

print(func([1,2,3,4,5,6,7,8,9]))



# 147 write a program to print the below pattern

# 123*

# 12*4

# 1*34

# *234

row = 5
col = 5
for i in range(1, row+1):        
    for j in range(1, col+1):
        if i+j == row+1:
            print("*", end=" ")
        else:
            print(j, end=" ")
    print()


# 48 write a program to map digits to its corresponding word

items = { "0": "ZERO", "1": "ONE", "2": "TWO", "3": "THREE", "4": "FOUR", "5": "FIVE", "6": "SIX", "7": "SEVEN", "8": "EIGHT", "9": "NINE" }

