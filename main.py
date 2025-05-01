import psycopg2
from book import Book
from search import Search
from member import Member
from show_loans import ShowLoans
from loans import Loans

conn = psycopg2.connect(
    dbname='bkymtagmsprxn7nktl1i',
    user='uflqb30waldkpepfpndf',
    password='S4KWQihF9543LpzTdlIoJy4xAHEhNe',
    host='bkymtagmsprxn7nktl1i-postgresql.services.clever-cloud.com',
    port='50013'
)

cursor = conn.cursor()

end_program = False
print("Hi, welcome to IT STEP LIBRARY! What would you like to do today?")
while end_program != True:
    what_now = input("Would you like to go MENU? Type YES/NO:")
    if what_now == "YES":
        selection = input("""        M E N U
    Please choose an option:
    1 - BOOK MANAGEMENT
    2 - MEMBER MANAGEMENT
    3 - LOAN MANAGEMENT
    4 - END PROGRAM
    
    Your selection: """)

        if selection == "1":
            book_management = input("To ADD A NEW BOOK type '1', To SEARCH FOR A BOOK type '2':\n")
            if book_management == "1":
                # PRIDANIE KNIHY
                Book.add_book(conn)
            elif book_management == "2":
                # VYHLADANIE KNIHY
                Search.search_book(conn)
            else:
                print("Something went wrong! Please try again or contact support.")

        elif selection == "2":
            print("Welcome to MEMBER MANAGEMENT!")
            # PRIDANIE CLENA
            Member.add_member(conn)

        elif selection == "3":
            loan_management = input("To LOAN A BOOK TO AN EXISTING MEMBER type '1', to SHOW MEMBER LOANS type '2':\n")
            if loan_management == "1":
                # POZICANIE KNIHY
                Loans.book_loan(conn)
            elif loan_management == "2":
                # ZOBRAZENIE VYPOZICIEK
                ShowLoans.show_loans(conn)
            else:
                print("Something went wrong! Please try again or contact support.")

        elif selection == "4":
            end_program = True
            print("Thank you! The program is now shutting down")
    elif what_now == "NO":
        end_program = True
        print("Thank you! The program is now shutting down")
