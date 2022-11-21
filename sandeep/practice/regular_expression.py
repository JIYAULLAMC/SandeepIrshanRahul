from re import findall, finditer, sub
import re

# how to match the leading and riding white spaces in the all the line of file
# carret symbole is used to match the patten at the bigining
'''
sentence = "          hi this is     jiya   "  


def _lstrip(line):
    newline = sub(f'^\s+',"",sentence)
    return newline

print(_lstrip(sentence))

def _rstrip(line):
    newline = sub(f'\s+$',"",sentence)
    return newline

print(_rstrip(sentence))

def _strip(line):
    newline = sub(f'(^\s+ | \s+$)',"",sentence)
    return newline

print(_strip(sentence))

# def _lstrip(line):
#     newline = sub(f'^\s+',"",sentence)
#     return newline



# print(_lstrip(sentence))



#how to finde the number present at the starting of string 

sentence = "23532343 heloo world 334423232 my happy holi 56444"

def str_nums(line):
    matches = findall(r'^\d+',sentence)
    res = "".join(matches)
    return f"the len of {res} is {len(res)}"

print(str_nums(sentence))

def end_nums(line):
    matches = findall(r'\d+$',sentence)
    res = "".join(matches)
    return f"the len of {res} is {len(res)}"

print(end_nums(sentence))



#how to find he leading and trailing white space in the line or in file with file handling 
sentence = "       heloo world 334423232 my happy holi     "

def start_num_of_spaces(line):
    matches = findall(r'^\s+',sentence)
    res = "".join(matches)
    return f"the len of {res} is {len(res)}"

print(start_num_of_spaces(sentence))


def end_num_of_spaces(line):
    matches = findall(r'\s+$',sentence)
    res = "".join(matches)
    return f"the len of {res} is {len(res)}"

print(end_num_of_spaces(sentence))

def start_and_end_num_of_spaces(line):
    matches = findall(r'(^\s+|\s+$)',sentence)
    res = "".join(matches)
    return f"the len of {res} is {len(res)}"

print(start_and_end_num_of_spaces(sentence))


#how to get the start  and end index of  3 occurances of hello

sentence = "hello world hello how are you hello my i hello "

matches = finditer(r'hello', sentence)

for index, item in enumerate(matches, start=1):
    print(f"start index : {index}  occurance of 'hello' is {item.start()} and ends at {item.end()}")




sentence = "hello how are you hello how are you hello how are you hello "
matches = finditer(r'hello', sentence)
print("__"*20)
indexs = [(item.start(), item.end()) for item in matches]
print(indexs)

print(f"start index is {indexs[2][0]} and end index is {indexs[2][-1]}")

'''