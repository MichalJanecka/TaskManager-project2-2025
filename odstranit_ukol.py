from vytvorit_pripojeni import pripojeni_db

def odstranit_ukol(id=None):
    conn = pripojeni_db()
    if not conn:
        print("Nelze odstranit úkol bez připojení k databázi.")
        return

    try:
        cursor = conn.cursor(dictionary=True)

        if id is None:
            cursor.execute("SELECT id, nazev FROM ukoly")
            ukoly = cursor.fetchall()

            if not ukoly:
                print("Žádné úkoly k odstranění.")
                return

            print("\nÚKOLY K ODSTRANĚNÍ:")
            for u in ukoly:
                print(f"ID: {u['id']} | Název: {u['nazev']}")

            while True:
                try:
                    id = int(input("Zadej ID úkolu k odstranění: "))
                    cursor.execute("SELECT id FROM ukoly WHERE id = %s", (id,))
                    if cursor.fetchone():
                        break
                    else:
                        print("Úkol s tímto ID neexistuje.")
                except ValueError:
                    print("Zadej platné číslo.")

            potvrzeni = input("Opravdu chceš úkol odstranit? (ano/ne): ").strip().lower()
            if potvrzeni != "ano":
                print("Odstranění zrušeno.")
                return
        else:
            cursor.execute("SELECT id FROM ukoly WHERE id = %s", (id,))
            if cursor.fetchone() is None:
                print(f"Úkol s ID {id} neexistuje.")
                return

        print(f"Odstraňuji ID: {id}")
        cursor.execute("DELETE FROM ukoly WHERE id = %s", (id,))
        conn.commit()
        print("Úkol byl odstraněn.")
    except Exception as e:
        print(f"Chyba při odstraňování úkolu: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    odstranit_ukol()
