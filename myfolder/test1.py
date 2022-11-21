
'''
with  open("C:\\Users\\JiyaUlla\\Desktop\\pythonfiles\\mydemo1.txt",'a') as file :
    file.write(" python class")
    file.close()



dict1 = {
    "pizza" : "🍕",
    "burger" : "🍔",
}

dict2 = {
    "bucket" : "🍿",
    "milk" : "🧂",
}

#output = {**dict1, **dict2}

output = dict(list(dict1.items())+ list(dict2.items()))

print(output)


# 1. String Programming Interview Questions
# The string is a primary and probably most common thing you come across
#  on any programming language and so is with any programming interview.
#  There is almost always a question on String whether its related to the length 
# or replace but I have always found one or two String programming questions on 
# interviews.




# 1) Write code to check a String is palindrome or not? (solution)
# A palindrome is those String whose reverse is equal to the original. 
# This can be done by using either StringBuffer reverse() method or
#  by technique demonstrated in the solution here.

str1 = "lolo"

str2 = str1[::-1]

if str1 == str2 :
    print("palindrome string ")

else :
    print("not a palindrome string ")

# 2) Write a method which will remove any given character from a String? (solution)
# hint: you can remove a given character from String by converting it into a character array and then using substring() method for removing them from output string.

def remove_chr(string, char ):
    output_string = ""
    for ch in string :
        if ch != char:
            output_string = output_string + ch

    return output_string

input_string = "hello world "
print(remove_chr(input_string, "l"))
    

# 3) Print all permutation of String both iterative and Recursive way? (solution)

def iterfact(num):
    res = 1
    for i in range(1, num+1):
        res = res * (num-1)
    return res 


def fact(num):
    if num == 1:
        return 1
    return num * fact(num-1)

def permutation(n, r):
    per  = (fact(n)/fact(n-r))
    return per



n = 5
r = 3
print(permutation(n,r))




# 5) How to find the first non repeated character of a given String? (solution)

string = "hello wohrld"

for i in string:
    if string.count(i) ==1:
        print(i)
        break

# 6) How to count the occurrence of a given character in a String? (solution)

string = "hello wohrld"

count_char_dict = {key : string.count(key) for key in string }
print(count_char_dict)


# 7) How to check if two String are Anagram? (solution)

string1 =  "waorld"
string2 = "worlda"

def anagram(string1, string2):
    for char in string1:
        if char not in string2:
            return False

    for char in string2:
        if char not in string1:
            return False

    return True
       

if anagram(string1, string2):
    print("is anagram")
else :
    print("not an anagram ")




        
    


# 8) How to convert numeric String to int in python? (solution)

string = "H"
print(ord(string))


# Some more String related Questions which mostly appear in Java
#  programming interviews:

# 1) What is the difference between String, StringBuilder, and StringBuffer 
# in Java? (answer)
# The main difference is that String is immutable but both StringBuilder and
#  StringBuffer are mutable. Also, StringBuilder is not synchronized like 
# StringBuffer and that's why faster and should be used for temporary String manipulation.


# 2) Why String is final in Java? (answer)
# The string is final because of same reason it is immutable. Couple of reasons 
# which I think make sense is an implementation of String pool, Security, 
# and Performance. Java designers know that String will be used heavily in
#  every single Java program, so they optimized it from the start.

# 3) How to Split String in Java? (answer)
# Java API provides several convenient methods to split a string based
#  upon any delimiter e.g. comma, semicolon or colon. You can even use 
# a regular expression to split a big string into several smaller strings.


from re import findall 
st = "Hello world hi hell how are you"
outst = st.split()
print(outst)
outst2 = findall(r"\b\w+\b",st)
print(outst2)



# 4) Why Char array is preferred over String for storing password? (answer)


# These questions help improve your knowledge of string as a data structure.
#  If you can solve all these String questions without any help then you are in good shape.

# If you want to learn more about String and other data structure then I
#  suggest you check out the Master the Coding Interview: Data Structures 
# + Algorithms course by Andrei Negaoie on ZTM Academy. It's a great course
#  to revise fundamentals before interview. 

# Data Structure and Algorithm Interview Questions Programmers

# If you need more practice, here is another list of 20 string coding questions.




# 2. Programming questions on Array
# An array is one of the topics where most of the programming questions are asked.
# There are many and many programming questions on Array and here I have included 
# only some of them which are not very difficult to solve but some of the array
#  programming questions can be extremely challenging, so well prepare this topic.


# 9) In an array 1-100 numbers are stored, one number is missing how do you find 
# it? (solution)

array = [1, 2,3,4,6,7,8,9,10]
print(array)
for item in range(1,11) :
    if item not in array:
        print(item)
        break



# 10) In an array 1-100 exactly one number is duplicate how do you find it?
#  (solution)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

for i in nums:
    if nums.count(i)>1:
        print(i)
        break



# 11) In an array 1-100 multiple numbers are duplicates, how do you find it?
#  (solution)
# One trick in this programming questions is by using HashMap or Hashtable,
#  we can store a number as key and its occurrence as a value if the number
#  is already present in Hashtable then increment its value or insert value
#  as 1 and later on print all those numbers whose values are more than one.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12, 13, 14, 15, 16, 17,1, 90, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

for i in nums:
    if nums.count(i)>1:
        print(i)
        continue
        

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12, 13, 14, 15, 16, 17,1, 90, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]


nums_count_dict = {num : nums.count(num) for num in nums if nums.count(num)>1}
print(nums_count_dict)




# 12) Given two arrays, 1,2,3,4,5 and 2,3,1,0,5 find which number is not 
# present in the second array.
# Here is a quick tip to solve this programming question: put the elements
#  of the second array in the Hashtable and for every element of the first
#  array, check whether it’s present in the hash or not, O/P all those
#  elements from the first array that are not present in the hash table


set1 = {1,2,3,4,5}
set2 = {2,3,1,0,5}
res = set1 - set2
print(res)


# 13) How do you find the second highest number in an integer array? 
# (solution)

nums = [1,3,4,9, 10, 1]
nums.sort()
print(nums[-2])


nums = [1, 3, 4, 9, 8, 10, 6, 2]
highest_num = nums[0]
for i in nums:
    if i>highest_num:
        highest_num = i

print(highest_num)

shighest_num = nums[0]
for i in nums:
    if i>shighest_num and i != highest_num:
        shighest_num = i

print(shighest_num)



# 14) How to find all pairs in an array of integers whose sum is equal 
# to the given number? (solution)


nums = [1,2,4,5,2,4,5,34,4,2,3,3,9,2,8,3,7,4,6,5,5,]
res = []

_sum = 10
r_sum = 0
for i in range(0, len(nums)):
    r_sum += nums[i]
    if r_sum == _sum :
        res.append((nums[i-1],nums[i]))
        rsum = 0
    


print(res)

    



# 15) How to remove duplicate elements from the array in Java? (solution)

nums = [1,2,4,5,2,4,5,3,4,4,2,3,3,9,2,8,3,7,4,6,5,5,]

res = []
for num in nums:
    if num not in res:
        res.append(num)


print(res)


nums = [1,2,4,5,2,4,5,3,4,4,2,3,3,9,2,8,3,7,4,6,5,5,]

res = list(set(nums))
print(res)




nums = [1,2,4,5,2,4,5,3,4,4,2,3,3,9,2,8,3,7,4,6,5,5,]

def myfunc(num):
    if num %2 ==0:
        return True


res = list(map( lambda num : num-1 if num%2==1  else num ,nums))
print(res)




# 16) How to find the largest and smallest number in an array? (solution)

nums = [1,5,8,6,10,20,5,1,2,-9]

print(max(nums))
print(min(nums))





# 17) How to find the top two maximum number in an array? (solution)



nums = [10,5,12,16,20,9,5,1,8]

_max = max(nums)
s_max = 0
for num in nums:
    if num>s_max and num not in (_max,):
        s_max = num

print(_max)  
print(s_max)




nums = [10,5,12,16,20,9,5,1,8]

nums = sorted(nums)
print(nums[-2])


nums = [10,5,12,16,20,9,5,1,8]

for i in range(0, len(nums)):
    for j in range(0,len(nums)-1):
        if nums[j]<nums[j+1]:
            temp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = temp

print(nums)

'''

