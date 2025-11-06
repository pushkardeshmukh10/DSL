def menu():
    print("------------------------------------------------")
    print("WELCOME TO MENU")
    print("1. BUBBLE SORT")
    print("2. SELECTION SORT")
    print("3. EXIT!!!")
def bubblesort(salary):
    n=len(salary)
    for i in range(n-1):
        for j in range(n-i-1):
            if(salary[j]>salary[j+1]):
                temp=salary[j]
                salary[j]=salary[j+1]
                salary[j+1]=temp
    return salary
salary = [10000.250,50000.00,45000.45,15000.00,6000.00,9000.00,23000.00,8000.00]
print("List of Salary:- ",salary)
while True:
    menu()
    choice = input("Enter your choice:- ")
    if(choice=='1'):
        print("Bubble Sort")
        sorted_salary=bubblesort(salary)
        print("Sorted Salary:- ",sorted_salary)
    if(choice=='3'):
        break
