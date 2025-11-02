rentepercentage = float(input("Rentepercentage"))/100
duurtijd = int(input("Duurtijd"))
bedrag = float(input("Bedrag"))

tellerbreuk = bedrag*(rentepercentage/12)
noemerbreuk = 1-1/((1+(rentepercentage/12))**(duurtijd*12))
breuk = tellerbreuk/noemerbreuk


monthlypayment = breuk
monthlypaymentafronding = int(monthlypayment)
totalpayment = monthlypayment*12*duurtijd
totalpaymentafronding = int(totalpayment)

print(f"The monthly payment is {monthlypaymentafronding}")
print(f"The total payment is {totalpaymentafronding}")