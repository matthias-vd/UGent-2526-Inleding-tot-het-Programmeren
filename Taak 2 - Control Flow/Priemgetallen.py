getal = int(input("Getal"))


def is_priemgetal(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if is_priemgetal(getal):
    print(f"{getal} is een priemgetal")
else:
    print(f"{getal} is geen priemgetal")