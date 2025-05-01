class Search:
    @staticmethod
    def search_book(conn):
        cursor = conn.cursor()

        # VYHLADANIE KNIHY
        search_book_input = input("To search for a book by BOOK NAME type '1', by AUTHOR NAME type '2', by GENRE type '3':\n")

        # VYHLADANIE PODLA NAZVU
        if search_book_input == "1":
            search_book = input("Type the book title:")
            cursor.execute(
                """SELECT books.title, authors.name, books.publication_year, books.isbn, books.copies FROM books INNER JOIN authors ON books.author_id = authors.author_id WHERE title = %s""",
                (search_book,))
            print_books = cursor.fetchall()
            print(print_books)

        # VYHLADANIE PODLA AUTORA
        elif search_book_input == "2":
            search_author = input("Type authors name to view all their books:")
            cursor.execute("""
            SELECT books.title FROM authors INNER JOIN books ON authors.author_id = books.author_id WHERE name = %s""", (search_author,))
            print_author = cursor.fetchall()
            print(print_author)

        # VYHLADANIE PODLA ZANRA
        elif search_book_input == "3":
            search_genre = input("Search by genre, available options are 1 - 'Fantasy', 2 - 'Sci-Fi', 3 - 'Detective':")
            cursor.execute(
                """SELECT books.title FROM genres INNER JOIN books ON genres.genre_id = books.genre_id WHERE genres.genre_id = %s""",
                (search_genre,))
            print_genre = cursor.fetchall()
            print(print_genre)


        cursor.close()