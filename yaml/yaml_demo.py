import yaml

with open("yaml_demo.yml") as f:
	data = yaml.load(f, Loader=yaml.Loader)
print(data)

with open("yaml_write_demo.yml","w") as w:
	yaml.dump(data,w)

data1 = '''
name: RSK
age: 39
'''
a = yaml.load(data1, Loader=yaml.Loader)
print(a)

b = yaml.dump(a, Dumper=yaml.Dumper,indent=2)
print(b)

