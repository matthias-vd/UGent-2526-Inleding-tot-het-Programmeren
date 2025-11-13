# zet je oplossing in de functie main
def main():
    gewicht = float(input())
    lengte = int(input())

    bmi = gewicht / ((lengte/100)**2)

    print(f"{bmi:.2f}")

    if bmi >= 30:
        print("Obesitas")
    elif bmi >= 25:
        print("Overgewicht")
    elif bmi >= 18.5:
        print("Gezond gewicht")
    else:
        print("Ondergewicht")

# enkel om lokaal te kunnen testen
if __name__ == '__main__':
    main()

