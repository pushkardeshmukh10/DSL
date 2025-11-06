class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Roll No: {self.roll_no}, Name: {self.name}, Marks: {self.marks}"

class StudentDB:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def hash_function(self, roll_no):
        return roll_no % self.size

    def insert(self, student):
        idx = self.hash_function(student.roll_no)
        start_idx = idx
        while self.table[idx] is not None:
            if self.table[idx].roll_no == student.roll_no:
                print("Student with this roll number already exists.")
                return
            idx = (idx + 1) % self.size
            if idx == start_idx:
                print("Database is full.")
                return
        self.table[idx] = student
        print("Student inserted successfully.")

    def search(self, roll_no):
        idx = self.hash_function(roll_no)
        start_idx = idx
        while self.table[idx] is not None:
            if self.table[idx].roll_no == roll_no:
                return self.table[idx]
            idx = (idx + 1) % self.size
            if idx == start_idx:
                break
        return None

    def delete(self, roll_no):
        idx = self.hash_function(roll_no)
        start_idx = idx
        while self.table[idx] is not None:
            if self.table[idx].roll_no == roll_no:
                self.table[idx] = None
                print("Student deleted successfully.")
                return
            idx = (idx + 1) % self.size
            if idx == start_idx:
                break
        print("Student not found.")

    def update(self, roll_no, name=None, marks=None):
        idx = self.hash_function(roll_no)
        start_idx = idx
        while self.table[idx] is not None:
            if self.table[idx].roll_no == roll_no:
                if name is not None:
                    self.table[idx].name = name
                if marks is not None:
                    self.table[idx].marks = marks
                print("Student updated successfully.")
                return
            idx = (idx + 1) % self.size
            if idx == start_idx:
                break
        print("Student not found.")

    def display(self):
        print("Student Database:")
        for student in self.table:
            if student is not None:
                print(student)

def main():
    db = StudentDB(size=10)
    while True:
        print("--------------*MENU*--------------")
        print("\n1. Insert Student\n2. Search Student\n3. Delete Student\n4. Update Student\n5. Display All\n6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            roll_no = int(input("Enter Roll No: "))
            name = input("Enter Name: ")
            marks = float(input("Enter Marks: "))
            db.insert(Student(roll_no, name, marks))
        elif choice == '2':
            roll_no = int(input("Enter Roll No to search: "))
            student = db.search(roll_no)
            if student:
                print("Student Found:", student)
            else:
                print("Student not found.")
        elif choice == '3':
            roll_no = int(input("Enter Roll No to delete: "))
            db.delete(roll_no)
        elif choice == '4':
            roll_no = int(input("Enter Roll No to update: "))
            name = input("Enter new Name (leave blank to keep unchanged): ")
            marks_input = input("Enter new Marks (leave blank to keep unchanged): ")
            name = name if name.strip() != "" else None
            marks = float(marks_input) if marks_input.strip() != "" else None
            db.update(roll_no, name, marks)
        elif choice == '5':
            db.display()
        elif choice == '6':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()