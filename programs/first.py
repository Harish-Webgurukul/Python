#Calculator 
print("===== Webgurukul =======")

choice=1
while choice==1:
	print("===== Simple Calculator =======")
	num1 = int(input("Enter first Number: "))
	num2 = int(input("Enter second Number: "))
	
	op = int(input("\n1.Add\t 2.Sub \t 3.Multi\t 4.Div"))
	print("Select Operation : ")
	if op==1:
		print("Addition is : ", num1+num2)
	elif op==2:
		print("Substraction is : ", num1-num2)
	elif op==3:
		print("Multiplication is : ", num1*num2)
	elif op==4:
		try:
			print("Division is : ", num1/num2)
		except Exception as e:
			print("Num2 Cannot be zero! Try again")
	else:
		print("Select between 1-4 for operation")
	choice=int(input("Do you want to do more operation: 1-Yes / 0-No"))
else:
	print("\tThank you!")
