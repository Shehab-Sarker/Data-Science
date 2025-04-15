var=[1,2,3,4,5]
print(var[4])
print(var[1:3])
print("")

var=[[1,2],[3,4],[5,6]]
print(var[1])
print("")

#Add Methods
numbers = [1,2,3]
numbers.append([7,8])
print(numbers)
print("")

#two list merge
list1=[1,2,3]
list2=[4,5,6]
list1.extend(list2)
print(list1)
print("")


#insert with extend
a1=[1,2,3]
b1=[4,6,7,8]
b1.insert(1,5)
a1.extend(b1)
print(a1)