students={}

def addStudent():
    student_id=int(input("Enter the student id : "))
    student_name=input("Enter student name : ")
    age=int(input("Enter student age : "))


    marks={}
    subject_count=int(input("How many subject marks you wish to enter ? "))
    for i in range(subject_count):
        subject_name=input("Enter subject name : ")
        sub_mark=int(input("Enter the subject mark : "))
        marks[subject_name]=sub_mark
    
    std_detail={}
    std_detail["name"]=student_name
    std_detail['age']=age
    std_detail["marks"]=marks
    

    students[student_id]=std_detail
    
    print(students)

def show_students():
    for student in students:
        print("id : ",student)
        print("name : ",students[student]["name"])
        print("age : ",students[student]["age"])
        print("marks : ",students[student]["marks"])

def removeStudent():
    std_id=int(input("Enter the student id whcih is to be removed : "))
    students.pop(std_id)
    print("Item removed successfully")
while True:
    print("1. Add Student\n2. View all students\n3. Delete Students\n4.Exit")
    choice=int(input("Enter your choice (1,2,3,4) : "))
    if choice==1:
        addStudent()
    elif choice==2:
        show_students()
    elif choice==3:
        removeStudent()
    elif choice==4:
        print("Exiting")
        break