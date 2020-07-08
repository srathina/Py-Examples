
#directly open the file, read and print it
#by default file open as read only.
f = open("Address.txt")
text = f.read()
f.close()
print(text)
print("\n")

#open the file using with keyword where we dont need to call file close 
#explicity as python does that for us.
with open("Address.txt") as fobj:
	text = fobj.read()
print(text)
print("\n")

#using try and except method when try to open the file that is not available.
try:
	with open("file1.txt") as nobj:
		text = nobj.read()
	print(text)
except:
	print("FileNotFound")

print("\n")

#file write
Oceans = ['pacific', 'artic', 'antartic', 'indian', 'southern']

with open("oceans.txt", "w") as f:
	for ocean in Oceans:
		f.write(ocean)
		f.write("\n")

#another way to write the files using print with file paramter
#another way to open the file using append method to append the content.
with open("oceans.txt","a") as f:
	print("There are 5 oceans", file=f)