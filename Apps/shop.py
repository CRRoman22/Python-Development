money = float(input("How much money do you have? "))

print("What would you like to buy? ")
print("""
           Donut(d) - Rs.150
           Coffee(c) - Rs.100
           Bagel(b) - Rs.250
           Scone(s) - Rs.275

      """)

choice = input("Enter your choice? (d/c/b/s) ")

if choice == 'd':
    amount = money/150.00
    print("You can buy",int(amount),"donuts from Rs.",money)
elif choice == 'c':
    amount = money / 100.00
    print("You can buy", int(amount), "coffee from Rs.", money)
elif choice == 'b':
    amount = money / 250.00
    print("You can buy", int(amount), "bagel from Rs.", money)
elif choice == 's':
    amount = money / 275.00
    print("You can buy", int(amount), "scone from Rs.", money)
else:
    print("Sorry, that is not a valid product")