nums = [5, 9, 1,3, 8,4]

for num in nums:
    print(nums)


# These questions will not only help you to develop your problem-solving
#  skills but also improve your knowledge of array data structure.

# If you need more advanced questions based upon array then you can see
#  also see The Coding Interview Bootcamp: Algorithms + Data Structures,
#  a bootcamp style course on algorithms, especially designed for 
# interview preparation to get a job on technical giants like Google,
#  Microsoft, Apple, Facebook etc.




# And, if you feel 10 is not enough questions and you need more practice,
#  then you can also check out this list of 30 array questions.




# 3. LinkedList Programming Interview Questions
# A linked list is another important data structure after array and String.
#  It actually compliments array and whatever you cannot do with an array, 
# you can do with a linked list.

# For example, the array needs contiguous memory to store objects but the 
# linked list doesn't need that. It's difficult to add and remove elements
#  in an array because you need to shift existing elements but that is very 
# easy with a linked list, as you just need to change the pointer to accommodate them.

# But, nothing is free in this world. While linked list provides all these
#  functionalities but the cost of that you lose the ability to search
#  elements in constant time with index. Searching and element require
#  traversing linked list, which means examining all nodes, thus cost around O(n) time.


# 14) How do you find middle element of a linked list in a single pass?
# To answer this programming question I would say you start with a simple 
# solution on which you traverse the LinkedList until you find the tail of
#  linked list where it points to null to find the length of the linked list
#  and then reiterating till middle.

