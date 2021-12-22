"""
Contains useful functions used across all modules such as reading/writing file data & displaying all file data as lists.

Date: 07/12/20
By Jordan Edoimioya

-- How to use --
Read data by calling  read_from("filename.extension")           e.g. read_from("logfile.txt")
Display data by calling  display_all("filename.extension")      e.g. display_all("database.txt")
Delay executions by calling processing_delay(secs)              e.g. processing_delay(3)
"""


def read_data(filename):
    """ Reads from a specified file

    filename = name of file to read (format = 'filename.extension', e.g. 'file.txt') """

    booklist = []
    all_books = open(filename, "r")
    for rows in all_books:
        clean_rows = rows.strip()
        books = clean_rows.split(":")
        booklist.append(books)

    return booklist


def write_books(filename, database):
    """ Writes a file after modification.

    filename = name of the file to be written (format = 'filename.extension', e.g. 'file.txt')
    database = source of all data """

    books = open(filename, "w+")
    for each_list in database:
        each_list = ":".join(each_list)
        books.write(str(each_list) + "\n")


def read_logs(filename):
    """ Reads log file and puts into list.

     filename = name of the file to be written (format = 'filename.extension', e.g. 'file.txt') """

    loglist = []
    all_logs = open(filename, "r+")
    for rows in all_logs:
        rows = rows.strip()
        logs = rows.split("|")
        loglist.append(logs)

    return loglist


def write_logs(filename, action, book_id, book_isbn):
    """ Create log whenever a book is withdrawn/returned.

    filename = name of the file to be written (format = 'filename.extension', e.g. 'file.txt')
    action = borrow ('B') or return ('R')
    book_id = Book ID number from user input
    book_isbn = Book ISBN found using book ID search """

    import datetime
    current_date = datetime.date.today().strftime("%d/%m/%y")
    current_time = datetime.datetime.now().strftime("%H:%M")

    loglist = read_logs(filename)
    loglist.append([book_id, book_isbn, action, current_date, current_time])
    new_logs = open(filename, "w+")

    for logs in loglist:
        logs = "|".join(logs)   # converts from list into original log format
        new_logs.write(str(logs) + "\n")


def display_all(filename):
    """ Displays all data (database/logfile) as list

    filename = name of file to list data (format = 'filename.extension', e.g. 'file.txt') """

    books = open(filename, "r")
    for rows in books:
        b = rows.strip()
        booklist = b.split(":")
        print(booklist)
    print("\n")

    books.close()


def processing_delay(time):
    """ Allows commands to be separated by short delays.

    time = number of seconds for delay """

    from time import sleep
    sleep(time)


if __name__ == "__main__":

    print("\nTesting database functions..\n\nChoose a function to test below:\n")
    tests_incomplete = True
    while tests_incomplete:
        test_option = input("Enter:\n"
                            "[1] = read_data('database.txt')\n"
                            "[2] = write_books('database.txt', list_data=read_data('database.txt'))\n"
                            "[3] = read_logs('logfile.txt')\n"
                            "[4] = write_logs('logfile.txt', 'B', '21', '9783161484121'))\n"
                            "[5] = display_all('database.txt')\n"
                            "[6] = processing_delay(3)\n"
                            "[Q] = quit testing\n\n")

        if test_option == str(1):
            print("\nReading database..\n")
            processing_delay(2)
            print(read_data("database.txt"))
            print("\nDatabase read successfully.\n")
            test_another = input("Test another function? [any key] or [N]\n\n")
            if test_another == "N".lower():
                print("Tests complete. All functions working correctly")
                tests_incomplete = False
                break
            else:
                tests_incomplete = True

        elif test_option == str(2):
            print("\nWriting database..\n")
            processing_delay(2)
            write_books("database.txt", database=read_data("database.txt"))
            print("Database written successfully. (check database.txt)\n")
            test_another = input("Test another function? [any key] or [N]\n\n")
            if test_another == "N".lower():
                print("Tests complete. All functions working correctly")
                tests_incomplete = False
                break
            else:
                tests_incomplete = True

        elif test_option == str(3):
            print("\nReading logfile..\n")
            processing_delay(3)
            print(read_logs("logfile.txt"))
            print("\nLogfile read successfully.\n")
            test_another = input("Test another function? [any key] or [N]\n\n")
            if test_another == "N".lower():
                print("Tests complete. All functions working correctly")
                tests_incomplete = False
                break
            else:
                tests_incomplete = True

        elif test_option == str(4):
            print("\nWriting an example log..\n(to be removed after write)\n")
            processing_delay(1)
            write_logs('logfile.txt', 'B', '21', '9783161484123')
            print("Log successfully written. (check logfile.txt)")
            test_another = input("Test another function? [any key] or [N]\n\n")
            if test_another == "N".lower():
                print("Tests complete. All functions working correctly")
                tests_incomplete = False
                break
            else:
                tests_incomplete = True

        elif test_option == str(5):
            print("\nLoading all contents..\n")
            processing_delay(2)
            display_all("database.txt")
            print("\nContents successfully displayed.\n")
            test_another = input("Test another function? [any key] or [N]\n\n")
            if test_another == "N".lower():
                print("Tests complete. All functions working correctly")
                tests_incomplete = False
                break
            else:
                tests_incomplete = True

        elif test_option == str(6):
            print("\nTesting time delay of 3 seconds..\n")
            processing_delay(3)
            print("Test complete. Time delay successful.\n")
            test_another = input("Test another function? [any key] or [N]\n\n")
            if test_another == "N".lower():
                print("Tests complete. All functions working correctly")
                tests_incomplete = False
                break
            else:
                tests_incomplete = True

        else:
            print("Tests complete. All functions working correctly")
            import sys
            sys.exit()
