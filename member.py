from datetime import date

class Member:
    @staticmethod
    def add_member(conn):
        cursor = conn.cursor()
        print("To add a new member, fill in the members details:")
        first_name = input("Insert first name:")
        last_name = input("Insert last name:")
        email = input("Insert email:")
        today = date.today()
        registration_date = today.isoformat()

        cursor.execute("""
                 INSERT INTO members (first_name, last_name, email, registration_date)
                 VALUES (%s, %s, %s, %s)""", (first_name, last_name, email, registration_date))
        conn.commit()
        print(f"The member {first_name} {last_name} has been successfully added!")

        cursor.close()