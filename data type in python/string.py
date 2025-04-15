str1 ="Hello"
str2 ="World"
str3 ="Python in amazing!"
print(str1,str2,str3)
print(type(str1))
print(isinstance(str1,str))
print("")

multi_line="Hello world python is amazing!"
print(multi_line)
print()

#  Indexing: Access characters using index (0-based).
#  Slicing: Extract a substring using [start:end:step].

text = "Python"
print(text[0])
print(text[5])
print(text[-1])
print(text[0:6:1])
print(text[5::-1])
print()

# text[0]='M'
# print(text) this will raise an error
# Instead of modifying a string directly, you need to create a new string.

new_text="M"+text[1:]
print(new_text)