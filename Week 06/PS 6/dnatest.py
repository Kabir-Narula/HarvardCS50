import csv
import sys

def main():

    # Ensure correct usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    details = []
    # Reading data into memory from file
    with open(sys.argv[1]) as file1:
        reader = csv.DictReader(file1)
        for row in reader:
            details.append(row)

    print(details)

    # Opening text file
    with open(sys.argv[2]) as file2:
        for letter in file2:
            sequence_string = "".join(letter.strip())

    print(sequence_string)

if __name__ == "__main__":
    main()