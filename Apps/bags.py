while True:
    bag = int(input("How many bags would you like to purchase? "))
    if bag<=0:
        print("Error! Only enter numbers greater than 0.")
        bag = int(input("How many bags would you like to purchase? "))


    def quantityDiscount():
        global initial,total,more
        if bag > 1 and bag < 9:
            initial = bag * 2000
            total = initial
        elif bag > 10 and bag < 19:
            initial = bag * 2000
            total = initial - initial * 0.15
        elif bag > 20 and bag < 49:
            initial = bag * 2000
            total = initial - initial * 0.25
        else:
            initial = bag * 2000
            total = initial - initial * 0.35

        print("Original cost: " , initial)
        print("Cost after discount: " , total)
        more = input("Would you like to purchase more bags? (yes/no)? ")

    quantityDiscount()

    if more == 'yes':
        continue
    elif more == 'no':
        break




