#wap to find the greatest of four numbers entered by the user.
num1 = int(input("enter number 1 : "))
num2 = int(input("enter number 2 : "))
num3 = int(input("enter number 3 : "))
num4 = int(input("enter number 4 : "))

if(num1>num2 and num1>num3 and num1>num4):
    print("Greatest number is num1 : ", num1)

elif(num2>num1 and num2>num3 and num2>num4):
    print("Greatest number is num2 : ", num2)

elif(num3>num1 and num3>num2 and num3>num4):
    print("Greatest number is num2 : ", num3)

else:
    print("Greatest number is num4 : ", num4)