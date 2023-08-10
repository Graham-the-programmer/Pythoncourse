print("*************Hello Graham!************")
# username = input("Enter your username:")
# print("Your username is\033[32m", username, "\033[0m")

# print(""" Python is a high-level, general-purpose programming language. 
# Its design philosophy emphasizes code readability with the use of significant indentation.[34]
# Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. 
# It is often described as a "batteries included" language due to its comprehensive standard library.[35][36]""")

choice1 = input("do you want to print your monkey in red, yellow, green or blue?:")
if choice1 == "red":
    print("\033[31m", "You chose red")
elif choice1 == "green":
    print("\033[32m", "You chose green")
elif choice1 == "blue":
    print("\033[34m", "you chose blue")
elif choice1 == "yellow":
    print("\033[33m", "you chose yellow")

print("""              __,__
   .--.  .-"     "-.  .--.
  / .. \/  .-. .-.  \/ .. \
 | |  '|  /   Y   \  |'  | |
 | \   \  \ 0 | 0 /  /   / |
  \ '- ,\.-"`` ``"-./, -' /
   `'-' /_   ^ ^   _\ '-'`
       |  \._   _./  |
       \   \ `~` /   /
        '._ '-=-' _.'
           '~---~'
 """)