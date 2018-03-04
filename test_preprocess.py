import unittest
import preprocess

class TestPreprocess(unittest.TestCase):

    # doesn't matter whether we change newline to whitespace or not
    def test_strip_trailing_whitespaces(self):
        self.assertEqual(preprocess.preprocess("  Nothing personel kidd  \n\r", "e"), "Nothing personel kidd")



    def test_sentence_final_punct1(self):
        self.assertEqual(preprocess.preprocess("That's what he said.\n", "e"), "That's what he said .")

    def test_sentence_final_punct2(self):
        self.assertEqual(preprocess.preprocess("That's what she said!\n", "e"), "That's what she said !")

    def test_sentence_final_punct3(self):
        self.assertEqual(preprocess.preprocess("That's what they said?\n", "e"), "That's what they said ?")

    def test_sentence_final_punct4(self):
        self.assertEqual(preprocess.preprocess("Mr. John, please take a seat.\n", "e"), "Mr. John, please take a seat .")

    def test_sentence_final_punct4(self):
        self.assertEqual(preprocess.preprocess("12.10 p.m.", "e"), "12.10 p.m .")

    def test_regex1(self):
        self.assertEqual(preprocess.preprocess("Mr. Michel Guimond (Beauport-Montmorency-Orleans, BQ)", "e"), "Mr. Michel Guimond ( Beauport - Montmorency - Orleans , BQ )")

    def test_regex2(self):
        self.assertEqual(preprocess.preprocess("He said, \"I am the one who knocks.\"", "e"), "He said ,  \" I am the one who knocks. \"")

    def test_regex2(self):
        self.assertEqual(preprocess.preprocess("Hon. Jim Peterson (Secretary of State (International Financial Institutions), Lib.):", "e"), "Hon. Jim Peterson ( Secretary of State ( International Financial Institutions ) , Lib. ) :")

    def test_french1(self):
        self.assertEqual(preprocess.preprocess("(Les deputes recoivent leur bulletin de vote, qu'ils remplissent en secret dans les isoloirs.)  ", "f"), "( Les deputes recoivent leur bulletin de vote , qu ' ils remplissent en secret dans les isoloirs. )")

    def test_empty(self):
        self.assertEqual(preprocess.preprocess("", "f"), "")

    def test_french_end(self):
        self.assertEqual(preprocess.preprocess("j'ai", "f"), "j ' ai")

    def test_french2(self):
        self.assertEqual(preprocess.preprocess("he d'ailleurs", "f"), "he d'ailleurs")

    def test_french3(self):
        self.assertEqual(preprocess.preprocess("puisqu'on bleh", "f"), "puisqu ' on bleh")

if __name__ == '__main__':
    unittest.main()
