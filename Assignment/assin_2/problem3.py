# Problem: 03
# Write a Python program that creates a new list containing only the duplicate elements from the given list: [1, 5, 6, 5, 1, 2, 3].

# duplicate=[] #this is new list
# def duplicate_elements(given_list):
#     seen=[]   
#     for item in given_list:
#         if item in seen:
#             duplicate.append(item)
#         else:
#             seen.append(item)
        
#     print(duplicate)

# given_list= [1, 5, 6, 5, 1, 2, 3,6]
# duplicate_elements(given_list)
print()

given_list=[1, 5, 6, 5, 1, 2, 3]
#create a new list
duplicate_list=[]

for item in given_list:
    if given_list.count(item)>1 and item not in duplicate_list:
        duplicate_list.append(item)
        
print(duplicate_list)
