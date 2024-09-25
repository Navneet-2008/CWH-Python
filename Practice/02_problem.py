salary = int(input("how much salary do you earn? : "))
tax = float(input("enter tax: "))
if(salary>=5000):
    tax *= salary
elif(salary>=6000):
    tax *= salary
elif(salary>=7000):
    tax *= salary
else:
    tax *= salary

print("salary: ",salary,"tax: ",tax)