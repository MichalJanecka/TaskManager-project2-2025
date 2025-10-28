from vytvorit_pripojeni import pripojeni_db

def aktualizovat_ukol(id=None, novy_nazev=None, novy_popis=None, novy_stav=None):
    conn = pripojeni_db()
    if not conn:
        print("Nelze aktualizovat úkol bez připojení k databázi.")
        return

    try:
        cursor = conn.cursor(dictionary=True)

        if id is None:
            cursor.execute("SELECT id, nazev, stav FROM ukoly")
            ukoly = cursor.fetchall()
            if not ukoly:
                print("Žádné úkoly k aktualizaci.")
                return
            print("\nÚKOLY K AKTUALIZACI:")
            for u in ukoly:
                print(f"ID: {u['id']} | Název: {u['nazev']} | Stav: {u['stav']}")
            while True:
                try:
                    id = int(input("Zadej ID úkolu k aktualizaci: "))
                    cursor.execute("SELECT id FROM ukoly WHERE id = %s", (id,))
                    if cursor.fetchone():
                        break
                    else:
                        print("Úkol s tímto ID neexistuje.")
                except ValueError:
                    print("Zadej platné číslo.")

        cursor.execute("SELECT * FROM ukoly WHERE id = %s", (id,))
        if not cursor.fetchone():
            print(f"Úkol s ID {id} neexistuje.")
            return

        if novy_nazev is None:
            novy_nazev = input("Zadej nový název úkolu: ").strip()
        if novy_popis is None:
            novy_popis = input("Zadej nový popis úkolu: ").strip()
        if novy_stav is None:
            while True:
                novy_stav = input("Zadej nový stav úkolu ('Probíhá' nebo 'Hotovo'): ").strip().capitalize()
                if novy_stav in ["Probíhá", "Hotovo"]:
                    break
                else:
                    print("Neplatný stav. Zadej 'Probíhá' nebo 'Hotovo'.")

        cursor.execute(
            "UPDATE ukoly SET nazev = %s, popis = %s, stav = %s WHERE id = %s",
            (novy_nazev, novy_popis, novy_stav, id)
        )
        conn.commit()
        print(f"Úkol ID {id} byl aktualizován.")

    except Exception as e:
        print(f"Chyba při aktualizaci úkolu: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    aktualizovat_ukol()
