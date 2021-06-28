
with open(r'data.txt', 'r') as fo:
	for data in fo.readlines():
		a = data.rsplit(',')
		print("Name: ", a[0])
		print("Roll no: ", a[1])
		print("Address: ", a[2])