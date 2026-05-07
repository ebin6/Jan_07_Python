# file=open("Student_details.txt","a")

# std_count=int(input("Enter how many students details you wish to store : "))
# for k in range(std_count):
#     name=input("Enter student name : ")
#     age=int(input("Enter student age : "))
#     course=input("Enter student course : ")
#     file.write(f"{name},{age},{course}\n")
 

with open("Student_details.txt","r") as file:
    """
    readlines sets each lines inside list -->  ["Anu,28,Digital Marketing\n","Tesna ,19,Python\n"]
    """
    data=file.readlines() 
    for std in data:
        std_data=std.split(",")  # ["Anu",28,"Digital Marketing"]
        print("Name :",std_data[0])
        print("Age : ",std_data[1])
        print("Course : ",std_data[2])
print("File closed ")


