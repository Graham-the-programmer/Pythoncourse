import random
# a = random.randint(1, 99)
# b = random.randint(1, 99)
# c = random.randint(1, 99)
# d = random.randint(1, 99)
# e = random.randint(1, 99)
# f = random.randint(1, 99)
# g = random.randint(1, 99)
# h = random.randint(1, 99)
# i = random.randint(1, 99)
# j = random.randint(1, 99)
# print(f"""---------------------------
#           |{a} |{b} |{c} |{d} |{e} |
#           |{f} |{g} |{h} |{i} |{j} |
#           --------------------- """)

print("-------------------------")
for j in range(2):
    line = "|"
    for i in range(5):
        rnd = random.randint(1, 99)

        if rnd < 10:
            line += " "
        line += " " + str(rnd) + " |"
    print(line)
    print("-------------------------")