# After this answer interviewer will ask you to find the middle element in 
# single pass and there you can explain that by doing space-time trade-off 
# you can use two pointers one incrementing one step at a time and other 
# incrementing two-step a time, so when the first pointer reaches end of 
# linked second pointer will point to the middle element.



# 15) How do you find the 3rd element from last in a single pass? (solution)
# This programming question is similar to above and can be solved by using 
# 2 pointers, start the second pointer when the first pointer reaches third place.


# 16) How do you find if there is any loop in a singly linked list? 
# How do you find the start of the loop? (solution)
# This programming question can also be solved using 2 pointers and 
# if you increase one pointer one step at a time and other as two steps
#  at a time they will meet in some point if there is a loop.


# 17) How do you reverse a singly linked list? (solution)


# 18) Difference between a linked list and array data structure? (answer)



# If you are having trouble solving these linked list coding questions then 
# I suggest you refresh your data structure and algorithms skill by going 
# through  Grokking the Coding Interview: Patterns for Coding Questions course 
# on Educative, one of the best course to learn coding patterns like Sliding 
# Window and Merge intervals, which can be used to solve 100+ Leetcode problems. 

# Programming Interview Questions with 1 to 3 years experienced programmers



# If you need more linked list based questions then you can also check out this 
# list of 30 linked list interview questions for more practice questions.



# 4. Binary Tree Programming Interview Questions
# Binary tree or simply tree is one of favorite topic for most of the 
# interviewer and pose a real challenge if you struggle with recursion. 
# Programming questions on the tree can become increasingly difficult when 
# you think iterative but sometimes can be very easy if you come with a recursive solution.


# 18) How do you find the depth of a binary tree? (solution)


# 19) Write code to print InOrder traversal of a tree? (solution)


# 20) Print out all leaf node of a binary tree? (solution)


# 21) Write a method in Java to check if a tree is a binary search tree or not? (solution)


# 22) How to check if a tree is balanced or not in Java? (solution)


# 23) How is a binary search tree implemented? (solution)

# 24) How do you perform preorder traversal in a given binary tree? (solution)

