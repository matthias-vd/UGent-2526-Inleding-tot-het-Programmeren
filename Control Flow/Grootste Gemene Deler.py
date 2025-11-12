getal1 = int(input("Geef getal 1?"))
getal2 = int(input("Geef getal 2?"))

if getal1 >= getal2:
    for i in range(1,getal2+1):
        if getal1%i==0 and getal2%i==0:
            ggd=i
elif getal2>getal1:
    for i in range(1,getal1+1):
        if getal1%i==0 and getal2%i==0:
            ggd=i

print("Grootste Gemene Deler is",ggd)