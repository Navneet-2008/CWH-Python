a = eval(input("enter the number: "))
b = eval(input("enter the number: "))
op = input("enter the operator: ")
if(op == "+"):
    print(a+b)
elif(op == "-"):
    print(a-b)
elif(op == "%"):
    print(a%b)
elif(op == "/"):
    print(a/b)
elif(op == "//"):
    print(a//b)
elif(op == "*"):
    print(a*b)
elif(op == "**"):
    print(a**b)
else:
    print("invalid operator")
