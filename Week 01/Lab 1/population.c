#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int start_size, end_size, n =  0; // n signifies the years taken to reach the end size from the start size

    do
    {
        start_size = get_int("Start size: ");
    }
    while (start_size < 9); // Prompts user for input until a value greater than or equal to 9 is provided

    do
    {
        end_size = get_int("End size: ");
    }
    while (end_size < start_size); // Prompts user for input until a value greater than or equal to start size is provided

    // Calculations

    while (start_size < end_size)
    {
        int net_increase = start_size / 3 - start_size / 4;
        start_size += net_increase;
        n++;
    }

    // Displaying final result
    printf("Years: %i\n", n);
}