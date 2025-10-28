from vytvorit_pripojeni import pripojeni_db

def zobrazit_ukoly():
    conn = pripojeni_db()
    if not conn:
        print("Nelze zobrazit úkoly bez připojení k databázi.")
        return

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT id, nazev, popis, stav
            FROM ukoly
            WHERE stav IN ('nezahájeno', 'probíhá')
        """)
        ukoly = cursor.fetchall()

        if not ukoly:
            print("Seznam úkolů je prázdný.")
        else:
            print("\nÚkoly:")
            for u in ukoly:
                print(f"ID: {u['id']} | Název: {u['nazev']} | Popis: {u['popis']} | Stav: {u['stav']}")
    except Exception as e:
        print(f"Chyba při načítání úkolů: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    zobrazit_ukoly()
