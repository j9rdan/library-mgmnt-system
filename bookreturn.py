"""
Contains function to return books by updating Member ID from user-input 4-digit number to 0.

Date: 08/12/20
By Jordan Edoimioya

-- How to use --
Call return_book() without parameters

"""


def return_book():
    """ Returns book to library by requesting Book ID, checking ID validity & availability of requested book. """

    import database
    try:
        is_returned = False
        while not is_returned:                                      # stops loop after checkout completes
            book_id_search = input("Enter Book ID: ")
            is_book_id = int(book_id_search) > 0                     # criteria for valid Book ID
            if is_book_id:
                books = open("database.txt", "r")
                for rows in books:
                    b = rows.strip()
                    booklist = b.split(":")
                    search_result = book_id_search == booklist[0]
                    if search_result:
                        print(booklist, "\n")
                        if booklist[5] == '0':
                            print("Book is already available.\n")
                            break
                        else:
                            print("Processing return..\n")
                            list_data = database.read_data("database.txt")
                            for i in range(len(list_data)):
                                if list_data[i][0] == booklist[0]:
                                    list_data[i][5] = '0'  # creates new database with new member_id

                            database.processing_delay(3)
                            booklist[5] = '0'
                            print(booklist, "\n")
                            print("Return complete.")
                            database.processing_delay(1)
                            is_returned = True
                            database.write_books("database.txt", list_data)
                            database.write_logs("logfile.txt", "R", book_id_search, booklist[1])
                            return_more = input("Return another? [any key] or [N]\n")
                            if return_more == "n".lower():
                                break
                            else:
                                is_returned = False
            else:
                print("Invalid Book ID. Try again")

    except KeyboardInterrupt:
        import sys
        sys.exit()

    except ValueError:
        print("Invalid Book ID. Try again")


if __name__ == "__main__":

    print("\nTesting book return function..\n\nEnter invalid Book ID NOT in database (0, 99, 'a')\n")
    return_book()
    print("\nSuccessful error-handling - rejects invalid Book IDs by:\n"
          "- repeating loop if: invalid ID or valid ID not in database\n"
          "- terminating process if: chars entered\n")
    print("Enter valid Book IDs in database but already available (3,6, 'a')\n")
    return_book()
    print("\nSuccessful error-handling: user notified when books already available.\n")
    print("Enter valid Book ID in database unavailable for borrow (1)\n")
    print("When prompted to return another, press any key and repeat return process.\n")
    return_book()
    print("\nSuccessful return process:\n"
          "- Member ID re-written to 0 in database.txt\n"
          "- Return log written to logfile.txt with current date & time\n"
          "- user given option to checkout multiple books\n")
    print("\nTests complete. Return function working correctly.")
