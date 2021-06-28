#String Function
msg = input("Enter your Message: ")

print(msg.capitalize())
print(msg.upper())
print(msg.islower())
print(msg.endswith('gupta'))
print(len(msg))
print(msg.center(10))


#2June 

a=9
print(a)
print("A = ", a)
print(a, " is value of  a")
print("square of ", a*2)

a =4
b =19
print("Different way to use print")
print(a, b)

print("a = ", a, "b = ", b)

print(a, end="\t")
print(b)

print("Multiple variable")
print(a, b ,sep="#", end=" Line ends!")

#This is comment

"""
multiline comment

"""
print(" this is \n comment")  


#if else

a = 2

if a > 5:
    print("a is greater than 5")

if a < 5:
    print("a is less than 5")
    
#true false
a=4
b = (a==4)
if b:
    print("True condition 1")

x = 10
if x==10:
    print("True condition 2")

if 450:
    print("Check condition 3")


#toggle
#efficient
if a>5:
    print("a is greater than 5")
else:
    print("a is less than 5")


#this is comment

"""

welcome to python
multiline comment

"""

msg = "welcome to python"
ch='z'

if ch in msg:
    print(ch, " found in msg")


if ch not in msg:
    print(ch, " not found in msg")


#user input
msg = input("Enter Message: ")
ch= input("Enter word to search: ")

if ch in msg:
    print(ch, " found in msg")

if ch not in msg:
    print(ch, " not found in msg")

print("Program 1")
#user input
num1 = input("Enter num1: ") #str
num2 = input("Enter num2: ") #str

print(type(num1))
#typecast from str to int
print("Addition is ", int(num1)+int(num2))



print("Program 2")
#user input directly to int
num1 = int(input("Enter num1: ")) #int
num2 = int(input("Enter num2: ")) #int

print(type(num1))
#typecast from str to int
print("Addition is ", num1+num2)
print("Multiplication is ",num1*num2)



print("Program 3")
#user input directly to int
num1 = int(input("Enter num1: ")) #int

if num1>10:
    print("Number is > 10")
if num1<10:
    print("Number is <10")

#toggle condition
if num1>10:
    print("Number is > 10")
else:
    print("Number is <10")



print("Program 4")
#user input directly to int
num1 = int(input("Enter num1: ")) #int

if num1>10:
    print("Number is > 10")
elif num1<10:
    print("Number is < 10")
else:
    print("Number is 10")


print("Program 5")
#user input directly to int
day = int(input("Enter day Number: ")) #int

if day==1:
    print("Monday")
elif day==2:
    print("Tuesday")
elif day==3:
    print("Wednesday")
elif day==4:
    print("Thursday")
elif day==5:
    print("Friday")
elif day==6:
    print("saturday")
elif day==7:
    print("Sunday")
else:
    print("Invalid")


print("Program 2")
#user input directly to int
num = int(input("Enter Number: ")) #int

if num>10:
    if num%2==0:
        print(">10 and even")
    else:
        print(">10 and odd")
else:
    if num%2==0:
        print("<10 and even")
    else:
        print("<10 and odd")
        


a=5

if a>5:
    print("a is greater than 5")
elif a<5:
    print("a is less than 5")
else:
    print("a is equal to 5")


a=36
op =a&1

if op==1:
    print("Number is odd")
else:
    print("Number is even")



a=input("Enter number :")

op =int(a)&1

if op==1:
    print("Number is odd")
else:
    print("Number is even")



a=int(input("Enter number :"))

op =a&1

if op==1:
    print("Number is odd")
else:
    print("Number is even")


msg = "hello welcome to python"

ch = "y"
if ch in msg:
    print(ch, " found")
else:
    print(ch, " not found")



msg = "hello welcome to python"

ch = "x"
if ch not in msg:
    print(ch, "not found")
else:
    print(ch, " found")


a = 21

if a%2==0:
    print(a, " is even")
    if a>10:
        print(a, " greater than 10")
    else:
        print(a, " is less than 10")
else:
    print("Odd")



#intialisation
i=0

#condition
while i<=10:
    print(i)
    i=i+2

#increment and decrement


#loop-Print Even Number
#while
i=0
while i<10:
    if i%2==0:
        print(i)
    i=i+1

#loop
#while
i=0
total=0

