#  Higher-Order Functions
#  Lambda functions are often used with:
#  1. map()
#  2. filter()
#  3. sorted()
numbers =[1,2,3,4]
squares=list(map(lambda x:x**2,numbers))
print(squares)
print()

# Keep only even numbers:
numbers=[1,2,3,4,5,6]
evens=list(filter(lambda x:x%2==0,numbers))
print(evens)
print()

#Sort a list of tuples by the second value:
pairs = [(2,2),(1,3),(4,1)]
sorted_pairs=sorted(pairs,key=lambda x:x[1])
print(sorted_pairs)
print()

def outer():
    def inner():
        print("This is a inner Function")
    inner()
    
outer()