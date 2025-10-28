from vytvorit_pripojeni import pripojeni_db

def vytvoreni_tabulky():
    conn = pripojeni_db()
    if not conn:
        print("Nelze ověřit tabulku bez připojení k databázi.")
        return

    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT COUNT(*)
            FROM information_schema.tables
            WHERE table_schema = DATABASE()
              AND table_name = 'ukoly'
        """)
        exists = cursor.fetchone()[0]

        if exists:
            print("Tabulka 'ukoly' již existuje.")
        else:
            cursor.execute("""
                CREATE TABLE ukoly (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nazev VARCHAR(255) NOT NULL,
                    popis TEXT NOT NULL,
                    stav ENUM('nezahájeno', 'hotovo', 'probíhá') NOT NULL DEFAULT 'nezahájeno',
                    datum_vytvoreni DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()
            print("Tabulka 'ukoly' byla úspěšně vytvořena.")
    except Exception as e:
        print(f"Chyba při vytváření nebo ověřování tabulky: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    vytvoreni_tabulky()
