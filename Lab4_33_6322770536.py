print("Menu:")
print("1.Kao Pad Koong: 40 Baht\n2.Sen Yai Pad Se-Eiw: 30 Baht\n3.Ka Prao Kai: 35 Baht\n4.Kha Na Moo Krob: 35 Baht\n5.Koong Ob Woon Sen: 55 Baht")
order = int(input("Please specify your order (1-5) : "))

price = 0
if order==1:
    price = 40
    egg = input("Do you need added fried egg (y/n) : ")
    size = input("Do you need your meal to be extra size (y/n) : ")
    if egg == "y":
        price+=10
    else:
        False
    if size == "y":
        price+=15
    else:
        False
    print("The price is %d Baht"%price)
elif order==2:
    price = 30
    egg = input("Do you need added fried egg (y/n) : ")
    size = input("Do you need your meal to be extra size (y/n) : ")
    if egg == "y":
        price+=10
    else:
        False
    if size == "y":
        price+=15
    else:
        False
    print("The price is %d Baht"%price)
elif order==3:
    price = 35
    egg = input("Do you need added fried egg (y/n) : ")
    size = input("Do you need your meal to be extra size (y/n) : ")
    if egg == "y":
        price+=10
    else:
        False
    if size == "y":
        price+=15
    else:
        False
    print("The price is %d Baht"%price)
elif order==4:
    price = 35
    egg = input("Do you need added fried egg (y/n) : ")
    size = input("Do you need your meal to be extra size (y/n) : ")
    if egg == "y":
        price+=10
    else:
        False
    if size == "y":
        price+=15
    else:
        False
    print("The price is %d Baht"%price)
elif order==5:
    price = 55
    egg = input("Do you need added fried egg (y/n) : ")
    size = input("Do you need your meal to be extra size (y/n) : ")
    if egg == "y":
        price+=10
    else:
        False
    if size == "y":
        price+=15
    else:
        False
    print("The price is %d Baht"%price)
else:
    print("You entered invalid choice.")
