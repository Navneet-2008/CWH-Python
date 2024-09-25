#wap to find out whether a student has passed or failed if requires a total of 40% and atleast 33% in each subject to pass.

mark1 = int(input("enter marks1 : "))
mark2 = int(input("enter marks2 : "))
mark3 = int(input("enter marks3 : "))

total_percentage = (100*(mark1 + mark2 + mark3))/300

if(total_percentage >= 40 and mark1 >= 33 and mark2 >= 33 and mark3 >= 33):
    print("you passed the exam")

else:
    print("you failed the exam")
