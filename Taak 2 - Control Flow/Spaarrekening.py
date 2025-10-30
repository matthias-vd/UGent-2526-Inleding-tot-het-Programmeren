import copy
bed=float(input())
bed0=copy.deepcopy(bed)
i=float(input())
j=int(input())
l=1
while l!=j+1:
    bed*=(1+i)
    print(f'Bedrag na {l} jaar: €{format(bed,".2f")}.')
    l+=1
if bed0<bed:
    print(f'Na {j} jaar bedraagt de winst €{format(abs(bed-bed0),".2f")}.')
if bed0>bed:
    print(f'Na {j} jaar bedraagt het verlies €{format(abs(bed-bed0),".2f")}.')

'''bedrag = float(input("Bedrag"))
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
    print(f"Na {duurtijd} jaar bedraagt de winst €{bedrag_delta}.")'''