studentid = []
studentname = []
studentdob = []
courseid = []
coursename = []
mark = []
numberofstudent = 0
numberofcourse = 0

# input number of student and student's information
def inputstudent():
    a = int(input("How many student would you like to add? "))
    print("----------------------------------------------------")
    if (a<0): 
        print("Invalid input")
        print("----------------------------------------------------")
        return 0
    else:
        global numberofstudent
        numberofstudent+=a
        for i in range(a):
            id = str(input(f"Enter the id of student number {i+1}: "))
            studentid.append(id)
            name = str(input(f"Enter the name of student number {i+1}: "))
            studentname.append(name)
            dob = int(input(f"Enter the DOB of student number {i+1}: "))
            studentdob.append(dob)
            print("----------------------------------------------------")
        return 0

# Input the number of course and course's information
def inputcourse():
    a = int(input("How many course would you like to add? "))
    print("----------------------------------------------------")
    if (a<0):
        print("Invalid input")
        print("----------------------------------------------------")
        return 0
    else:
        global numberofcourse
        numberofcourse+=a
        for i in range(a):
            id = str(input(f"Enter the id of the course {i+1}: "))
            courseid.append(id)
            name = str(input(f"Enter the name of the course {i+1}: "))
            coursename.append(name)
            print("----------------------------------------------------")
            mark.append(0)
            # This final line is for the mark array can have a list for mark
        return 0
        
# Input mark for a specific course
def inputmark():
    if (courseid == 0):
        print("There aren't any course at here, please input the course information first")
        print("----------------------------------------------------")
        return 0
    elif (studentid == 0):
        print("There aren't any student in the class, please input the student informaton first")
        print("----------------------------------------------------")
        return 0
    else:
        b = []
        course = int(input("Type the id of the course you would like to input mark: "))
        print("----------------------------------------------------")
        courseposi = courseid.index(str(course))
        for i in range(numberofstudent):
            a = int(input(f"Input the mark for {studentid[i]}: "))
            b.append(a)
        mark[courseposi] = b
        print("----------------------------------------------------")
        return 0

# List course
def listcourses():
    if (numberofcourse == 0):
        print("You don't have any course, please input the courses information first")
        print("----------------------------------------------------")
        return 0
    else:
        for i in range(numberofcourse):
            print(f"{courseid[i]} {coursename[i]}")
        print("----------------------------------------------------")
        return 0

# List student
def liststudent():
    if (numberofstudent == 0):
        print("You don't have any student, please input the student information first")
        print("----------------------------------------------------")
        return 0
    else:
        for i in range(numberofstudent):
            print(f"{studentid[i]} {studentname[i]} {studentdob[i]}")
        print("----------------------------------------------------")
        return 0

# Show student mark for a specific course
def listmark():
    if (numberofcourse == 0 or numberofstudent == 0):
        print("There are not any student or course, please input the information of student and course then input the mark")
        print("----------------------------------------------------")
        return 0
    else:
        a = int(input("Please enter id of the course you would like to show the mark: "))
        print("----------------------------------------------------")
        if (courseid.index(str(a))):
            b = courseid.index(str(a))
            if (mark[b] == 0):
                print("You didn't input the mark for this course, please input the mark first")
                print("----------------------------------------------------")
                return 0
            else:
                for i in range(numberofstudent):
                    print(f"{studentid[i]} {studentname[i]} {mark[b][i]}")
                print("----------------------------------------------------")
                return 0
        else:
            print("There are not any id for this corse")
            return
        return 0

while True:
    print("Which operation would you like to do? ")
    print("1. Input student information")
    print("2. Input course information")
    print("3. Input marks for a course")
    print("4. List course")
    print("5. List student")
    print("6. Show student mark")
    print("7. Exit program")
    oper = int(input("Please input the operation you want to do: "))
    print("----------------------------------------------------")
    match oper:
        case 1:
            inputstudent()
        case 2:
            inputcourse()
        case 3:
            inputmark()
        case 4:
            listcourses()
        case 5:
            liststudent()
        case 6:
            listmark()
        case 7:
            break
print("----------------------------------------------------")
print("Have a nice day!")