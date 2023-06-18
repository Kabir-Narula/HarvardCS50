#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, string argv[])
{
    int key;
    // Accepting valid command line arguments
    if (argc == 2)
    {
        for (int i = 0, n = strlen(argv[1]); i < n; i++)
        {
            if (!isdigit(argv[1][i]))  // Checking for integer value
            {
                printf("Usage: ./caesar key\n");
                return 1;
            }
        }
        key = atoi(argv[1]); // Converting the key to integer
        printf("Success\n");
        printf("%i\n", key);
    }
    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Prompting user to enter text
    string user_input = get_string("plaintext: ");
    for (int j = 0, m = strlen(user_input); j < m; j++)
    {
        if (isupper(user_input[j]))
        {
            user_input[j] = (((user_input[j] - 65) + key) % 26) + 65; // adding 65 to reach upper case ascii values
        }
        else if (islower(user_input[j]))
        {
            user_input[j] = (((user_input[j] - 97) + key) % 26) + 97; // adding 97 to reach lower case ascii values
        }
    }

    printf("ciphertext: %s\n", user_input);
    return 0;
}