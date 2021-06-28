print("Welcome user!")
filename = input("Enter file name: ")


with open(filename+'.txt', 'a') as fo:
	for i in range(1):
		name = input("\nEnter Name: ")
		roll = input("Enter Rollno: ")
		add = input("Enter Address: ")
		data = name+','+roll+','+add+'\n'
		fo.write(data)
	print("Data inserted!")
