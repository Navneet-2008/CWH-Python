'''
*
* *
* * *
* * * *
* * * * *

'''
# n = int(input("enter the number: "))
# i = 1
# while(i<=n):
#     print("* "*i)
#     i += 1

n = int(input("enter the number: "))
i = 1
while(i<=n):
    j = 1
    while(j<=i):
        print("*", end=" ")
        j += 1
    i += 1
    print()

