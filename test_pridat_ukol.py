import unittest
from vytvorit_pripojeni import pripojeni_db
from pridat_ukol import pridat_ukol

class TestPridatUkol(unittest.TestCase):
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

    def test_pozitivni_pridani(self):
        pridat_ukol(nazev="Test úkol", popis="Test popis")
        self.cursor.execute("SELECT COUNT(*) AS pocet FROM ukoly")
        pocet = self.cursor.fetchone()["pocet"]
        self.assertEqual(pocet, 1)

    def test_negativni_pridani_bez_nazvu(self):
        pridat_ukol(nazev="", popis="Popis bez názvu")
        self.cursor.execute("SELECT COUNT(*) AS pocet FROM ukoly")
        pocet = self.cursor.fetchone()["pocet"]
        self.assertEqual(pocet, 0)

if __name__ == "__main__":
    unittest.main()
