# 90-100 = Ex,
# 80-90 = A,
# 70-80 = B, 
# 60-70 = C,
# 50-60 = D,
# <50 = F

grades = int(input("enter grades : "))
if(grades<=100 and grades>=90):
    print("Grade = Ex")
elif(grades<90 and grades>=80):
    print("Grade = A")
elif(grades<80 and grades>=70):
    print("Grade = B")
elif(grades<70 and grades>=60):
    print("Grade = C")
elif(grades<60 and grades>=50):
    print("Grade = D")
elif(grades<50):
    print("Grade = F")

