# Variables init
p=0

while p==0:
    x=int(input("Aantal werknemers:"))
    y=float(input("Jaaromzet:"))
    z=float(input("Balanstotaal:"))
    s=int(input("Percentage in handen van een niet-KMO onderneming:"))
    if x<250 and (y<50000 or z<43000) and s<25:
        print("Het bedrijf is EEN KMO")
    else:
        print("Het bedrijf is GEEN KMO")
    r=input("Opnieuw?")
    if r.lower()=="ja":
        p+=0
    else: p+=1