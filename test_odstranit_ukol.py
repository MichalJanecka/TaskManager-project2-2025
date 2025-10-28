import unittest
from vytvorit_pripojeni import pripojeni_db
from odstranit_ukol import odstranit_ukol

class TestOdstranitUkol(unittest.TestCase):
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

    def test_pozitivni_odstraneni(self):
        self.cursor.execute("INSERT INTO ukoly (nazev, popis) VALUES (%s, %s)", ("Úkol k odstranění", "Popis"))
        self.conn.commit()
        self.cursor.execute("SELECT id FROM ukoly LIMIT 1")
        ukol_id = self.cursor.fetchone()["id"]
        odstranit_ukol(id=ukol_id)
        conn_check = pripojeni_db()
        cursor_check = conn_check.cursor(dictionary=True)
        cursor_check.execute("SELECT COUNT(*) AS pocet FROM ukoly")
        pocet = cursor_check.fetchone()["pocet"]
        cursor_check.close()
        conn_check.close()
        self.assertEqual(pocet, 0)

    def test_negativni_odstraneni_neexistujici_id(self):
        odstranit_ukol(id=1234)
        self.cursor.execute("SELECT COUNT(*) AS pocet FROM ukoly")
        pocet = self.cursor.fetchone()["pocet"]
        self.assertEqual(pocet, 0)

if __name__ == "__main__":
    unittest.main()
