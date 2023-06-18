#include <stdio.h>
#include <cs50.h>
#include <math.h> // used for mathematical functions like "round()"

int main()
{
    int penny = 1, nickel = 5, dime = 10, quarter = 25, totalCoins = 0; // initializing the values of coins
    float change;
    do
    {
        change = get_float("Change Owed: ");
    }
    while (change <= 0);

    float cents = round(change * 100); // Rounding the number to avoid errors

    while (cents > 0)
    {
        if (cents >= 25)
        {
            cents -= quarter;
        }
        else if (cents >= 10 && cents < 25)
        {
            cents -= dime;
        }
        else if (cents >= 5 && cents < 10)
        {
            cents -= nickel;
        }
        else
        {
            cents -= penny;
        }
        totalCoins += 1; // Counting coins
    }

    printf("%i", totalCoins); // Displaying the total number of coins
}