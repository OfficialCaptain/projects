from random import randint
colors = []

for i in range(int(input("How many colors?: "))):
    colors.append('#%06X' % randint(0, 0xFFFFFF))

print(colors)