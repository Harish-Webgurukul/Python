#Library - Harish
#June 2021
#function



def greet():
    print("Good Morning User!")

#function with return tuple type
def check_vowel(arg):
    vowel ="aeiou"
    l1 = list()
    for ch in arg:
        if ch in vowel:
            l1.append(ch)
    print("Vowel found :", end=" ")
    for i in range(len(l1)):
        print(l1[i], end=" ")
        


#passing dict as an argument
def printDict(arg):
    print("\nDictionary Data as follow: ", end=" ")
    for k, v in arg.items():
        print(k, v)

greet()
check_vowel('welcome user')