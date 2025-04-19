fruits={"apple","banana","cherry"}
fruits.discard("apple")
print(fruits)
print()

# print(dir(list))
# print()

# print(dir(set))
# print()

# print(dir(tuple))

set1={1,2,3}
set2={4,6,3}
union_set=set1.union(set2)
print(set1.union(set2))
print(set1 & set2)
print(set1 | set2)

print(set1.symmetric_difference(set2))
print()

# course_A = {"Alice", "Bob", "Charlie", "David"}
# course_B = {"Charlie", "Eve", "David", "Frank"}


# Write a program that:

# 1. Finds students who are enrolled in both courses.
# 2. Finds students who are enrolled in only Course A.
# 3. Finds students who are enrolled in either Course A or Course B but not both.

course_A = {"Alice", "Bob", "Charlie", "David"}
course_B = {"Charlie", "Eve", "David", "Frank"}

print("1:",course_A & course_B)
print("2:",course_A - course_B)
print("3:",course_A ^ course_B)
print()

print("1:",course_A.intersection(course_B))
print("2:",course_A.difference(course_B))
print("3:",course_A.symmetric_difference(course_B))
print()

students = [
    ("Alice", 3.75),
    ("Bob", 3.60),
    ("Charlie", 3.90),
]

for name,cgpa in students:
    print(f"Name : {name}, CGPA : {cgpa}")
    



