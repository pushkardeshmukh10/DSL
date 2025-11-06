salaries=[45000.0,32000.0,85000.0,12000.0,90000.0,74000.0,35000.0,56000.0]
def bubble_sort(salary_list):
	n = len(salary_list)
	for i in range(n):
		for j in range(n - i -1):
			if salary_list[j] > salary_list[j+1]:
				salary_list[j],salary_list[j+1] = salary_list[j+1],salary_list[j]
	return salary_list
	
x=bubble_sort(salaries)
n=len(bubble_sort(salaries))
print("Sorted list by using bubble sort :\n")
print(x)
print("TOP 5 SALARIES :\n",x[0:5:1])
print("BOTTOM 5 SALARIES :\n",x[n-1:n-6:-1])
