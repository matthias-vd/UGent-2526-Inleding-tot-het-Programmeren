print("Ik vind voor jou de combinatie aan centjes dat overeenkomt met een bepaald bedrag.")
bedrag = int(input("Geef een bedrag tussen 0 en 100:"))

centjes = [50,20,10,5,2]

print(f"{bedrag} centje(s) bestaat uit:")

for centje in centjes:
    aantalcentjes = bedrag // centje
    print(f"{aantalcentjes} centje(s) van {centje} cent")
    bedrag = bedrag % centje

print(f"{bedrag} centje(s)")