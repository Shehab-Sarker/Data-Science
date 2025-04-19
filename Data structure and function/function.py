# 1. Functions are reusable blocks of code that perform a specific task.
#  2. Instead of writing the same code again and again, you write it once as a function and
#  call it when needed.
#  3. Break down complex problems
#  4. Increase readability

def greet(name):
    print("Hello",name)
    print("Hello, Shehab Sarker!")

greet("Mahi")  
print()

# Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

# E.g. if you send a List as an argument, it will still be a List when it reaches the function:  

def my_function(food):
    for x in food:
        print(x)
        
fruits=["apple","banana","cherry"]
my_function(fruits)
print()

## Keyword & Default Arguments
def greet(name,message):
    print(name,message)
    
greet(message="Hi",name="Timur") 
print()

# function with Default Arguments
#default Argument
def greet(name,message="Hello"):
    print(name,message)
    
greet("Timur")       

#return statement
def add(x,y):
    return x+y

print(add(7, 8))
print()

# Difference between print() and return
#  1. print() shows the result to the user
#  2. return sends the result back to the caller


# Task: Create a function that takes a list of numbers and returns a dictionary with
#  statistics: min, max, sum, and average
def calculate_status(numbers):
    if len(numbers)==0:
        return "List is empty,cannot calculate stats."
    stats={
        "min":min(numbers),
        "max":max(numbers),
        "sum":sum(numbers),
        "average":sum(numbers)/len(numbers)
    }
    return stats

numbers_list=[5,10,15,20,25,30]
result = calculate_status(numbers_list)
print(result)

# The function calculate_stats() takes a list of numbers as input.
#  1. min(): Finds the smallest number in the list.
#  2. max(): Finds the largest number.
#  3. sum(): Adds up all the numbers.
#  4. average: Sum divided by the number of elements in the list.
#  If the list is empty, it returns a message indicating that stats can't be calculated
print()

#  1. *args -> Accepts variable number of values (tuple)
#  2. **kwargs -> Accepts variable number of named arguments (dictionary)

def add(*args):
    print(args)
    print(sum(args))
    
add(1,2,4)

def describe_pet(**kwargs):
    print(kwargs)
    
describe_pet(name="Bobby", type="dog")  

