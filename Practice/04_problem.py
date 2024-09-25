a = int(input("enter the value: "))
b = int(input("enter the value: "))
c = int(input("enter the value: "))
if(a+b>c and b+c>a and a+c>b):
    print("they form three sides of a triangle")
else:
    print("these numbers do not form three sides of triangle")
