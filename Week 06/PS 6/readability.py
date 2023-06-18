from cs50 import get_string

# Defining variables
letters = 0
words = 1   # Since there is no space after the last word, there would be an extra word
sentences = 0

text = get_string("Text: ")

for i in range(len(text)):
    if (text[i].isalpha()):
        letters += 1

    elif text[i] == ' ':
        words += 1

    elif text[i] == '.' or text[i] == '!' or text[i] == '?':
        sentences += 1

# Calculation of L and S
L = (letters * 100) / words  # L is the average number of letters per 100 words in the text
S = (sentences * 100) / words  # S is the average number of sentences per 100 words in the text

grade = ((0.0588 * L) - (0.296 * S) - 15.8)   # Formula to calculate grade level

if grade <= 16 and grade >= 1:
    print(f"Grade {round(grade)}")

elif grade > 16:
    print("Grade 16+\n")

else:
    print("Before Grade 1")