from datetime import date

class Loans:
    @staticmethod
    def book_loan(conn):
        cursor = conn.cursor()

        # POZICANIE KNIHY
        loaning_last_name = input("Are you a member? If yes, insert your last name:")
        loaning_copy = input("Type the name of the book title you would like to loan:")

        cursor.execute("SELECT member_id FROM members WHERE last_name = %s", (loaning_last_name,))
        fetched_member_id = cursor.fetchone()[0]

        cursor.execute("""SELECT book_id FROM books WHERE title = %s""", (loaning_copy,))
        fetched_book_id = cursor.fetchone()[0]

        today = date.today()
        loaning_date = today.isoformat()
        loaning_due_date = input("Type in the date you'd like to return the book in the format YYYY-MM-DD:")

        cursor.execute("""
        INSERT INTO loans (book_id, member_id, loan_date, due_date)
        VALUES (%s, %s, %s, %s)""", (fetched_book_id, fetched_member_id, loaning_date, loaning_due_date))
        conn.commit()

        # UPDATNUTIE POCTU KNIH
        cursor.execute("""UPDATE books
        SET copies = copies - 1
        WHERE title = %s""", (loaning_copy,))
        print(f"The book {loaning_copy} has been successfully loaned!")
        conn.commit()