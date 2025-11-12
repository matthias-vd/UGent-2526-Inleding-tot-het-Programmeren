x = str(input("Geef de zin die het toverwoord bevat."))

x2=x[13:]
x3=x2.find(" ")
x4=x2[:x3]
x5=x.find("\"")
x6=x.rfind("\"")
x7=x[x5+1:x6]

print("Het toverwoord van",x4,"is","\""+x7+"\""+". De lengte van het toverwoord is",len(x7),"letters.")