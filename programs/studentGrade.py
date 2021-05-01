import statistics
studentGrades = {}

def enterGrade():
    i1 = input('Student Name: ')
    i2 = int(input('Grade: '))
    try:
        if studentGrades[i1]:
            studentGrades[i1].append(i2)
    except KeyError as t:
        studentGrades[i1] = []
        studentGrades[i1].append(i2)
    print(len(studentGrades))


def removeGrade():
    nameToRemove = input('Enter name to remove?')
    del studentGrades[nameToRemove]
    print(studentGrades)

def studentAverage():
    i1 = input('Enter name to calculate average?')
    x = statistics.mean(studentGrades[i1])
    print('Average of ',x)

userInput=5
while(userInput):
    print("\n Welcome to Grade Central system")
    print("[1] - Enter Grades")
    print("[2] - Remove Students")
    print("[3] - Student Average Grades")
    print("[4] - Enter Grades")
    userInput = int(input("What would you like to do today? (Enter a number)"))
    if userInput==1:
        enterGrade();
    elif userInput==2:
        removeGrade();
    elif userInput==3:
        studentAverage();
    else:
        print('Programs ends! Thank you')
        break
