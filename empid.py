n = int(input("Enter Number of users in your Company:- "))
emp_ID = []
print("Enter elements one by one:- ")
for i in range(n):
    ele = int(input())
    emp_ID.append(ele)
print("Array:- ",emp_ID)
emp_ID.sort()
print(emp_ID)
lr=emp_ID[0]
ur=emp_ID[n-1]
print(f"lr:-{lr},ur={ur}")
