def hello_fun():
	print("Hello, I am Om")
def sum():
    num1=int(input("Enter First Number:- "))
    num2=int(input("Enter Second Number:- "))
    res=num1+num2
    print("Addition is:- ",res)
def sum_rtrn():
    a=int(input("Enter the A Value:- "))
    b=int(input("Enter the B Value:- "))
    add=a+b
    return add
hello_fun()
sum()
add=sum_rtrn()
print("Addition is:- ",add)
