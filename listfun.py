def search():
    k= int(input("Enter the Element:- "))
    if k in list:
        print("ELement found in List.")
    else:
        print("ELement not found in List")

list = [10,20,23,12,34]
print(list)
maxm = max(list)
minm = min(list)
avg = sum(list) / len(list)
print("Maximum := ", maxm)
print("Minimum := ",minm)
print("Average of List:- ",avg)
list.reverse()
print("Reversed is :- ",list)
search()

