list1 = [ 1, 2, 3, 'a', 'b', 'c']

dic = {}

for i in list1:
	if type(i)==int:
		dic[i]= i
	elif type(i)==str:
		dic[i] = i
	else:
		dic[i] = i

print(dic)


dic1 = {}
intcount = 0
strcount = 0
othercount = 0

for i in list1:
	if type(i)==int:
		intcount = intcount+1
		dic1['intcount'] = intcount
	elif type(i) == str:
		strcount = strcount +1
		dic1['strcount'] = strcount
	else :
		othercont = othercount + 1
		dic1['othercount'] = othercount

print(dic1)

		


