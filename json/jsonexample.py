#Java script object notation
import json

employee = '''
[
	{
		"name": "rsk",
		"no": 1234,
		"salary": 3000,
		"is_manager": true,
		"provident_fund": 
		{
			"epf": [1000,2000,3000,4000],
			"vpf": [1000,2000,3000,4000]
		}
	},
	{
		"name": "anitha",
		"no": 5678,
		"salary": 2000,
		"is_manager": false,
		"provident_fund": 
		{
			"epf": [1000,2000,3000,4000],
			"vpf": [1000,2000,3000,4000]
		}
	}
]
'''

#convers json file to python string and print it
data = json.loads(employee)

for item in data:
	print(item['name'],item['no'], item['salary'])
	del item['no']
	print(item)


#convert python string back to json and print it
new_data = json.dumps(data,indent = 2)
print(new_data)

