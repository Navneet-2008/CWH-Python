list1 = []
limit = int(input("enter the limit: "))
for i in range(limit):
    nums = int(input("enter the numbers: "))
    list1.append(nums)
number = int(input("enter the number you want to check: "))
if(number in list1):
    print(f"the number {number} is present at index",list1.index(number))
else:
    print(f"the number {number} is not present")

list1 = [5,10,15,20,25,50,20]
list1[3] = 200
print(list1)

l = ["RINKU","AUSHIM","VINJAYA","AKTAR","LEENA","TARUN","AMAN"]
for i in l:
    if(i.startswith("A")):
        print(i)