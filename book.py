class Book:
    @staticmethod
    def add_book(conn):
        cursor = conn.cursor()
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
        VALUES (%s, %s, %s, %s, %s, %s)""", (title, author_id, genre_id, isbn, publication_year, copies))

        conn.commit()
        print(f"The book {title} has been successfully added!")

        cursor.close()