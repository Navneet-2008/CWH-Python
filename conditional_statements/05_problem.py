#detect spam comment
p1 = "make a lot of money"
p2 = "buy this"
p3 = "subscribe this"
p4 = "click this"

message = input("enter your message : ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("this is a spam comment")
else:
    print("this is not a spam comment")