# 25) How do you traverse a given binary tree in preorder without recursion? (solution)

# 26) How do you print all nodes of a given binary tree using inorder traversal without recursion? (solution)
# 27) How do you implement a postorder traversal algorithm? (solution)
# 28) How do you traverse a binary tree in postorder traversal without recursion? (solution)
# 29) How are all leaves of a binary search tree printed? (solution)
# 40) How do you count a number of leaf nodes in a given binary tree? (solution)
# 41) How do you perform a binary search in a given array? (solution)


# Binary tree based questions sometimes get trick and if you are having trouble
#  solving these tree-based list coding questions then I suggest you revise
#  your data structure and algorithms skill by going through Software Engineering 
# Interview Course on Exponent.  


# Top 30 Coding questions asked in Interview - Java C C++ Answers


# This course provides a comprehensive review of the most important data
#  structures, algorithms, and system design principles and also provides mock 
# interviews with FAANG engineers and managers showcasing what interviews look
#  like, as well as interactive coding problems in Python and JavaScript. 

# Plus, there are extra lessons on behavioral interview questions for engineers
# , and advice on growing your tech career.  It's written by an ex-FAANG engineers 
# and it is one of the most comprehensive course to revise all important data structures
#  like an array, linked list, binary tree etc.



# 5. Programming Questions on Searching and Sorting
# I have only included two programming questions related to searching 
# and sorting but there are more can be found on Google. Purpose of these programming
#  questions is to see whether a programmer is familiar with the essential search
#  and sort mechanism or not.


# 23) Write a program to sort numbers in place using quick sort? (solution)


# 24) Write a program to implement a binary search algorithm in Java or C++? (solution)


# 25) How do you sort Java objects using a Comparator? (answer)
# This is another Java specific programming questions and you can check how to sort
#  Object using Comparator and Comparable for an answer.

# 26) Write code to implement Insertion Sort in Java? (solution)


# 27) Write code to implement Bubble Sort in Java? (solution)



# If you can solve these questions easily then you are in good shape. For more 
# advanced questions, I suggest you solve problems given in the Algorithm Design
#  Manual by Steven Skiena, a book with the toughest algorithm questions.

# Top 30 Algorithms questions asked in Interview - Java C C++ Answers




# 6. Programming Questions on Numbers
# Most of the programming questions are based on numbers and these are the ones 
# which most of us did on the college level and mind you they still have value I
#  have seen programmers with experience of 3 years struggle with these programming
#  questions and doesn't solve it some time and take a lot of time which simply 
# shows that they are not in programming in there day to day work.


# 26) Write code to check whether a no is a power of two or not? (solution)


# 27) Write a program to check whether a number is a palindrome or not? (solution)
# Check out this post which shows how to reverse a number in Java and can be used
# to find if its palindrome or not.


# 28) Write code to check whether an integer is Armstrong number or not? (solution)
# Here is a Java program to find Armstrong number, you can use the same logic to 
# write code in any other programming language like C and C++.


# 29) Write a program to find all prime number up to a given number? (solution)
# Here is another Java program to find prime numbers and print them. By using 
# logic demonstrated in this program; you can write a similar program in C and C++.


# 30) Write a function to compute Nth Fibonacci number? Both iterative and recursive? (solution)
# You can check this Java program to print Fibonacci Series using recursion and iteration.


# 31) How to check if a number is binary? (solution)
# For this question, you need to write a function which will accept an integer 
# and return true if it contains only 0 and 1 e.g. if the input is 123 then your
#  function will return false, for 101 it should return true.

# 32)  How to reverse an integer in Java? (solution)


# 33) How to count a number of set bits in given integer? (solution)


# 34) How to find the sum of digits of a number using recursion? (solution)


# 35) How to swap two numbers without using temp variable? (solution)


# 36) How to find the largest of three integers in Java? (solution)


# 37) Write a program to find prime factors of an integer? (solution)


# 38) How to add two integers without using arithmetic operator? (solution)


