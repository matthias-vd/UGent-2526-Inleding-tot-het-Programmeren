x = int(input("Find all prime numbers <= n, enter n: "))

# Variables init
t = 0
z=""

for i in range(2,x+1):
    r=0
    for j in range(1,i+1):
      if i%j==0:
          r+=1
    if r==2:
        t += 1
        z += str(i)+""
        if t % 10 == 0:
            z += "\n"
        else:
            z += " "


print("The prime numbers are:")

print(z)

print(str(t),"prime(s) less than or equal to",x)