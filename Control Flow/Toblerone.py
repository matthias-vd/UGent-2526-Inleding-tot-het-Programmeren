x = input("Merknaam: ")
y = input("Stad: ")
z = ""

j = 0

for i in range(len(x)):
    if j < len(y) and x[i].lower() == y[j].lower():
        z += "[" + x[i] + "]"
        j += 1
    else:
        z += x[i]

while "][" in z:
    z= z.replace("][", "")

print(z)