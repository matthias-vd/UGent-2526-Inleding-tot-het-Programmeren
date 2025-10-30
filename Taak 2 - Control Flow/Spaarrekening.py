bedrag = float(input("Bedrag"))
rentevoet = float(input("Rentevoet"))
duurtijd = int(input("Duurtijd"))


# Variables init
counter = 1
bedrag_totaal = 0
bedrag_initieel = bedrag

# Print bedragen

while counter != (duurtijd+1):
    bedrag = float((bedrag * (1+rentevoet)))
    bedrag = float("{:.2f}".format(bedrag))
    print(f"Bedrag na {counter} jaar: €{bedrag}.")
    counter = counter + 1


# Bepaal winst

bedrag_delta = float(bedrag - bedrag_initieel)
bedrag_delta = float("{:.2f}".format(bedrag_delta))
if bedrag_delta < 0:
    bedrag_delta = abs(bedrag_delta)
    print(f"Na {duurtijd} jaar bedraagt het verlies €{bedrag_delta}.")
elif bedrag_delta > 0:
    print(f"Na {duurtijd} jaar bedraagt de winst €{bedrag_delta}.")