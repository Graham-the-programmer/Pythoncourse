small_pizza = 15
medium_pizza = 20 
large_pizza = 25
pepp_for_small = 2
pepp_for_m_or_l = 3
extra_cheese = 1

customers_choice = []

choice1 = input("What size pizza would you like? Small, Medium or Large?, Please type: s, m or l: ")
while choice1 != "s" or "m" or "l":
   choice1 = input("Please type: s, m or l: ") 
   if choice1 == "s":
    print("this is working") 