# If you need more such coding questions you can take help from books like Cracking 
# the  Coding Interview book by Gayle Lakman  McDowell which presents 189+ Programming
#  questions and solution. A good book to prepare for programming job interviews in a
#  short time.


# Top 30 Programming Interview Questions Answers for Programmers




# 7. General Programming Interview Questions
# In this category of programming questions, I have put questions which are not fit 
# into any data structure but present a real-life problem and you need to provide
#  a solution. These programming questions are sometimes based on problems faced by the developer itself.

# I have not included many Software design-related programming question which I 
# have shared on Top 20 software design questions and answers; you can also check that.


# 31) Write a program to find out if two rectangles R1 and R2 are overlapping? (solution)


# 32) You need to write a function to climb n steps you can climb either 1 step at 
# a time or 2 steps a time, write a function to return a number of ways to climb a 
# ladder with n step. (solution)
# It's actually a Fibonacci series so you can solve it like that.

# 33) Write code for Generate Random No in a range from min to max? (solution)


# 34) Write a program for word-wrap which should work on any screen size? (solution)


# 35) Design an algorithm to find the frequency of occurrence of a word in an article? (solution)


# 36) Write a program to implement a blocking queue in Java? (solution)


# 37) Write a program for the producer-consumer problem? (solution)
# This article solves the producer-consumer problem using BlockingQueue in Java. 
# You can refer it to answer this question.


# 8. Books to prepare for Programming Job Interviews
# There are a lot of good books available, which can help the programmer to do
#  well on Interviews. Here is a list of books, which I personally prefer, in order, I like them.

# Programming Interview Questions and Answers


# 1. Programming Interviews Exposed: Secrets to Landing Your Next Job
# A must-read books for both beginners and experienced programmers alike. It
#  not only help you to do well on interviews but also on negotiation, answering
#  general questions etc.


# 2. Cracking the Coding Interview: 189 Programming Questions and Solutions
# This book contains a collection of questions from a wide range of programming topics,
#  including data structure, algorithms, strings, Java, networking, database, SQL, 
# object-oriented programming, software design etc. This book will give you the 
# whole picture of what can be asked.


# 3. Top 10 coding interview problems asked in Google with solutions: Algorithmic
#  Approach
# This is the must read a book, if you are preparing for Google interview, or s
# omething along the line e.g. Facebook, Amazon or Microsoft Interviews. It 
# contains top 10 programming problems, frequently asked at Google with detailed
#  worked out a solution, explanation in both pseudocodes and in C++.



# 9. Tips on answering Programming questions
# Interviews are not ready and even if you know the answers you need to keep some 
# things in mind while answering the questions or solving problems. The
#  interviewer often likes to see your ability to solve unknown problems and
#  how you react when a new challenge presented.

# For example, if you wrote a recursive solution then they will ask you to solve 
# without recursion, if you use additional memory then you will ask you to solve 
# without that and in-place, mostly in case of an array and linked list problems.

# Here are some of the tips to do well on your programming interview:

# 1. If Interviewer asks you to write function then make sure you do some necessary 
# check for bad input e.g. null check or empty check. Most of the time programmer 
# forgets to test for not null, empty, less than 1, greater than 1 or zero input.


# 2. If you write an iterative version of function then Interviewer may ask you to 
# write recursive version or vice-versa so be prepared for that.


# 3. If you write a recursive function then Interviewer will ask to optimize it, 
# even in case of Iterative version. So remember that you can optimize recursive 
# function by Memorization (caching already calculated value) and by applying some
#  space/time tradeoff principle. For example, recursive version of Fibonacci 
# series has O(n ^2) time performance which can be reduced to O(n) using Memoziation.


# 4. The interviewer may ask you to calculate Order of complexity for best and
#  worst case of any method so be prepared.


# Read more: https://javarevisited.blogspot.com/2011/06/top-programming-interview-questions.html#ixzz7dppQy4Ii
# 4) Write a function to find out longest palindrome in a given string? (solution)
