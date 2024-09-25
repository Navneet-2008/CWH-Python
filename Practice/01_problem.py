hourlypay = int(input("how much do you earn per hour? : "))
hoursperweek = int(input("how many hours do you earn per week? : "))
weeklypay = hourlypay*hoursperweek
if(weeklypay>4000):
    print("you can afford to live alone")
else:
    print("you can't afford to live alone")