while i<=10:
    total=total+i #adding previous value with cur i
    print("i=", i)
    print("total", total, end="\n\n")
    i=i+1

print("Sum is ",  total)



#calci
#while loop with else
num = 1
total= 0
while num!=0:
    num=int(input("Enter number: "))
    total = total+num
    print("Sum is ", total)
else:
    print("Thank You!")
    



#for loop
for i in range(5):
    print(i)

#for loop
print("start and end")
for i in range(4, 10):
    print(i)


#for loop
print("start, stop,  step")
for i in range(1, 10, 2):
    print(i)

#for loop reverse
print("start, stop,  step reverse")
for i in range(10, 0, -1):
    print(i)




#for loop
for i in range(5):
    for j in range(5):
        print("i=",i, "j= ", j, end=" ")
    print()

#for loop
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()


#for loop
for i in range(5):
    for j in range(5, i, -1):
        print("*", end=" ")
    print()



#string and for

msg = "welcome to python"
for ch in msg:
    print(ch)


#string and for
msg = "welcome to python"
for ch in msg:
    if 'a' in ch:
        print("a found")
    elif 'e' in ch:
        print("e found")
    elif 'i' in ch:
        print("i found")
    elif 'o' in ch:
        print("o found")
    elif 'u' in ch:
        print("u found")
    else:
        pass

     
print("efficient Code")    
#string and for
msg = "welcome to python"
vowel = "aeiou"
for ch in msg:
    if ch in vowel:
        print(ch, " found")      
        

        
print("efficient Code")    
#string and for
msg = "welcome to python"
vowel = "aeiou"

for ch in msg: #in work as right to left
    if ch in vowel: #check from left to right
        print(ch, " found")
        


#python:list - array in php
#to create empty list
l = list()

#list with data
l1 = [2,3,4,545,5, 'harish']

#type cast from str to list
msg= "welcome"
l1 = list(msg)
print(type(l1))
print(l1)

#program
msg="welcome user"
vowel="aeiou"

print("Using String")
#str
for i in range(2, 9):
    print(msg[i])

print("Using List")
#list
l1 = list(msg)
for i in range(2, 9):
    print(l1[i])


msg="welcome user"
vowel="aeiou"

print("Using String")
#str
for i in range(2, 9):
    print(msg[i])

print("Using List")
#list
l1 = list(msg)
print(type(msg))
print(type(l1))
print(l1)
for i in range(2, 9):
    print(l1[i])

l2 = l1[0:7];
print(l2)
print(type(l2))


#string function
msg= "hi"
l1 = list(msg)
print(l1)

l1.append('u')
print(l1)


l1.clear()
print(l1)

msg= "hi hi"
l1 = list(msg)
msg2="bye"
l2=list(msg2)

a = l1.count('e')
print(a)

l1.extend(l2)
print(l1)

a = l1.index('b')
print(a)

print(l1.pop(1)) #last element
print(l1) #specific index location

print(l1.remove('h'))
print(l1)

l1.reverse()
print("reverse", l1)

l1.sort()
print("Ascending", l1)

l1.sort(reverse=True)
print(" Descending", l1)





#Create student List

l1=list()

#student name

op='y'
while op=='y':
    stuName = input("Enter Name: ")
    l1.append(stuName)
    op = input("Do you want to add more name(y/n): ")

print(l1)


#data appending
l1=[ ['a','b'],
     ['c', 'd']
    ]
print(l1)
print(l1[1][0])

l2 = list(list())
#adding single element
l2.append('a')
print(l2)

#appending list
l2.append(['a', 'b'])
print(l2[1][1])




l2 = list()
i=0
while i<3:
    l3=list()
    stuName = input("Enter Student name: ")
    mark1 = int(input("Enter marks of sub1"))
    mark2 = int(input("Enter marks of sub2"))
    mark3 = int(input("Enter marks of sub3"))
    l3 = [stuName, mark1, mark2, mark3]
    l2.append(l3) #append list to l2
    i=i+1


print(l2)


//task
1. Take user input and count number of occurence of vowel.
2. Create empty list append number of vowels from the input string. - repeatation
3. Create an empty list add only one occurence of vowel. - single 
4. Create a program to input student detail with marks of three subject. and Print it with total marks and Percentage. 



