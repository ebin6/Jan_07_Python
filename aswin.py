students={}

def add_student():
    id=input("enter id: ")
    name=input("enter name: ")
    age=int(input("enter age: "))



    marks={}
    num_subject=int(input("number of subject: "))
    for s in range(num_subject):
        subject=input("enter subject name: ")
        mark=int(input("enter mark: "))
        marks[subject]=mark

    detail={}
    detail["name"]=name
    detail["age"]=age
    detail["marks"]=marks
    students[id]=detail


def show_students():
    for student in students:
        print("id : ",student)
        print("name : ",students[student]["name"])
        print("age : ",students[student]["age"])
        print("marks : ",students[student]["marks"])

def all():
    while True:
        print("<<<< students management system>>>>")
        print("1.add student")
        print("2.show student")
        print("3.exit")

        choice = int(input("Enter your choice: "))
        if choice==1:
            add_student()
        elif choice==2:
            show_students()
        elif choice==3:
            print("Exiting ...")
            break


print(students)

all()
