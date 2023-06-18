import csv
import sys

def main():

    # Ensure correct usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    details = []
    details_listOfdicts = []

    # Storing the data of the CSV file in a list of lists
    with open(sys.argv[1]) as file1a:
        reader = csv.reader(file1a)
        for row in reader:
            details.append(row)

    # print(details)

    # Storing the data of the CSV file in a list of dictionaries too
    with open(sys.argv[1]) as file1b:
        reader1 = csv.DictReader(file1b)
        for row1 in reader1:
            details_listOfdicts.append(row1)

    # print(details_listOfdicts)

    # Creating a new list where all the strs will be stored
    dna_strs_list = details[0][1:]
    # print(dna_strs_list)

    # Opening text file
    with open(sys.argv[2]) as file2:
        for letter in file2:
            sequence_string = "".join(letter.strip())

    # print(sequence_string)

    def number_of_times(input_string, substring):
        counter = 0
        while substring*(counter + 1) in input_string:
            counter += 1
        return counter

    # Making a dictionary where all the values will be stored
    dna_str_count = {}
    for sequence in dna_strs_list:
        dna_str_count[sequence] = str(number_of_times(sequence_string, sequence))

    # Defining a function to check whether a dictionary is a subset of the other
    def isSubset(subset, superset):
        if dna_str_count.items() <= d.items():
            return True
        else:
            return False

    # Printing the name if the strs match
    count = 0
    for d in details_listOfdicts:
        if isSubset(dna_str_count, d):
            count += 1
            print(d['name'])

    if count == 0:
        print("No match")

if __name__ == "__main__":
    main()