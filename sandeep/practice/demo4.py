from json import loads 

json_data = '''
{"fname" : "bill",
"lname" : "gates",
"pay": 1000 }
'''

type(json_data)
python_data = loads(json_data)

print(python_data)
print(type(python_data))
