"""
Combines all separate functionalities into one menu using CLI.

Date: 17/12/20
By Jordan Edoimioya

-- How to use --
Run the module and follow the menu in the CLI.
"""


def main_menu():
    """ Options to navigate menu between all imported modules. """

    menu_option = input("[S] = search for a book / view library\n"
                        "[C] = checkout a book\n"
                        "[R] = return a book\n"
                        "[W] = weed books & view unpopular titles\n"
                        "[Q] = quit\n\n").title()
    return menu_option


print("\n" + 50 * "~")
print(19 * "~", "MAIN MENU", 20 * "~")     # display banner
print(50 * "~", "\n")

choice = main_menu()

try:
    while True:
        if choice == "S":
            import booksearch
            booksearch.general_search()
            go_back = input("\nBack to main menu? [M]\n[Q] to quit\n").title()
            if go_back == "M":
                choice = main_menu()    # option to return to main menu after function completed
            else:
                break

        elif choice == "C":
            import bookcheckout
            bookcheckout.checkout()
            go_back = input("\nBack to main menu? [M]\n[Q] to quit\n").title()
            if go_back == "M":
                choice = main_menu()
            else:
                break

        elif choice == "R":
            import bookreturn
            bookreturn.return_book()
            go_back = input("\nBack to main menu? [M]\n[Q] to quit\n").title()
            if go_back == "M":
                choice = main_menu()
            else:
                break

        elif choice == "W":
            import bookweed
            borrows_103 = bookweed.calc_total_borrows('103')
            borrows_111 = bookweed.calc_total_borrows('111')
            borrows_109 = bookweed.calc_total_borrows('109')
            from booksearch import isbn_search
            print("Enter: 103, 111, 109 to view books for suggested removal")
            isbn_search()
            print("Unpopular book - Total borrows: %s\n" % borrows_103)
            isbn_search()
            print("Unpopular book - Total borrows: %s\n" % borrows_111)
            isbn_search()
            print("Unpopular book - Total borrows: %s\n" % borrows_109)
            go_back = input("\nBack to main menu? [M]\n[Q] to quit\n").title()
            if go_back == "M":
                choice = main_menu()
            else:
                break

        elif choice == "Q":
            import sys
            sys.exit()

        else:
            print("Unrecognised input. Try again")
            break

except KeyboardInterrupt:
    import sys
    sys.exit()


""" All functions imported have been tested and are fully functional. """
