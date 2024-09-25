# output the maximum number from the list
list = [23, 45, 98, 3, 100, 67]

maxi = 0
i = 0
while(i < len(list)):
    if maxi < list[i]:
        maxi = list[i]
    i += 1

print(maxi)
