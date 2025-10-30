# Lees twee kommagetallen in: gewicht (in kg) en lengte (in m)
gewicht = float(input("Gewicht"))
lengte = float(input("Lengte"))

# Bereken het BMI en schrijf de interpretatie hiervan naar het scherm.
bmi = float(gewicht/(lengte**2))
print(bmi)

if bmi < 18:
    print("Ondergewicht")
elif bmi >= 18 and bmi < 25:
    print("Normaal gewicht")
elif bmi >= 25 and bmi < 30:
    print("Overgewicht")
elif bmi >= 30:
    print("Obesitas")