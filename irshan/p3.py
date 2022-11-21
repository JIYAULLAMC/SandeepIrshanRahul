from re import findall

vars = [
('http://www.google.com/base/feeds/snippets/11448761432933644688', {"from":"2020-06-09", "to":"2020-06-30"}, 
{"home", "index", "game"}, 
'spanish vocabulary builder "expand your vocabulary! contains fun lessons that both teach and entertain you\' 11 quickly find yourself mastering new terms. includes games and more!" '),


('http://www.yahoo.com/base/feeds/snippets/8175198959985911471',{"from":"2019-10-09", 'to':'2019-10-29'}, 
{'drawing', "music", "dance"}, 
'topics presents: museums of world "5 cd-rom set. step behind the velvet rope to examine some of the most treasured collections of antiquities art and inventions. includes the following the louvre virtual visit 25 rooms in full screen interactive video detailed map of the louvre ..." '),


('http://www.facebook.com/base/feeds/snippets/18445827127704822533', {"from":"2021-04-09", 'to':'2021-04-30'}, 
{"animation","photography"}, 
'sierrahome hse hallmark card studio special edition win 98 me 2000 xp "hallmark card studio special edition (win 98 me 2000 xp)sierrahome"'),]

#-----------------------------------------------------------
# for var in vars : 
#     day1 = int(var[1]['from'][-1:-3:-1][: :-1])
#     day2 = int(var[1]['to'][-1:-3:-1][: : -1])
#     print(day2-day1)

#--------------------------------------------------------------
# strvar = str(vars)
# words = findall(r"[\w]+", strvar)
# no_of_words = len(words)
# no_chrecters = len(strvar)
# sp_chars = findall(r"[^\w]", strvar)
# no_special_chars = len(sp_chars)


#-------------------------------------------------
# words = findall(r"[\w]+", strvar)




def sort_set(item):
    return sorted(item)


all_sets = []

for var in vars:
    all_sets.append(sort_set(var[2]))


print(all_sets)


out = [[len(_set )for _set in mysets] for mysets in all_sets]

print(out)


'''
1) find out the no of days available in each web link.
output format: ('google':no of days (int), 'yahoo' :no of days(int), "facebook" :no of days (int))
2) find out the no of words, no of characters and no of special symbols in entire Input.
3) extract all the words from the given input and store them in the from list.
4) sort all the strings present inside each and every set from the given input and store them in the form of list based on length.
example:
input ("hai','ab", "mysore') outputs("ab","hai", "mysore"}
6343
'''