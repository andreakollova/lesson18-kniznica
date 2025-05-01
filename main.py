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
print("Hi, welcome to IT STEP LIBRARY!")
# print("What would you like to do today? for Správa kníh type '1', for Správa členov type '2', for Správa výpožičiek type '3'")

# PRIDANIE ALEBO VYHLADANIE?
# book_management = input("'Správa kníh' --> Type '1' for Pridávanie nových kníh OR '2' for Vyhľadávanie kníh:")
#
# PRIDANIE KNIHY
Book.add_book(conn)

# VYHLADANIE KNIHY
Search.search_book(conn)

# PRIDANIE CLENA
Member.add_member(conn)

# ZOBRAZENIE VYPOZICIEK
ShowLoans.show_loans(conn)


# POZICANIE KNIHY
Loans.book_loan(conn)

cursor.close()
conn.close()