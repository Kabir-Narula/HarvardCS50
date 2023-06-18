# include <stdio.h>
# include <cs50.h>

int main()
{
    int height, i, j, k, hash = 0;

    // Accepting the appropriate value
    do
    {
        height = get_int("Height: ");
    }
    while (height <= 0 || height > 8);

    for (i = 0; i < height; i++)
    {
        for (j = i; j < height - 1; j++)
        {
            printf(" "); // Adds spaces in the start which decrease in number everytime the loop runs
        }
        for (k = 0; k < hash + 1; k++)
        {
            printf("#"); // Adds hashtags in the end which increase in number everytime the loop runs
        }
        printf("\n"); // Adds a newline to create more rows
        hash++;
    }
}