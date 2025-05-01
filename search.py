class Search:
    @staticmethod
    def search_book(conn):
        cursor = conn.cursor()

        # VYHLADANIE KNIHY
        print("Select to search a book by author name, author or genre:")

        # VYHLADANIE PODLA NAZVU
        search_book = input("Type the book title:")
        cursor.execute(
            """SELECT books.title, authors.name, books.publication_year, books.isbn, books.copies FROM books INNER JOIN authors ON books.author_id = authors.author_id WHERE title = %s""",
            (search_book,))
        print_books = cursor.fetchall()
        print(print_books)

        # VYHLADANIE PODLA AUTORA
        search_author = input("Type authors name to view all their books:")
        cursor.execute("""
        SELECT books.title FROM authors INNER JOIN books ON authors.author_id = books.author_id WHERE name = %s""",
                       (search_author,))
        print_author = cursor.fetchall()
        print(print_author)

        # VYHLADANIE PODLA ZANRA
        search_genre = input("Search by genre, available options are 1 - 'Fantasy', 2 - 'Sci-Fi', 3 - 'Detective':")
        cursor.execute(
            """SELECT books.title FROM genres INNER JOIN books ON genres.genre_id = books.genre_id WHERE genres.genre_id = %s""",
            (search_genre,))
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

        cursor.close()