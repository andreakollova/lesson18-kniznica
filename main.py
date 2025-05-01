import psycopg2
from datetime import date

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
#
book_management = input("'Správa kníh' --> Type '1' for Pridávanie nových kníh OR '2' for Vyhľadávanie kníh:")

# PRIDANIE KNIHY
print("To add a book, first you need to add an author")
name = input("Insert author name:")
bio = input("Insert author bio:")

cursor.execute("""
INSERT INTO authors (name, bio)
VALUES (%s, %s)""", (name, bio))

cursor.execute("SELECT author_id FROM authors WHERE name = %s", (name,))
nameAuthor = cursor.fetchone()[0]

conn.commit()
print("New author was added! Now let's add the book:")

title = input("Insert book title:")
author_id = nameAuthor
genre_id = input("Insert genre, type '1' for Fantasy, '2' for Drama:")
isbn = input("Insert ISBN:")
publication_year = input("Insert publication year:")
copies = input("Insert number of copies:")

cursor.execute("""
INSERT INTO books (title, author_id, genre_id, isbn, publication_year, copies)
VALUES (%s, %s, %s, %s, %s, %s)""", (title, author_id, genre_id, isbn, publication_year, copies) )

conn.commit()
print(f"The book {title} has been successfully added!")

# VYHLADANIE KNIHY
print("Select to search a book by author name, author or genre:")

# VYHLADANIE PODLA NAZVU
search_book = input("Type the book title:")
cursor.execute("""SELECT books.title, authors.name, books.publication_year, books.isbn, books.copies FROM books INNER JOIN authors ON books.author_id = authors.author_id WHERE title = %s""", (search_book,))
print_books = cursor.fetchall()
print(print_books)

# VYHLADANIE PODLA AUTORA
search_author = input("Type authors name to view all their books:")
cursor.execute("""
SELECT books.title FROM authors INNER JOIN books ON authors.author_id = books.author_id WHERE name = %s""", (search_author,))
print_author = cursor.fetchall()
print(print_author)

# VYHLADANIE PODLA ZANRA
search_genre = input("Search by genre, available options are 1 - 'Fantasy', 2 - 'Sci-Fi', 3 - 'Detective':")
cursor.execute("""SELECT books.title FROM genres INNER JOIN books ON genres.genre_id = books.genre_id WHERE genres.genre_id = %s""",(search_genre,))
print_genre = cursor.fetchall()
print(print_genre)

# PRIDANIE CLENA
print("To add a new member, fill in the members details:")
first_name = input("Insert first name:")
last_name = input("Insert last name:")
email = input("Insert email:")
registration_date = input("Insert registration date in the format YYYY-MM-DD:")

cursor.execute("""
INSERT INTO members (first_name, last_name, email, registration_date)
VALUES (%s, %s, %s, %s)""", (first_name, last_name, email, registration_date))
conn.commit()
print(f"The member {first_name} {last_name} has been successfully added!")

# ZOBRAZENIE VYPOZICIEK
search_loans = input("Insert the last name of member whose loans you want to view:")
cursor.execute("""SELECT members.first_name, members.last_name, loans.book_id, loans.loan_date, loans.due_date FROM loans INNER JOIN members ON loans.member_id = members.member_id WHERE members.last_name = %s""", (search_loans,))
print_loans = cursor.fetchall()
print(print_loans)

# POZICANIE KNIHY
loaning_last_name = input("Are you a member? If yes, insert your last name:")
loaning_copy = input("Type the name of the book title you would like to loan:")

cursor.execute("SELECT member_id FROM members WHERE last_name = %s", (loaning_last_name,))
fetched_member_id = cursor.fetchone()[0]

cursor.execute("""SELECT book_id FROM books WHERE title = %s""", (loaning_copy,))
fetched_book_id = cursor.fetchone()[0]

today = date.today()
loaning_date = today.isoformat()
loaning_due_date = input("Type in the date you'd like to return the book in the format YYYY-MM-DD")

cursor.execute("""
INSERT INTO loans (book_id, member_id, loan_date, due_date)
VALUES (%s, %s, %s, %s)""",(fetched_book_id, fetched_member_id, loaning_date, loaning_due_date) )
conn.commit()

# UPDATNUTIE POCTU KNIH
cursor.execute("""UPDATE books
SET copies = copies - 1
WHERE title = %s""", (loaning_copy,))
print(f"The book {loaning_copy} has been successfully loaned!")
conn.commit()

cursor.close()
conn.close()
