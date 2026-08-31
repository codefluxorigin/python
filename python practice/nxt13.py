#wap to take one billing amount from the user if the amount is greater than 5k give 5 percent of discount to the person if not print not eligible and print the final amount after providing the discount
amount=float(input("enter the amount of your bill="))
if amount>=5000:
    amount=amount-(5/100)*(amount)
    print(amount)
else:
    print("not eligible for the discount")