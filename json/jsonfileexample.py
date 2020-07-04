#Java script object notation
import json

#convers json file to python string and print it
with open('employee.json') as f:
	data = json.load(f)

#move the dictionary to new dictionary from the master list "data"
for i in range(len(data)):
	data[i]['new_no'] = data[i]['no']
	print(data)

#delete the unwanted dictionary
for item in data:
	del item['no']
	del item['provident_fund']['vpf']


#convert python string back to json and print it
with open('new_employee_db.json', 'w') as f:
	json.dump(data,f,indent = 2)
	
