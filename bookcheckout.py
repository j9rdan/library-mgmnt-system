"""
Contains function to withdraw books by updating Member ID from 0 to user-input 4-digit number.

Date: 08/12/20
By Jordan Edoimioya

-- How to use --
Call checkout() without parameters

"""


def checkout():
    """ Withdraws book from library by requesting Book ID, checking ID validity & availability of requested book. """

    import database
    try:
        is_checked_out = False
        while not is_checked_out:  # stops loop after checkout completes
            book_id_search = input("Enter Book ID: ")
            is_book_id = int(book_id_search) > 0  # criteria for valid Book ID

            if is_book_id:
                books = open("database.txt", "r+")
                for rows in books:
                    b = rows.strip()
                    booklist = b.split(":")
                    search_result = book_id_search == booklist[0]
                    if search_result:
                        print(booklist, "\n")
                        if booklist[5] != '0':
                            print("Book currently unavailable.\n")
                            break

                        else:
                            print("Book is available.\n")
                            is_checked_out = False      # put into while loop if not checked out
                            while not is_checked_out:
                                is_checked_out = True
                                try:
                                    member_id = input("Enter Member ID: ")
                                    is_member_id = 0 < int(member_id) < 9999 and len(member_id) == 4
                                    if is_member_id:
                                        print("Checkout in progress..\n")
                                        list_data = database.read_data("database.txt")
                                        for i in range(len(list_data)):
                                            if list_data[i][0] == booklist[0]:
                                                list_data[i][5] = member_id   # creates new database with new member_id

                                        booklist[5] = member_id
                                        database.processing_delay(3)  # 3-second delay while processing request
                                        print(booklist, "\n")
                                        print("Checkout complete.")
                                        database.processing_delay(1)
                                        is_checked_out = True
                                        database.write_books("database.txt", list_data)
                                        database.write_logs("logfile.txt", "B", book_id_search, booklist[1])
                                        checkout_another = input("Checkout another? [any key] or [N]\n")
                                        if checkout_another == "n".lower():
                                            break
                                        else:
                                            is_checked_out = False  # user wants to check out again
                                    else:
                                        print("Invalid Member ID. Try again")
                                        is_checked_out = False
                                    if not is_checked_out and is_member_id:
                                        break

                                except ValueError:  # rejects invalid numbers & letters
                                    print("Invalid Member ID. Try again")

            else:
                print("Invalid Book ID. Try again")

    except KeyboardInterrupt:  # prevent errors when manually stopping program
        import sys
        sys.exit()

    except ValueError:  # prevents errors when ' ' or chars are entered
        print("Invalid Book ID. Try again")


if __name__ == "__main__":

    print("\nTesting book checkout function..\n\nEnter invalid Book ID NOT in database (0, 99, 'a')\n")
    checkout()
    print("\nSuccessful error-handling - rejects invalid Book IDs by:\n"
          "- repeating loop if: invalid ID or valid ID not in database\n"
          "- terminating process if: chars entered\n")
    print("Enter valid Book IDs in database but currently being borrowed (1,2, 'a')\n")
    checkout()
    print("\nSuccessful error-handling: user notified when books unavailable.\n")
    print("\nEnter valid Book ID in database available for borrow (3) then invalid Member IDs (1,12,123,a)\n")
    checkout()
    print("\nSuccessful error-handling - rejects invalid Member IDs by:\n"
          "- repeating loop if: numbers entered do not meet valid criteria (length = 4, 0-9998)\n"
          "- terminating process if: chars entered\n")
    print("When prompted:\n"
          "1. Enter valid Book ID in database available for borrow (3)\n"
          "2. Enter valid Member ID (1111)\n"
          "3. Select [any key] and repeat process with other valid inputs\n")
    checkout()
    print("\nSuccessful checkout process:\n"
          "- Member ID written to database.txt\n"
          "- Borrow log written to logfile.txt with current date & time\n"
          "- user given option to checkout multiple books\n")
    print("\nTests complete. Checkout function working correctly.")
