from array import *
arr = [10,20,30,40,50]  
print(arr)
arr.insert(2,25)
print("Inserted:-",arr)
arr.append(55)
print("Appended:-",arr)
arr.extend([60,70,80,90])
print("Extended:-",arr)
arr1=[100,110,120]
print("New Array:-",arr1)
arr_result = arr + arr1
print("Merge Array:-",arr_result)
arr.remove(55)
print("Removed:-",arr)
v1=arr.pop()
print("Last Popped:-",arr)
print("Popped Element:-",v1)
v2=arr.pop(3)
print("30 is popped:- ",arr)
print("popped:- ",v2)
