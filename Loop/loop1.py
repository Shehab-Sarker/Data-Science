# For Loop
#  A for loop in Python is used to iterate over a sequence/Mapping (like a list, tuple,
#  dictionary, string ...
#  1. The loop picks each element from the sequence, one at a time.
#  2. The loop executes the block of code inside it.
#  3. It continues until all elements in the sequence are processed

#  1. range(5) generates numbers from 0 to 4 (excluding 5).
#  2. Each number is assigned to i in each iteration.
#  range(start, stop, step) handles loop control internally.

for i in range(2,10,2):
    print(i,end=" ")
    
print()
    
# # Iterating Over a List
fruits=["apple","banana","cherry"]
for fruit in fruits:
    print(fruit)  
    
#Looping Through a String
word ="Python"
for letter in word:
    # print(letter)
    print(letter,end="")
print()

my_tuple = ("red","green","blue")

for i in range(len(my_tuple)):
    print("Index",i,"has value",my_tuple[i])
    

#Nested for loop
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
        
print()       