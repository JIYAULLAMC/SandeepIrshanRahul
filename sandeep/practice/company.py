from csv import reader, DictReader
from collections import defaultdict

# how to read the file from the given path
with open("C:\\Users\\JiyaUlla\\Desktop\\python\\sandeep\\rawdata\\company.csv", 'r') as r_obj:
    for line in r_obj:
        print(line)


with open("C:\\Users\\JiyaUlla\\Desktop\\python\\sandeep\\rawdata\\company.csv", 'r') as r_obj:
    data = reader(r_obj)
    #helped to not show the titles
    next(data)
    for line in data:
        print(line)




#how to read the data from the csv file and store into an separate object in
#in the form of the lists


# #how to read the data from the csv file and store into an separate object in
# #in the form of the lists
def read_csv():  
    data = []      
    with open("C:\\Users\\JiyaUlla\\Desktop\\python\\sandeep\\rawdata\\company.csv", 'r') as r_obj:
        file_obj = reader(r_obj)
        for line in file_obj:
            data.append(line)
    return data 


# reading the content form the file and storing in the form of dictionary
def read_as_dict():
    data = []
    with open(r"C:\Users\JiyaUlla\Desktop\python\sandeep\rawdata\company.csv", "r") as r_obj:
        dict_obj = DictReader(r_obj)
        for line in dict_obj:
            data.append(line)
    return data 


#fetch the name of the employees
def read_names():
    data = read_as_dict()
    names = []
    for record in data:
        names.append(record['name'])
    return names

# total sum of all employees payment
def total_payment():
    data = read_as_dict()
    total_pay = 0
    for row in data:
        total_pay += int(row['pay'])
    return total_pay

#how much male and female working
def gender_count():
    data = read_as_dict()
    genders = defaultdict(int)
    for row in data:
        gender = row['gender']
        genders[gender] += 1
    return dict(genders)


#sort the employees based on the payment
def sort_emps():
    data = read_as_dict()
    pay_data = sorted(data, key=lambda record : int(record['pay']))
    return pay_data

#highest pay get by emp
def top_pay_emp():
    data = sort_emps()
    return data[-1]

#lowest pay get by emp
def low_pay_emp():
    data = sort_emps()
    return data[0]

