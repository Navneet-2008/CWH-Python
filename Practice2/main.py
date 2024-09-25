list3 = [3,21,5,6,3,8,21,6]
num = int(input("enter the number: "))
count = list3.count(num)
print(count)


lst = []
var = int(input("enter the limit: "))
for i in range(var):
    number = int(input("enter the number: "))
    lst.append(number)
print("max number is: ",max(lst))
print("min number is: ",min(lst))

li = [10,20,30,40,50,60,70]
x = int(len(li)/2)
for i in range(x):
    li[i],li[x+i] = li[x+i],li[i]
print(li)

letter = "python"
for i in letter:
    print(i)

list1 = [20,30,40,50]
for i in list1:
    print(i)

list2 = [1,2,3,4,5,6,7,8,9,10]
for i in list2:
    if(i%2 == 0):
        print(i,"is a even number")

for i in "123":
    print("welcome to",i,"loop")

num = int(input("enter the number: "))
for i in range(1,11):
    print(i,"*",num,"=",num*i)

n = int(input("enter the number: "))
fact = 1
for i in range(1,n+1):
    fact *= i 
print(fact)

n = int(input("enter the number: "))
if(n==1):
    print("not a prime number")
else:
    for i in range(2,n//2+1):
        if(n%i == 0):
            print("its not a prime number")
            break
    else:
        print("its a prime number")


odd = 0
even = 0
for i in range(5,100+1):
    if(i%2 == 0):
        even+=1
    else:
        odd+=1

print("number of even num:",even)
print("number of odd num:",odd)

str = input("enter the word: ")
for i in range(len(str)-1,-1,-1):
    print(str[i],end="")

for i in range(1500,2700+1):
    if(i%5==0) and (i%7==0):
        print(i)

s = 0
n = int(input("enter the limit: "))
for i in range(n+1):
    if (i % 2 == 0):
        s += i
print("sum of even numbers upto n is: ",s)

# n = int(input("enter the limit: "))
# for i in range(n,0,-1):
#     print(i)

n = int(input("enter the number: "))
for i in range(2,n//2+1):
    if(n%i == 0):
        print("it's not a prime number")
        break
else:
    print("it's a prime number")

list = []
limit = int(input("enter the limit: "))
for i in range(limit):
    num = int(input("enter the number: "))
    list.append(num)
list.sort()
print(list)
print(len(list)-1) 

list = []
limit = int(input("enter the limit: "))
for i in range(limit):
    num = int(input("enter the number: "))
    if(num%2 == 0):
        list.append(num)
print(list)

