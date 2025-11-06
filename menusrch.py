def srch(emp_ID,target):
    for i in range(0,len(emp_ID)):
        if(target==emp_ID[i]):
            return i;
            break
    return -1;
def menu():
    print("------------------------------------------------")
    print("WELCOME TO MENU")
    print("1. LINEAR SEARCH")
    print("3. BINARY SEARCH")
    print("4. EXIT!!!")

n = int(input("Enter Number of users in your Company:- "))
emp_ID = []
print("Enter elements one by one:- ")
for i in range(n):
    ele = int(input())
    emp_ID.append(ele)
print("Employee ID's:- ",emp_ID)
while True:
    menu()
    choice = input("Enter your Choice:- ")
    if(choice=='1'):
        key=int(input("Enter the Employee Id You want to search==> "))
        res = srch(emp_ID,key)
        if(res!=-1):
            print(f"Employee ID is found at {res+1} :- {emp_ID[res]}")
        else:
            print("Employee is Not Found...PLEASE GIVE CORRECT ID")
    elif (choice=='3'):
        break
