import random 

#  list of adjectives

list1 = ["Geeky", "Nerdy", "Tech-savvy", "Cyber", "Innovative", "Digital", 
"Caffeinated", "Screaming", "Techoholic", "Gigabit", "Futuristic", 
"Cloudy", "Wireless", "Pixelated", "Robotronic", "Artificial", 
"Viral", "Quantum", "Epic", "Databionic"]
# list of nouns

list2 = ["Banana", "Penguin", "Noodle", "Cupcake", "Bumblebee", "Pickle", 
"Flamingo", "Pancake", "Snickerdoodle", "Cucumber", 
"Wombat", "Marshmallow", "Llama", "Gummy Bear", "Muffin", "Koala", 
"Panda", "Popcorn", "Jigsaw", "Raindrop"]
# additions and titles

list3 = ["Master of Memes", "Pixel Picasso", "Code Wizard", "Digital Dynamo", 
"Tech Ninja", "Byte Buccaneer", "Debugging Diva", "Chief Emoji Officer", "Virtual Virtuoso", "Data Jedi", "Wi-Fi Whisperer", 
"Chief Troubleshooting Titan", "Byte-sized Comedian", "Pixel Puncher", "Algorithm Alchemist", "Digital Doodle Dandy", "Error Eradicato"]



def nickname_generator():
    a = random.choice(list1)
    b = random.choice(list2)
    c = random.choice(list3)
    list4 = [a, b, c,] 
    nickname = ' '.join(list4)
    print(f"The best nickname for you is: ", str(nickname))


nickname_generator()