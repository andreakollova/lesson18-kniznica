class ShowLoans:
    @staticmethod
    def show_loans(conn):
        cursor = conn.cursor()
        search_loans = input("Insert the last name of member whose loans you want to view:")
        cursor.execute(
            """SELECT members.first_name, members.last_name, loans.book_id, loans.loan_date, loans.due_date FROM loans INNER JOIN members ON loans.member_id = members.member_id WHERE members.last_name = %s""",
            (search_loans,))
        print_loans = cursor.fetchall()
        print(print_loans)

        cursor.close()