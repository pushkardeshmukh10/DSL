'''Create a Student Record Management System using linked list 
• Use a singly/doubly linked list to store student data (Roll No, Name, Marks). 
• Perform operations: Add, Delete, Update, Search, and Sort. 
• Display records in ascending/descending order based on marks or roll number.'''
class Student:
    def __init__(self,roll_no,name,mrks):
        self.roll_no = roll_no
        self.name = name
        self.mrks = mrks
        self.next = None
class Node:
    def __init__(self):
        self.head = None
    def add_student(self,roll_no,name,mrks):
        new_node = Student(roll_no,name,mrks)
        if self.head is None:
            self.head = new_node
        else:
            crt = self.head
            while crt.next:
                crt = crt.next
            crt.next = new_node
        print("Student record Added.")
    def delete_stdt(self,roll_no):
        crt = self.head
        prv = None
        while crt:
            if crt.roll_no == roll_no:
                if prv:
                    prv.next = crt.next
                else:
                    self.head = crt.next
                print("Student Record is Deleted")
                return
            prv = crt
            crt = crt.next
        print("Student Not Found")
    def display(self):
        if self.head is None:
            print("No Student records found")
            return
        crt = self.head
        print("---------STUDENT RECORD---------")
        while crt:
            print(f"Roll No:- {crt.roll_no}, Name:- {crt.name}, Marks:- {crt.mrks}")
            crt = crt.next
    def update(self, roll_no, new_name, new_marks):
        crt = self.head
        while crt:
            if crt.roll_no == roll_no:
                crt.name = new_name
                crt.mrks = new_marks
                print("Student record updated.")
                return
            crt = crt.next
        print("Student not found.")
    def search(self,roll):
        crt = self.head
        while crt:
            if crt.roll_no == roll_no:
                print(f"Found: Roll No: {crt.roll_no}, Name: {crt.name}, Marks: {crt.mrks}")
                return            
                crt = crt.next
        print("Student not found.")
            
    def menu(self):
        while True:
            print("*********MENU**********")
            print("1. Add Student Details:")
            print("2. Delete Student Details:\n3. Update Student Details:")
            print("4. Display Student Details:\n5. Search Student Details:")
            print("6. Exit!!!")
            choice=int(input("Enter your choice:- "))
            if choice==1:
                roll_no=int(input("Enter Student Roll No:- "))
                name= input("Enter Student Name:- ")
                mrks = float(input("Enter Student Marks:- "))
                self.add_student(roll_no,name,mrks)
            elif choice==2:
                roll_no=int(input("Enter the Roll No. to delete:- "))
                self.delete_stdt(roll_no)
            elif choice==3:
                roll_no=int(input("Enter Roll_no:- "))
                name=input("Enter Name to Update:- ")
                mrks=float(input("Enter Marks to Update:- "))
                self.update(roll_no,name,mrks)
            elif choice == 4:
                self.display()
            elif choice == 5:
                roll = int(input("Enter Roll No to Search: "))
                self.search(roll)
            elif choice == 6:
                print("Exiting!!!")
                break
std = Node()
std.menu()

'''
-----------------OUTPUT----------------
*********MENU**********
1. Add Student Details:
2. Delete Student Details:
3. Update Student Details:
4. Display Student Details:
5. Search Student Details:
6. Exit!!!
Enter your choice:- 1
Enter Student Roll No:- 0
Enter Student Name:- om
Enter Student Marks:- 78
Student record Added.
*********MENU**********
1. Add Student Details:
2. Delete Student Details:
3. Update Student Details:
4. Display Student Details:
5. Search Student Details:
6. Exit!!!
Enter your choice:- 1
Enter Student Roll No:- 1 
Enter Student Name:- mok
Enter Student Marks:- 89
Student record Added.
*********MENU**********
1. Add Student Details:
2. Delete Student Details:
3. Update Student Details:
4. Display Student Details:
5. Search Student Details:
6. Exit!!!
Enter your choice:- 2
Enter the Roll No. to delete:- 0
Student Record is Deleted
*********MENU**********
1. Add Student Details:
2. Delete Student Details:
3. Update Student Details:
4. Display Student Details:
5. Search Student Details:
6. Exit!!!
Enter your choice:- 3
Enter Roll_no:- 1
Enter Name to Update:- manish
Enter Marks to Update:- 98
Student record updated.
*********MENU**********
1. Add Student Details:
2. Delete Student Details:
3. Update Student Details:
4. Display Student Details:
5. Search Student Details:
6. Exit!!!
Enter your choice:- 4
---------STUDENT RECORD---------
Roll No:- 1, Name:- manish, Marks:- 98.0
*********MENU**********
1. Add Student Details:
2. Delete Student Details:
3. Update Student Details:
4. Display Student Details:
5. Search Student Details:
6. Exit!!!
Enter your choice:- 5
Enter Roll No to Search: 1

'''
