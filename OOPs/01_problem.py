class programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary 
        self.pin = pin 

p = programmer("navneet",4500000,144601)
print(p.name,p.salary,p.pin,p.company)

r = programmer("rajvir",3000000,144601)
print(r.name,r.salary,r.pin,r.company)