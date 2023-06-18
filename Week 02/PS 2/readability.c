#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int main()
{
    int letters = 0;
    int words = 1; // Since there is no space after the last word, there would be an extra word
    int sentences = 0;
    string text = get_string("Text: ");

    for (int i = 0; i < strlen(text); i++)
    {
        if (isalpha(text[i]) != 0)
        {
            letters++;
        }
        else if (text[i] == ' ')
        {
            words++;
        }
        else if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sentences++;
        }
    }
    float L, S;
    // L is the average number of letters per 100 words in the text
    // S is the average number of sentences per 100 words in the text

    // Calculation of L and S
    L = (letters * 100) / (float) words;
    S = (sentences * 100) / (float) words;

    float grade = 0.0588 * L - 0.296 * S - 15.8; // Formula to calculate grade level

    if (grade <= 16 && grade >= 1)
    {
        printf("Grade %i\n", (int) round(grade));
    }
    else if (grade > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Before Grade 1\n");
    }
}