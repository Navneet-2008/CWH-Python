fib = [0,1]
n = int(input("enter n: "))

for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])

for item in fib:
    print(item, end=" ")


str = input("Enter word: ")
for i in range(len(str)-1, -1, -1):
    print(str[i], end="")