# Write a Program to take a user score and find a student's grade using Python code. Following is the grade information.

score=int(input())
if  90<=score<=100:
    print("A")
elif 80<=score<90:
    print("B")
elif 70<=score<80:
    print("C")
elif 60<=score<70:
    print("D")
elif 50<=score<60:
    print("E")
elif 40<=score<50:
    print("E-")
elif score<40:
    print("F or Fail")
else:
    print("invaild")