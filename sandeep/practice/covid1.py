from csv import DictReader
from collections import defaultdict

#open the file and saving in object

# to read the data from the file and strore in the generator object
def read_csv():        
    with open(r"C:\Users\JiyaUlla\Desktop\python\sandeep\rawdata\covid-data.csv", 'r') as file_obj:
        data = []
        genobj = DictReader(file_obj) 
        for row in genobj:
           data.append({"contry": row['location'], "date":row['date'], 'new_cases':int(row['new_cases'])})
        return data 
#find the total cases in the worldwide
def total_cases():
    data = read_csv()
    total = 0
    for row in data:
        total += row['new_cases']
    return total

#  calculate number of cases in each contry
def contry_total_cases():
    data = read_csv()
    contry_cases_pair = defaultdict(int)
    for row in data:
        contry_cases_pair[row['contry']] += row['new_cases']
    return sorted(contry_cases_pair.items(), key= lambda item: item[1])

#used to find the total number of unique contries present in the list
def unique_contry():
    data = read_csv()    
    return {row['contry']  for row in data }

print(len(unique_contry()))





