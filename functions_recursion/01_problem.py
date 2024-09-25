#wap using functions to find the greatest of three numbers
def greatestnumber(a,b,c):
    if(a>b and a>c):
        return a 
    elif(b>a and b>c):
        return b
    else:
        return c 
a = 3
b = 5
c = 16
print(greatestnumber(a,b,c))


