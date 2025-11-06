def srch():
    for i in range(0,len(arr)):
    #for ele in arr :
       # if(key==ele)
        if(key==arr[i]):
            flag=1
            break
        else:
            flag=0
    if (flag==1):
        print("Element is found")
    else:
        print("Element is not found")
from array import *
arr = array('i',[10,20,30,40,50])
key = int(input("Enter the Search Elemernt:- "))
flag = 0
srch()
'''for i in range(0,len(arr)):
#for ele in arr:
   # if(key==ele)
    if(key==arr[i]):
        flag=1
        break
    else:
        flag=0
if (flag==1):
    print("Element is found")
else:
    print("Element is not found")'''
