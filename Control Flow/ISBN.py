getal1 = int(input("Getal 1"))
getal2 = int(input("Getal 2"))
getal3 = int(input("Getal 3"))
getal4 = int(input("Getal 4"))
getal5 = int(input("Getal 5"))
getal6 = int(input("Getal 6"))
getal7 = int(input("Getal 7"))
getal8 = int(input("Getal 8"))
getal9 = int(input("Getal 9"))
getal10 = int(input("Getal 10"))

# Geldigheid controleren
controlegetal = (getal1 + 2*getal2 + 3*getal3 + 4*getal4 + 5*getal5 + 6*getal6 + 7*getal7 + 8*getal8 + 9*getal9) % 11

if getal10 == controlegetal:
    print("OK")
else:
    print("FOUT")