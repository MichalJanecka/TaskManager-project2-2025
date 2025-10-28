from pridat_ukol import pridat_ukol
from zobrazit_ukoly import zobrazit_ukoly
from aktualizovat_ukol import aktualizovat_ukol
from odstranit_ukol import odstranit_ukol

def hlavni_menu():
    while True:
        print("\nHLAVNÍ NABÍDKA")
        print("1. Přidat úkol")
        print("2. Zobrazit úkoly")
        print("3. Aktualizovat úkol")
        print("4. Odstranit úkol")
        print("5. Ukončit program")

        volba = input("Zadej číslo volby (1–5): ").strip()

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            aktualizovat_ukol()
        elif volba == "4":
            odstranit_ukol()
        elif volba == "5":
            print("Program ukončen.")
            break
        else:
            print("Neplatná volba. Zadej číslo od 1 do 5.")

if __name__ == "__main__":
    hlavni_menu()
