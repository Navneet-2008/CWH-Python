n = int(input("enter number: "))
if n == 1:
    print("Not Prime")
else:
    for i in range(2,n//2+1):
        if(n%i == 0):
            print("Number is not prime")
            break
    else:
        print("Number is prime")