#Program for total and percentage
l2 = list()
count = int(input("Enter student Count: "))
i=0
while i<count:
    l3=list()
    stuName = input("\nEnter Student name: ")
    mark1 = int(input("Enter marks of sub1"))
    mark2 = int(input("Enter marks of sub2"))
    mark3 = int(input("Enter marks of sub3"))
    l3 = [stuName, mark1, mark2, mark3]
    l2.append(l3) #append list to l2
    i=i+1

print(l2)

for i in range(count):
    total=percentage=0
    print("\nStudent Name: ", l2[i][0])
    total = l2[i][1]+l2[i][2]+l2[i][3]
    print("Total Marks: ", total)
    print("Percentage: ", (total/3))


#Program 2
l1 = list()
count = int(input("Enter student Count: "))

i=0
while i<count:
    name = input("enter the name:")
    mark1 = int(input("enter the mark: "))
    mark2 = int(input("enter the mark: "))
    mark3 = int(input("enter the mark: "))
    total = mark1 + mark2 + mark3
    percentage = total/3
    l2 = [name, mark1, mark2, mark3, total, percentage]
    l1.append(l2)
    i=i+1
    
print(l1)

for z in range(count):
    print("name of student: ", l1[z][0])
    print("name of total: ", l1[z][4])
    print("name of percentage: ", l1[z][5])


#tuple
#tuple = constant list
vowel = ('a','e', 'i', 'o', 'u')
msg = "Welcome user"

for ch in msg:
    if ch in vowel:
        print(ch, 'vowel found')


#dict

#search key inside dict
if 'a' in vowel:
    print("key a found")

#list1
car = ['bmw', 'audi','skoda']
#list2
owner = ['alok', 'suraj', 'rahul']

for i in range(3):
    print(owner[i], " has ", car[i])

#associative array = php
#python dict

#dict
vowel ={} #empty
vowel['i']=0 #it create key and value


owner = {'alok':'bmw',
         'suraj':'audi',
         'rahul':'skoda'}

for key,value in owner.items():
    print(key, " has ", value)

#only keys
for key in owner.keys():
    print(key)

#only values
for v in owner.values():
    print(v)

    #dict    

d = dict()
print(d)
d.setdefault(0, 'rahul');
print(d)

for k,v in d.items():
    print(k, v)


    
#dict    

vowel = "aeiou"
d ={'a':0,'e':0, 'i':0, 'o':0, 'u':0}

msg = input("Enter String: ")

for ch in msg:
    if ch in d:
        d[ch]=d[ch]+1

print(d)


#task only display found vowel inside dict
#dict    

vowel = "aeiou"
d ={'a':1}

msg = input("Enter String: ")

for ch in msg:
    if ch in d:
        d[ch]=d[ch]+1

print(d)

#dict display only specific vowel
vowel ={}
msg = input("Enter String : ")
v = "aeiou"

for ch in msg:
    if ch in v:
        if ch not in vowel: #key create
            vowel[ch]=0
        vowel[ch] =vowel[ch]+1


print(vowel)
        



#set

vowel = "aeiou"
msg = "hello user"
s1 = set(vowel)
s2 = set(msg)

s3 = s1.intersection(s2)
print(s3)

#list
#tuple
#dict
#set

vowel = "aeiou"
msg = "hello user"
s1 = set(vowel)
s2 = set(msg)

s3 = s1.intersection(s2)
print(s3)



1.  Input name, roll no, marks of three subject
    for 3 students,
    calculate 
    Percentage and display information

{0: ['rahul', 23, 39,3,3]}

2. Use empty dictionary and add matched vowel with the given string
{'a':0}


#simple Function
#function declaration

def a():
    print("=====================")
#function call
a()

#function with argument

def greet(arg):
    print("Good Morning", arg)


name = input("Enter your name: ")
greet(name)

#function with argument

def greet(arg):
    if arg>=6 and arg<=12:
        print("Good Morning Sir")
    elif arg>=13 and arg<=17:
        print("Good Evening Sir!")
    else:
        print("Good Night Sir")


t = int(input("What is time? 24Hours: "))
greet(t)


#function with default argument 
#calculator
def add(x=0, y=0):
    print("Addition is ", x+y)


def sub(x=0, y=0):
    print("Substraction is ", x-y)


num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
op = int(input("1.Add 2.Sub: "))

