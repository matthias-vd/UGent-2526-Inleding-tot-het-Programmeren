import random

# Randomisatie

random.seed(1)
getal = random.randint(0, 99)

getal_tiental = getal // 10
getal_eenheid = getal % 10

# Input

userinput = int(input("Enter your lottery pick (two digits):"))

userinput_tiental = userinput // 10
userinput_eenheid = userinput % 10


# Winnend bedrag

print(f"The lottery number is {getal}")

if getal == userinput:
    print("Exact match: you win 10.000 €")
elif getal_tiental == userinput_eenheid and getal_eenheid == userinput_tiental:
    print("Match all digits: you win 3.000 €")
elif getal_tiental == userinput_eenheid or getal_eenheid == userinput_tiental or getal_tiental == userinput_tiental or getal_eenheid == userinput_eenheid:
    print("Match one digit: you win 1.000 €")
else:
    print("Sorry, no match")