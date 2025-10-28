import mysql.connector
from mysql.connector import Error

def pripojeni_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            port=3307,
            user="root",
            password="1111",
            database="project2"
        )
        return conn
    except Error as e:
        print(f"Chyba při připojení: {e}")
        return None

if __name__ == "__main__":
    conn = pripojeni_db()
    if conn:
        print("Připojení k databázi je funkční.")
        conn.close()
    else:
        print("Připojení se nezdařilo.")
