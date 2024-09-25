# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

n = int(input("enter the number: "))
i = 1
while(i<=n):
    j = 1
    while(j<=i):
        print(j,end=" ")
        j += 1
    i += 1
    print()