def menu():
    print("------------------------------------------------")
    print("WELCOME TO MENU")
    print("1. BUBBLE SORT")
    print("2. SELECTION SORT")
    print("3. EXIT!!!")
def bubblesort(salary,n):
    for i in range(n-1):
        for j in range(n-i-1):
            if(salary[j]>salary[j+1]):
                temp=salary[j]
                salary[j]=salary[j+1]
                salary[j+1]=temp
    return salary
n = int(input("Enter Number of Employee's in your Company:- "))
salary = []
print("Enter Salary in Decimal:- ")
for i in range(n):
    ele = float(input())
    salary.append(ele)
print("List of salary:- ",salary)
while True:
    menu()
    choice = input("Enter your choice:- ")
    if(choice=='1'):
        print("Bubble Sort")
        sorted_salary=bubblesort(salary,n)
        print("Sorted Salary:- ",sorted_salary)
    if(choice=='3'):
        print("EXIT")
        break
