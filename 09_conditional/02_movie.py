age=int(input("Enter age :"))
day=input("Enter the 3 letter of the day :")


price=12 if age>=18 else 8
if day=="wed":
    price-=2
print("Ticket price for $",price)
