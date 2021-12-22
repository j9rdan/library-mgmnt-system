"""
Contains function to display no. of borrows for books given as parameters, used to visualise which should be removed
from the library.

Date: 13/12/20
By Jordan Edoimioya

-- How to use --
Call calc_total_borrows(isbn_abbr) where isbn_abbr = the last 3 digits of a Book ISBN.
"""


def calc_total_borrows(isbn_abbr):
    """ Calculates number of borrows/returns of a book.

    isbn_abbr = abbreviated ISBN - last 3 digits """

    import database
    loglist = database.read_logs("logfile.txt")
    isbn_and_action = [[logs[1][10:], logs[2]] for logs in loglist]  # list of last 3 digits of ISBN and action (B/R)
    total = 0
    for each_log in isbn_and_action:
        borrows = isbn_and_action and each_log[0] == isbn_abbr and each_log[1] == 'B'   # show borrows for each title
        if borrows:
            total += 1

    return total


if __name__ == "__main__":

    print("\nTesting function to calculate total number of borrows..\n(Verify using logfile.txt)\n")
    option = input("Enter:\n"
                   "[any key] = calculate total borrows for a book\n"
                   "[n] = quit\n")
    if option != 'n'.lower():
        while True:
            isbn_abbr = input("\nLast 3 digits of ISBN: ")
            result = calc_total_borrows(isbn_abbr)
            if isbn_abbr == "n".lower():
                import sys
                sys.exit()
            else:
                print("No. of borrows for Book 9783161484" + isbn_abbr + ":", result)
    else:
        import sys
        sys.exit()

