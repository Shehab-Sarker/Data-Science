# Set
#  A set is an unordered collection of unique elements.
#  1. Sets are mutable (can be modified), but they do not allow duplicate values.
#  2. Sets are defined using curly braces {} or the set() constructor

#Basic Set
fruits=("apple","banana","cherry")
print(fruits)
print()

# Set with Duplicates (Duplicates will be removed)
fruits = {"apple", "banana", "cherry", "apple", "banana"}
print(fruits) # Output: {'apple', 'banana', 'cherry'}
print()

#Creating a set from list
numbers=set([1,2,3,4,5])
print(numbers)
print()

#Set Opeartions(|)
#set Union (|)
set1={1,2,3}
set2={3,4,5}
union_set=set1|set2
print(union_set)
print()

#Set intersection (&)
intersection_set=set1&set2
print(intersection_set)
print()

#Set difference (-)
diff_set=set1-set2
print(diff_set)