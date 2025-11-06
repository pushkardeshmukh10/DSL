'''
GROUP:-A PRACTICAL NO..2
PROBLEM STATEMENT:--> In an e-commerce system,cutomer account ID's are stored in a list
and you are tasked with writing a program that implements the following:-
1.Linear Search 
2.Binary Search
-----------------------------------------------------------------------------------------
Name:- Deore Om Yashwant
Roll No.:- 29
Batch:- SEA-2
'''
def srch(emp_ID,target):
    for i in range(0,len(emp_ID)):
        if(target==emp_ID[i]):
            return i;
            break
    return -1;
def bisrch(emp,target):
    sort=sorted(emp)
    print(f"Sorted List:- {sort}")
    lr=0
    ur=n-1
    while (lr<=ur):
        mid=lr+ur//2
        if (emp[mid]==target):
            return mid
            #break
        elif(target<emp[mid]):
            print("Element found in First Half")
            ur=mid-1
        elif(target>emp[mid]):
            print("Element found in Second Half")
            lr=mid+1
    return -1
def menu():
    print("------------------------------------------------")
    print("WELCOME TO MENU")
    print("1. LINEAR SEARCH")
    print("2. BINARY SEARCH")
    print("3. EXIT!!!")

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
        print("-------<*>LINEAR SEARCH<*>-----------")
        key=int(input("Enter the Employee Id You want to search==> "))
        res = srch(emp_ID,key)
        if(res!=-1):
            print(f"Employee ID {emp_ID[res]} is found.")
        else:
            print("Employee is Not Found...PLEASE GIVE CORRECT ID")
    if(choice=='2'):
        print("-------<*>BINARY SEARCH<*>-----------")
        key=int(input("Enter the Employee Id You want to search==> "))
        res = bisrch(emp_ID,key)
        if(res!=-1):
            print(f"Employee ID {emp_ID[res]} is found.")
        else:
            print("Employee is Not Found...PLEASE GIVE CORRECT ID")
    elif (choice=='3'):
        print("\t----------<*>EXIT<*>-----------")
        break

'''
OUTPUT--------->

python3 menusrch.py
Enter Number of users in your Company:- 5
Enter elements one by one:- 
123
234
345
456
567
Employee ID's:-  [123, 234, 345, 456, 567]
------------------------------------------------
WELCOME TO MENU
1. LINEAR SEARCH
2. BINARY SEARCH
3. EXIT!!!
Enter your Choice:- 1
-------<*>LINEAR SEARCH<*>-----------
Enter the Employee Id You want to search==> 123
Employee ID 123 is found.
------------------------------------------------
WELCOME TO MENU
1. LINEAR SEARCH
2. BINARY SEARCH
3. EXIT!!!
Enter your Choice:- 2
-------<*>BINARY SEARCH<*>-----------
Enter the Employee Id You want to search==> 345
Sorted List:- [123, 234, 345, 456, 567]
Employee ID 345 is found.
------------------------------------------------
WELCOME TO MENU
1. LINEAR SEARCH
2. BINARY SEARCH
3. EXIT!!!
Enter your Choice:- 3
	----------<*>EXIT<*>-----------

'''
