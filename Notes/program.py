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

//task
1. Take user input and count number of occurence of vowel.
2. Create empty list append number of vowels from the input string. - repeatation
3. Create an empty list add only one occurence of vowel. - single 
4. Create a program to input student detail with marks of three subject. and Print it with total marks and Percentage. 


#dict

#list1
car = ['bmw', 'audi','skoda']
#list2
owner = ['alok', 'suraj', 'rahul']

for i in range(3):
    print(owner[i], " has ", car[i])

#associative array = php
#python dict

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