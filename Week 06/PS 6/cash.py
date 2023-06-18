from cs50 import get_float

# Initializing Variables
penny = 1
nickel = 5
dime = 10
quarter = 25
totalCoins = 0

while True:
    change = get_float("Change Owed: ")
    if change > 0:
        break

cents = round(change*100, 2)

while (cents > 0):
    if cents >= 25:
        cents -= quarter
    elif cents >= 10 and cents < 25:
        cents -= dime
    elif cents >= 5 and cents < 10:
        cents -= nickel
    else:
        cents -= penny

    totalCoins += 1   # Counting coins

print(totalCoins)   # Displaying the total number of coins