if op==1:
    add(num1, num2)
elif op==2:
    sub(num1, num2)
else:
    print("Invalid input")

#function with default argument 
#repeatation
op = 'y'
while op=='y':
    name = input("Enter Name: ")
    print("Welcome ", name)
    op=input("Do you want to cntd(y/n)")


#function with default argument 
#calculator
def add(x=0, y=0):
    print("Addition is ", x+y)


def sub(x=0, y=0):
    print("Substraction is ", x-y)

choice='y'
while choice=='y':
    num1 = int(input("Enter Number 1: "))
    num2 = int(input("Enter Number 2: "))
    op = int(input("1.Add 2.Sub: "))
    if op==1:
        add(num1, num2)
    elif op==2:
        sub(num1, num2)
    else:
        print("Invalid input")
    choice = input("Do you want to cntd(y/n)!")


#while with else
#while not print else when explicity break the loop

i=0
while i<10:
    print(i)
    if i==5:
        break
    i=i+1
else:
    print("Thank You!")


#while with else
i=0
while i<10:
    print(i)
    i=i+1
else:
    print("Thank You!")


#function with return type

def pi_value():
    return 3.14

area = pi_value()*4*4
print("Area of circle is ", area)



#function with return type

def swap(x):
    return x.swapcase()
    
name = input("Enter name : ")
print(swap(name))

#Type of Function
#simple function
#function with argument
#function with return type
#function with argument and return type
#function with default argument

#passsing string as an argument

def fun1(arg):
    print("argument is ", arg)


fun1("harish")


#passing list as an argument
def fun1(arg):
    print("argument is ", arg)
    length = len(arg)
    for i in range(length):
        print("Element ", arg[i])
        

l1 = ['a', 'b', 'c', 34]
fun1(l1)


#passing dict as an argument
def fun1(arg):
    print("argument is ", arg)
    for k, v in arg.items():
        print("Element ", k, v)
        
l1 = {'a':9, 'b':7, 'c':0}
fun1(l1)





#check vowel normal
def check_vowel(arg):
    vowel ="aeiou"
    for ch in arg:
        if ch in vowel:
            print("vowel found", ch)
        
msg = input("Enter Message: ")
check_vowel(msg)


#function with return tuple type
def check_vowel(arg):
    vowel ="aeiou"
    l1 = list()
    for ch in arg:
        if ch in vowel:
            l1.append(ch)
    return tuple(l1)
        
    

msg = input("Enter Message: ")
result = check_vowel(msg)
print(result)




#Modules
#import harishlib

harishlib.greet()
harishlib.check_vowel("Hello")
harishlib.printDict({'a':0, 'b':0})

#class and Object
a=5
b=a
print(a)
print(type(a))
print(id(a))


print("b data")
print(b)
print(type(b))
print(id(b))
b=9

print(b)
print(type(b))
print(id(b))


#class and object
#this is comment

class Bike():
    #global variable
    name = ""

    """This class contain info about bike"""
    def fun(obj):
        print("Bike name is ", obj.name)
        

chintu = Bike()
pintu = Bike()
chintu.name = "apache"
pintu.name = "pulsar"

chintu.fun()
pintu.fun()


#class and object
#this is comment
#calci
class Calci():
    num1=""
    num2=""

    def add(self):
        self.num1 = int(input("Enter num1 :"))
        self.num2 = int(input("Enter num2 :"))
        print("Sum is ", self.num1+self.num2)


obj = Calci()
obj.add()    #Calci.add(obj)


#class and object
#calci2
class Calci():
    num1=""
    num2=""

    def add(self):
        self.num1 = int(input("Enter num1 :"))
        self.num2 = int(input("Enter num2 :"))
        print("Sum is ", self.num1+self.num2)


    def sub(self):
        self.num1 = int(input("Enter num1 :"))
        self.num2 = int(input("Enter num2 :"))
        print("Sub is ", self.num1-self.num2)

obj = Calci()
op = int(input("Select Operation 1.Add 2.Sub"))

#Calci.add(obj)
if op==1:
    obj.add()
elif op==2:
    obj.sub()
else:
    print("Invalid Input")


