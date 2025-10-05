gewicht = int(input("Gewicht"))
lengte = int(input("Lengte"))
leeftijd = int(input("Leeftijd"))

bmrman = (66.4730 + (13.7516 * gewicht) + (5.0033 * lengte) - (6.7550 * leeftijd))/230
bmrvrouw = (655.0955 + (9.5634 * gewicht) + (1.8496 * lengte) - (4.6756 * leeftijd))/230

print("Een man moet dagelijks",bmrman,"chocoladerepen eten om zijn gewicht te behouden.")
print("Een vrouw moet dagelijks",bmrvrouw,"chocoladerepen eten om haar gewicht te behouden.")