def bill(units):
    if units<=100:
        amount=units*8
    else:
        amount=units*10
        return(amount)
a=float(input("enetr the units consumed this month"))
a=bill(a)
print("the amount you need to pay=",a)
