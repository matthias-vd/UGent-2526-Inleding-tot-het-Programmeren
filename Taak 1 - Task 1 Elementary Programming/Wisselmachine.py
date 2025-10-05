import math

print("Ik vind voor jou de combinatie aan centjes dat overeenkomt met een bepaald bedrag.")

bedrag = int(input("Geef een bedrag tussen 0 en 100:"))

print(f"{bedrag} centje(s) bestaat uit:")


if (bedrag / 50) >= 1:
    cent1 = math.floor(bedrag / 50)
    print(f"{cent1} centje(s) van 50 cent")
    bedrag = bedrag - (cent1*50)
else:
    print("0 centje(s) van 50 cent")

if (bedrag / 20) >= 1:
    cent1 = math.floor(bedrag / 20)
    print(f"{cent1} centje(s) van 20 cent")
    bedrag = bedrag - (cent1*20)
else:
    print("0 centje(s) van 20 cent")

if (bedrag / 10) >= 1:
    cent1 = math.floor(bedrag / 10)
    print(f"{cent1} centje(s) van 10 cent")
    bedrag = bedrag - (cent1*10)
else:
    print("0 centje(s) van 10 cent")

if (bedrag / 5) >= 1:
    cent1 = math.floor(bedrag / 5)
    print(f"{cent1} centje(s) van 5 cent")
    bedrag = bedrag - (cent1*5)
else:
    print("0 centje(s) van 5 cent")

if (bedrag / 2) >= 1:
    cent1 = math.floor(bedrag / 2)
    print(f"{cent1} centje(s) van 2 cent")
    bedrag = bedrag - (cent1*2)
else:
    print("0 centje(s) van 2 cent")

if (bedrag / 1) >= 1:
    cent1 = math.floor(bedrag / 1)
    print(f"{cent1} centje(s)")
    bedrag = bedrag - (cent1*1)
else:
    print("0 centje(s)")

