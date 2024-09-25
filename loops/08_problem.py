#prime number
n = int(input("enter the number: "))
if(n == 1): #edge case
    print("Not Prime")
else:
    i = 2
    isPrime = True
    while i < n:
        if(n%i == 0):
            isPrime = False
            break
        i += 1

    if isPrime == True:
        print("Prime Number")
    else:
        print("Not a Prime Number")
