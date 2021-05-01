def add(num1, num2):
    answer = num1+num2
    return answer

def sub(num1, num2):
    answer = num1-num2
    return answer

def multi(num1, num2):
    answer = num1*num2
    return answer

def div(num1, num2):
    answer = num1/num2
    return answer

print("Enter two Number")
x = int(input("Enter first numbers"))
y = int(input("Enter second numbers"))
print("Enter operation to perform 1. Add, 2. Sub, 3. Multi, 4. Div")
choice = int(input("Enter choice: "))
if choice==1:
    ans = add(x,y)
elif choice==2:
    ans = sub(x,y)
elif choice==3:
    ans= multi(x,y)
elif choice==4:
    ans = div(x,y)
else:
    printf("Invalid Input")
    ans = 0

print("Op is ", ans)
    
     

    
