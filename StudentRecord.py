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
            
    def menu(self):
        while True:
            print("*********MENU**********")
            print("1. Add Student Details:")
            print("2. Delete Student Details:")
            print("3. Display Student Details")
            print("4. Exit!!!")
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
                self.display()
            elif choice == 4:
                print("Exiting!!!")
                break
std = Node()
std.menu()