#class and object
#full calci
class Calci():
    num1=""
    num2=""

    def __init__(self):
        e=9
        print("Enter Number:")
        self.num1 = int(input("Enter num1 :"))
        self.num2 = int(input("Enter num2 :"))

    def add(self):
        print("Sum is ", self.num1+self.num2)

    def sub(self):
        print("Sub is ", self.num1-self.num2)

    def multi(self):
        print("Multi is ", self.num1*self.num2)

    def div(self):
        print("Div is ", self.num1-self.num2)


obj = Calci() #constructor call

op = int(input("Select Operation 1.Add 2.Sub 3.Multi 4.Div: "))

#Calci.add(obj)
if op==1:
    obj.add()
elif op==2:
    obj.sub()
elif op==3:
    obj.multi()
elif op==4:
    obj.div()
else:
    print("Invalid Input")


#constructor with argument
class Calci():
    def __init__(self, a,b):
        print("constructor")
        print("sum =  ", a+b)

obj1 = Calci(4, 5) #it gets call when object is created



#class and object
#function inside function 
class Calci():
    def __init__(self, a,b):
        print("constructor")
        print("sum =  ", a+b)
        self.display()

    def display(self):
        #throw None in print function
        print("Display function = ", self.pi_v())

    def pi_v(self):
        print("pi value")

obj1 = Calci(4, 5) #it gets call when object is created

#inhertance
#basic example
class A():
    num1=""
    def showdata(self):
        print("Showdata")

#class B inhert class A
class B(A):
    def display(self):
        print("Display Data")


obj = B()
obj.showdata()
obj.display()


#inhertance
#base class -= redundancy
class Vehicle():
    company=""
    tyre =""
    category=""
    cc=""

#derive class
class Bike(Vehicle):

    def getdata(self):
        self.company = input("Comapany : ")
        self.tyre = input("tyre : ")
        self.name = input("Bike name : ")
        self.cc = input("cc : ")

    def showdata(self):
        print("\nCompany", self.company)
        print("tyre", self.tyre)
        print("Bike name", self.name)
        print("cc", self.cc)

obj = Bike()
obj.getdata()
obj.showdata()


#inhertance
#constructor call
class Vehicle():
    def __init__(self):
        print(" base class Constructor ")

    company=""
    tyre =""
    category=""
    cc=""

#derive class
class Bike(Vehicle):
    def __init__(self):
        #to call base class constructor 
        super(Bike, self).__init__()
        print(" Derive class Constructor ")
    
    def getdata(self):
        self.company = input("Comapany : ")
        self.tyre = input("tyre : ")
        self.name = input("Bike name : ")
        self.cc = input("cc : ")

    def showdata(self):
        print("\nCompany", self.company)
        print("tyre", self.tyre)
        print("Bike name", self.name)
        print("cc", self.cc)

obj = Bike() #will call bike class constructor
obj.getdata()
obj.showdata()



#File Handling
fo = open('data.txt', 'r')
a = fo.readline()
print(type(a))
print(a)
fo.close()

#file handling 
fo = open('data.txt', 'r')
#this will read whole file
#a = fo.read()

#read only 10 characters
#a = fo.read(10)

#read line one  by one
a = fo.readline()

print(a)
fo.close()


#file handling - write mode
fo = open('data.txt', 'w')

msg = "New Data"
fo.write(msg)
print("file written")
fo.close()

#file handling 
fo = open('data.txt', 'a')

msg = "\tNew Data Appended"
fo.write(msg)
print("file append")
fo.close()

#file handling  - raw data name
fo = open(r'E:\new.txt', 'w') #r is raw data- \n \t 
 
msg = "\tNew Data Appended"
fo.write(msg)
print("file append")
fo.close()


#contextual
with open('data.txt', 'w') as fo:
    fo.write("Hello User!");
    print("data write")


#file data read and write

with open(r'data.txt', 'r') as fo:
    data = fo.read()#string 
    data = data.rsplit('\n')
    for i in range(3):
        a = data[i].rsplit(',')
        print("\n User data")
        print('Name: ', a[0])
        print('Roll No: ', a[1])
        print('Address: ', a[2])
    

with open(r'data.txt', 'w') as fo:
    for i in range(3):
        name = input("\nEnter Name: ")
        roll = input("Enter Rollno: ")
        add = input("Enter Address: ")
        data = name+','+roll+','+add+'\n'
        fo.write(data)
    print("Data inserted!")
