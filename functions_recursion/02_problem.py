#factorial of n
n = int(input("enter the number: "))
def factorial(n):
    if(n==0 or n==1):
        return 1
    return n * factorial(n-1)

print("the factorial of n is: ", factorial(n))