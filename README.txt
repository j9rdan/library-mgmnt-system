--- NOTES ---

- logfile.txt formed from artificial dates but logs according to current datetime
- logs not sorted after write (written to bottom of list)
- could not install matplotlib on laptop --> no chance to show data visualisation

___________


--- EXTRA FEATURES ---

BOOKSEARCH.PY

- choose search (display all/ID/ISBN/title/author) + input error message when wrong option selected
- added short delay when loading all books
- prevent keyboard interrupt error

BOOKCHECKOUT.PY / BOOKRETURN.PY

- loop until checkout/return completes
- loop if member ID invalid --> stops when valid
- prevent keyboard interrupt error
- option to borrow/return another --> repeats loop if yes, breaks if no
- added short delay when processing checkout/return
- doesn't allow you to checkout/return once member id written

