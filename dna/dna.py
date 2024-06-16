import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: lol")

    # TODO: Read database file into a variable
    list = []
    egg ={}
    ogg = sys.argv[1]
    hi = 1
    bee = 0
    a = 1
    one = 0

    with open (ogg, "r") as file:

        reader = csv.DictReader(file)

        for person in reader:
            if hi == 1:
                for i in range(len(person.keys())):
                    bee = bee + 1

            hi = 0
    with open (ogg, "r") as file2:
        reader2 = csv.reader(file2)

        for person in reader2:

            if one == 0:

                for k in range(bee-1):

                    list.append(person[k+1])
            if one == 1:
                for i in range(bee-1):
                    a = int(person[i+1])*a

            egg[a] = person[0]
            one = 1
            a = 1



    # TODO: Read DNA sequence file into a variable

    kno = sys.argv[2]
    with open(kno , "r") as fe:
        ha = fe.read()


    # TODO: Find longest match of each STR in DNA sequence
    ke = 1
    for i in list:

        ke = longest_match(ha, i)*ke

    # TODO: Check database for matching profiles

    for hel in egg:
       
        if hel == ke:
            print(f"{egg[ke]}")
            sys.exit()
    print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
