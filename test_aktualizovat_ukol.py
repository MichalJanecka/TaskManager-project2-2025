import unittest
from vytvorit_pripojeni import pripojeni_db
from aktualizovat_ukol import aktualizovat_ukol

class TestAktualizovatUkol(unittest.TestCase):
    def setUp(self):
        self.conn = pripojeni_db()
        self.cursor = self.conn.cursor(dictionary=True)
        self.cursor.execute("DELETE FROM ukoly")
        self.conn.commit()

    def tearDown(self):
        self.cursor.execute("DELETE FROM ukoly")
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def test_pozitivni_aktualizace(self):
        self.cursor.execute("INSERT INTO ukoly (nazev, popis, stav) VALUES (%s, %s, %s)", ("Původní název", "Popis", "nezahájeno"))
        self.conn.commit()
        self.cursor.execute("SELECT id FROM ukoly LIMIT 1")
        ukol_id = self.cursor.fetchone()["id"]
        aktualizovat_ukol(id=ukol_id, novy_nazev="Aktualizovaný název", novy_popis="Nový popis", novy_stav="hotovo")
        conn_check = pripojeni_db()
        cursor_check = conn_check.cursor(dictionary=True)
        cursor_check.execute("SELECT * FROM ukoly WHERE id = %s", (ukol_id,))
        ukol = cursor_check.fetchone()
        cursor_check.close()
        conn_check.close()
        self.assertEqual(ukol["nazev"], "Aktualizovaný název")
        self.assertEqual(ukol["stav"], "hotovo")

    def test_negativni_aktualizace_neexistujici_id(self):
        aktualizovat_ukol(id=1234, novy_nazev="X", novy_popis="Y", novy_stav="hotovo")
        self.cursor.execute("SELECT COUNT(*) AS pocet FROM ukoly")
        pocet = self.cursor.fetchone()["pocet"]
        self.assertEqual(pocet, 0)

if __name__ == "__main__":
    unittest.main()
