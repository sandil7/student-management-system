import json
students=[]

try:
    with open("students.json","r")as file:
     students=json.load(file)
except:
     students=[]   

def save_data():
    with open("students.json","w") as file:
        json.dump(students,file,indent=4)  


def add_student():
    name=input("Enter student name:").strip()
    if not name:
        print("Error.Name cannot be empty")
        return
    if not all(c.isalpha() or c.isspace() for c in name):
        print("Error.Name should contain letters only.")
        return
    
    roll=input("Enter roll number:").strip()
    if not roll:
        print("Error.Roll number cannot be empty.")
        return
    
    if not roll.isdigit():
        print("Error.Roll should have numbers only.")
        return
    
  
    for student in students:
        
        if student["roll"]==roll:
            print("Error:Roll number already exists.")
            return    
        

    student={
        "name":name,
        "roll":roll
    }
    students.append(student)
    save_data()
    print("student added sucessfully")

def view_student():
    if not students:
        print("No student found")
        return
    print("\nStudent list:")
    
    students.sort(key=lambda s: int(s['roll']))

    for i,student in enumerate(students,start=1):
        print(f"---------------------")
        print(f"Student {i}")
        print(f"Name : {student['name']}")
        print(f"Roll : {student['roll']}")
        print(f"---------------------")
        print()
        

def search_student():
    roll=input("enter roll number you want to search:")
    
    if not roll:
        print("Error.Roll number cannot be empty.")
        return
    if not roll.isdigit():
        print("Error.Roll should contain digit only.")
        return
    for student in students:
        if student["roll"]==roll:
            print(f"Student found:{student['name']}")
            return
    print("Student not found")
    
def delete_student():
    
    roll=input("enter roll number of student you want to delete:")
    
    if not roll:
        print("Error.Roll number cannot be empty.")
        return
    if not roll.isdigit():
        print("Error.Roll should be digit only.")
        return

    for student in students:
        if student["roll"]==roll:
            students.remove(student)
            save_data()
            print("Student deleted succesfully")
            return
    print("Student not found")

def update_student():
    roll=input("enter roll you want to update:")
    if not roll:
        print("Error.Roll cannot be empty.")
        return
    if not roll.isdigit():
        print("Error.Roll should be numbers only.")
        return
    for student in students:
        if student["roll"]==roll:
            newname=input("enter new name:")
            if not newname:
                print("Error.Newname cannot be empty.")
                return
            if not all(c.isalpha() or c.isspace() for c in newname):
             print("Error. It should contain name only.")
             return
             
            student["name"]=newname
            save_data()
            print("student updated successfully")
            return
    print("Student not found.")

while True:
    print("\n-----Student Management System-----")
    print("1.Add student")
    print("2.View Student")
    print("3.Search Student")
    print("4.Delete Student")
    print("5.Update Student")
    print("6.Exit")

    choice=input("Enter your choice:")
    if choice=="1":
        add_student()
    elif choice=="2":
        view_student()
    elif choice=="3":
        search_student()
    elif choice=="4":
        delete_student()
    elif choice=="5":
        update_student()    
    elif choice=="6":
        print("Good Bye")
        break
    else:
        print("Invalid choice") 





