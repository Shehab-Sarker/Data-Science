# 1. input() always returns a string (convert if needed).
#  2. Use .split() for multiple inputs.

name=input("Enter your name: ")
print("Hello, "+name+"!")
print()

#Converts input to an integer
age=int(input("Enter your age: "))
print("You are ",age," years old")
print()

#Multiple Inputs in One Line
a,b=map(int,input("Enter two numbers: ").split()) #split input by spaces
# a,b =int(a) , int(b) #Convert to integers
print("Sum:",a+b)
print()

#List Input(Multiple Values)
numbers=list(map(int,input("Enter numbers: ").split()))
print("You entered:",numbers)
print()

names=input("Enter names separeted by commans: ").split(",")
print("Names: ",names)