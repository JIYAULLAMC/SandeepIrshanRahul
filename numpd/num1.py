from json import loads , dumps
import json

json_data = ''' {"fname" : "bill","lname" : "gates","pay": 1000 }'''

python_data = loads(json_data)

print(python_data)
print(type(python_data))


json_data = dumps(python_data)
print(json_data)
print(type(json_data))
