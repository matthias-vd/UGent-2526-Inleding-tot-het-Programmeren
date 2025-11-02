bedrag = float(input("bedrag?"))
duurtijd = int(input("aantal jaren?"))
rentevoet = float(input("rentevoet?"))

# Variables init
npv = 0


for i in range(duurtijd):
    inkomsten = float(input("Inkomsten"))
    uitgaven = float(input("Uitgaven"))
    npv += ((inkomsten - uitgaven) / ((1 + rentevoet) ** (i)))

winst = npv - bedrag
print("De contante waarde over", int(duurtijd), "jaar is € %.2f." % NPV)
if winst > 0:
    print("Hoera! Er wordt een winst geboekt van € %.2f!" % winst)
elif winst == 0:
    print("Er wordt exact break-even gedraaid.")
else:
    print("Er is helaas een verlies van € %.2f!" % winst)