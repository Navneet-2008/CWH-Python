#wap to accept marks of 6 students and display them in a sorted manner
marks = []
stu1 = int(input("enter marks : "))
marks.append(stu1)
stu2 = int(input("enter marks : "))
marks.append(stu2)
stu3 = int(input("enter marks : "))
marks.append(stu3)
stu4 = int(input("enter marks : "))
marks.append(stu4)
stu5 = int(input("enter marks : "))
marks.append(stu5)
stu6 = int(input("enter marks : "))
marks.append(stu6)
marks.sort()
print(marks)