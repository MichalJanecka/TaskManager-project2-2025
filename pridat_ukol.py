from vytvorit_pripojeni import pripojeni_db

def pridat_ukol(nazev=None, popis=None):
    if nazev is None:
        nazev = input("Zadej název úkolu: ").strip()
    if not nazev:
        print("Název je povinný. Úkol nebyl přidán.")
        return

    if popis is None:
        popis = input("Zadej popis úkolu: ").strip()
    if not popis:
        print("Popis je povinný. Úkol nebyl přidán.")
        return

    conn = pripojeni_db()
    if not conn:
        print("Nelze přidat úkol bez připojení k databázi.")
        return

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT COUNT(*) AS pocet FROM ukoly")
        pocet = cursor.fetchone()['pocet']
        if pocet == 0:
            cursor.execute("ALTER TABLE ukoly AUTO_INCREMENT = 1")
        cursor.execute("""
            INSERT INTO ukoly (nazev, popis)
            VALUES (%s, %s)
        """, (nazev, popis))
        conn.commit()
        print("Úkol byl úspěšně přidán do databáze.")
    except Exception as e:
        print(f"Chyba při přidávání úkolu: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    pridat_ukol()
