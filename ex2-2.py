money_spent = int(input("How much money was spent: "))
if money_spent >= 500:
  discount = money_spent * 0.9  
  print("Total to pay after discount: $", discount) 
else:
    print("Sorry no discout, total to pay: $", money_spent)