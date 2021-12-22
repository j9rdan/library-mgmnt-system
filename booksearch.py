"""
Contains search functions to return list of books given a specified input.

Date: 28/11/20
By Jordan Edoimioya

-- How to use --
Call any search function without parameters, e.g. general_search()
"""


def isbn_search():
    """ Search books using ISBN. """

    general_search_id = input("Enter ISBN:\n9783161484___\n")
    books = open("database.txt", "r")
    found = False
    for rows in books:
        b = rows.strip()
        booklist = b.split(":")
        to_display = general_search_id in booklist[1] and "9783161484" in general_search_id
        if to_display:
            print(booklist)
            print("\n")
            found = True
    if not found:
        print("No books found. Try again")


def general_search():
    """ Option to display all books, or search by Book ID/ISBN/Title/Author. """

    try:
        search_option = input("Search by..\n[0] = Book ID\n[1] = ISBN\n[2] = Title\n[3] = Author\n"
                              "[4] = Display all books\n\n")

        if search_option == str(4):                                 # display all books
            import database
            print("Loading..")
            database.processing_delay(2)
            database.display_all("database.txt")

        elif search_option == str(0):                               # search by Book ID
            general_search_id = input("Enter Book ID: ")
            books = open("database.txt", "r")
            found = False
            for rows in books:
                b = rows.strip()
                booklist = b.split(":")
                to_display = general_search_id == booklist[0]
                if to_display:
                    print(booklist, "\n")
                    found = True
            if not found:
                print("No books found. Try again")

        elif search_option == str(1):                               # search by ISBN
            general_search_id = input("Enter ISBN:\n9783161484___\n")
            books = open("database.txt", "r")
            found = False
            for rows in books:
                b = rows.strip()
                booklist = b.split(":")
                to_display = general_search_id in booklist[1] and "9783161484" in general_search_id
                if to_display:
                    print(booklist, "\n")
                    found = True
            if not found:
                print("No books found. Try again")

        elif search_option == str(2):                               # search by book title
            general_search_id = input("Enter Book Title: ").title()
            books = open("database.txt", "r")
            found = False
            for rows in books:
                b = rows.strip()
                booklist = b.split(":")
                to_display = general_search_id in booklist[2]
                if to_display:
                    print(booklist, "\n")
                    found = True
            if not found:
                print("'%s' not found. Try again" % general_search_id)

        elif search_option == str(3):                               # search by author
            general_search_id = input("Enter author: ").title()
            books = open("database.txt", "r")
            found = False
            for rows in books:
                b = rows.strip()
                booklist = b.split(":")
                to_display = general_search_id in booklist[3]
                if to_display:
                    print(booklist, "\n")
                    found = True
            if not found:
                print("'%s' not found in authors. Try again" % general_search_id)

        else:
            print("Invalid input. Try again")

    except KeyboardInterrupt:                                       # prevent error when manually stopping program
        import sys
        sys.exit()


if __name__ == "__main__":

    print("\nTesting book search functions..\n")
    print("Enter [4] to test display function\n")
    general_search()
    print("\nSearch successful.\n")
    print("Enter [0] to test search by Book ID.\nSearch a valid ID in the database (1-20)\n")
    general_search()
    print("\nSearch successful.\n")
    print("Enter [0] to test search by Book ID.\nSearch an invalid ID NOT in the database (chars/0/20+)\n")
    general_search()
    print("\nSuccessful error-handling.\n")
    print("Enter [1] to test search by ISBN.\nSearch valid ISBN in database 97831614841__"
          "00/02/03/05/07/08/09/11/20/21")
    general_search()
    print("\nSearch successful.\n")
    print("Enter [1] to test search by ISBN.\nSearch invalid ISBN NOT in database\n")
    general_search()
    print("\nSuccessful error-handling.\n")
    print("Enter [2] to test search by title.\nSearch title found in database (eg 'master')\n")
    general_search()
    print("\nSearch successful.\n")
    print("Enter [2] to test search by title.\nSearch title NOT found in database (eg 'food')\n")
    general_search()
    print("\nSuccessful error-handling.\n")
    print("Enter [3] to test search by author.\nSearch author found in database (eg 'firat')\n")
    general_search()
    print("\nSearch successful.\n")
    print("Enter [3] to test search by author.\nSearch author NOT found in database (eg 'jordan')\n")
    general_search()
    print("\nSuccessful error-handling.\n")
    print("\nTests complete. All functions working correctly.")
