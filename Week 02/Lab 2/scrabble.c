#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Getting input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Scoring both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // Printing the winner
    if (score1 > score2)
    {
        printf("Player 1 wins!");
    }
    else if (score1 < score2)
    {
        printf("Player 2 wins!");
    }
    else
    {
        printf("Tie!");
    }
}

int compute_score(string word) // WORD
{
    // Forming an array for all letters
    char letters[26];
    int asciiValue = 97;
    for (int i = 0; i < 26; i++)
    {
        letters[i] = asciiValue + i;
    }

    // Computing and returning the score for string
    int score = 0;
    for (int j = 0, str_len = strlen(word); j < str_len; j++)
    {
        word[j] = tolower(word[j]);
        for (int k = 0; k < 26; k++)
        {
            if (letters[k] == word[j])
            {
                score = score + POINTS[k];
            }
        }
    }

    return score;
}