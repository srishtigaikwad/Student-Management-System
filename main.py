"""
fields:-['Roll','Name','DOB','E_mail','Phone','X_Board','X_Percent','XII_Board','Stream','XII_Percent']
1.Add New Student
2.View Student
3.Search Student
4.Update Student
5.Delete Student
6.Quit
"""

import csv
#Define globle variables
student_fields=['roll','Name','DOB','E_mail','Phone','X_Board','X_Percent','XII_Board','Stream','XII_Percent']
student_database='student2.csv'

def display_menu():
    print("------------------------")
    print("Welcome to Student Management System")
    print("------------------------")
    print("1.Add New Student")
    print("2.View Student")
    print("3.Search Student")
    print("4.Update Student")
    print("5.Delete Student")
    print("6.Quit")

def add_student():
    print("------------------------")
    print("Add Student Information")
    print("------------------------")
    global student_fields
    global student_database

    student_data = []
    for field in student_fields:
        value=input("Enter" +  field  + ":")
        student_data.append(value)

    with open(student_database,"a",encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerows([student_data])

    print("Data saved successfully")
    input("Press any Key to continue")
    return

def view_student():
    global student_fields
    global student_database

    print("--Student Records--")

    with open(student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        for x in student_fields:
            print(x,end='\t|')
        print("\n-------------------------")

        for row in reader:
            for item in row:
                print(item,end="\t|")
            print("\n")

    input("Press any key to continue")

def search_student():
    global student_fields
    global student_database

    print("--Search Student--")
    roll=input("Enter roll no. to search:")
    with open(student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        for row in reader:
            if len(row)>0:
                if roll==row[0]:
                    print("---Student Found---")
                    print(" Roll:",row[0])
                    print(" Name:",row[1])
                    print(" DOB:",row[2])
                    print(" E_mail:",row[3])
                    print(" Phone:",row[4])
                    print(" X_Board:",row[5])
                    print(" X_Percent:",row[6])
                    print(" XII_Board:",row[7])
                    print(" Steram:",row[8])
                    print(" XII_Percent:",row[9])
                    break
        else:
            print("Student not found in our database")
    input("Press any key to continue")

def update_student():
    global student_fields
    global student_database

    print("--Update Student--")
    roll=input("Enter roll no. to update:")
    index_student=None
    updated_data=[]
    with open(student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        counter=0
        for row in reader:
            if len(row)>0:
                if roll==row[0]:
                    index_student=counter
                    print("Student Found: at index",index_student)
                    student_data=[]
                    for field in student_fields:
                        value=input("Enter"+field+":")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter+=1

    #Check if the record is found or not
    if index_student is not None:
        with open(student_database,"w",encoding="utf-8") as f:
            writer=csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("Roll No. not fount in our database")

    input("Press any key to continue")

def delete_student():
    global student_fields
    global student_database

    print("--Delete Student--")
    roll=input("Enter Roll No. to delete:")
    student_found=False
    update_data=[]
    with open(student_database,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        counter=0
        for row in reader:
            if len(row)>0:
                if roll!=row[0]:
                    update_data.append(row)
                    counter+=1
                else:
                    student_found=True

    if student_found is True:
        with open(student_database,"w",encoding="utf-8") as f:
            writer=csv.writer(f)
            writer.writerows(update_data)
        print("Roll no.",roll,"delete successfully")
    else:
        print("Roll no. not found in our database")

    input("Press any key to continue")

while True:
    display_menu()

    choice=input("Enter your choice:")
    if choice=='1':
        add_student()
    elif choice=='2':
        view_student()
    elif choice=='3':
        search_student()
    elif choice=='4':
        update_student()
    elif choice=='5':
        delete_student()
    else:
        break
print("~~-----------------------~~")
print("Thank you for using our system. \nHave a Nice Day!!")
print("~~-----------------------~~")
