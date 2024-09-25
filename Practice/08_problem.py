while True:
    print("1.For area of circle")
    print("2.For area of rectangle")
    print("3.For circumference of circle")
    print("4.For area of square")
    choice = int(input("enter your choice(enter 0 to exit): "))
    if(choice==1):
        r = int(input("enter radius: "))
        a = 3.14*r*r
        print("area of circle",a)
    elif(choice==2):
        l = int(input("enter the length: "))
        b = int(input("enter the breath: "))
        a = l*b
        print("area of rectangle",a)
    elif(choice==3):
        r = int(input("enter radius: "))
        a = 2*3.14*r
        print("circumference of circle: ",a)
    elif(choice==4):
        side = int(input("enter the side: "))
        a = side*side
        print("area of a square: ",a)
    elif(choice==0):
        break
    else:
        print("invalid option")