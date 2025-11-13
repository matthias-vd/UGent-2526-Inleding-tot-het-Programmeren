woord = str(input("Enter a string:"))

# Draai string om
omgekeerdwoord = woord[::-1]

# Verwijder spaties
woord_filtered = woord.replace(" ","")
omgekeerdwoord_filtered = omgekeerdwoord.replace(" ","")


if woord_filtered == omgekeerdwoord_filtered:
    print(f"The string {woord} is a palindrome.")
else:
    print(f"The string {woord} is not a palindrome.")