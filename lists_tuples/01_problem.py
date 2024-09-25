#wap to store seven fruits in a list by the user
fruits = []
num = 0
limit = int(input("How many fruits you want to add: "))
while num < limit: 
    currentFruit = input("Enter fruit: ")
    fruits.append(currentFruit)
    num += 1
print(fruits)