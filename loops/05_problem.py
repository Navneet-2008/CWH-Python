#sum of first n natural numbers

n = int(input("Enter the value of n: "))
i = 1
sum = 0
while i <= n:
    sum += i
    i += 1

print(sum)