import csv
import sys
import cs50


def main():

    open("info.db", "w").close()
    db = cs50.SQL("sqlite:///info.db")

    # TODO: Check for command-line usage
    if len(sys.argv) != 2:
        sys.exit("Usage: lol")

    # TODO: Read database file into a variable

    ogg = sys.argv[1]

    with open (ogg, "r") as file:

        reader = csv.DictReader(file)
        for row in reader:
            symp = row["Symbol"]
            db.execute("INSERT INTO stock (symbol) VALUES(?)", symp)

main()
