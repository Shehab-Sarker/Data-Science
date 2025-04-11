#Problem: 02
# Write a program that takes two numbers and an operator (+, -, *, /) and performs the calculation.
# num1,num2=map(int,input("Enter the two number:\n").split())
num1=int(input("Enter the 1st numbers: "))
num2=int(input("Enter the 2nd numbers: "))
print(num1,"+",num2,"=",num1+num2)
print(num1,"-",num2,"=",num1-num2)
print(num1,"*",num2,"=",num1*num2)

if num2!=0:
    print(num1,"/",num2,"=",num1/num2)
else:
    print("divison by zero is not allowed")