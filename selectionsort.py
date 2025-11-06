list1=[12,15,6,17,20,19,10,3,11,4,2,1]

def selection_sort(list0):
	n=len(list0)

	for i in range(n):
		min_idx=i
		for j in range(i+1,n):
			if list0[j] < list0[min_idx]:
				list0[min_idx],list0[j] = list0[j],list0[min_idx]
				
	return list0
	
x=selection_sort(list1)
print("SORTED LIST BY SELECTION SORT :\n",x)

