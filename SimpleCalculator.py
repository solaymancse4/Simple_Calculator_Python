def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b
def modulus(a,b):
    return a%b
print("Please Select the Operation:")
print("1.Addition")
print("2.Subtraction")
print("3. Multiplication")
print("4.Division")
print("5.Modulus")
option = input("Please enter your option:(1/2/3/4/5):")
num1=int (input("Please Enter the first number: "))
num2=int (input("Please Enter the second number: "))

if option=='1':
    print(num1,"+",num2,"=",add(num1,num2))
elif option=='2':
    print(num1,"-",num2,"=",subtract(num1,num2))
elif option=='3':
    print(num1,"*",num2,"=",multiply(num1,num2))
elif option=='4':
    print(num1,"/",num2,"=",division(num1,num2))
elif option=='5':
    print(num1,"%",num2,"=",modulus(num1,num2))
else:
    print("Invalid Input for this calculator")

