import unittest
import preprocess

class TestPreprocess(unittest.TestCase):

    # doesn't matter whether we change newline to whitespace or not
    def test_strip_trailing_whitespaces(self):
        self.assertEqual(preprocess.preprocess("  Nothing personel kidd  \n\r", "e"), "SENTSTART nothing personel kidd SENTEND")



    def test_sentence_final_punct1(self):
        self.assertEqual(preprocess.preprocess("That's what he said.\n", "e"), "SENTSTART that's what he said . SENTEND")

    def test_sentence_final_punct2(self):
        self.assertEqual(preprocess.preprocess("That's what she said!\n", "e"), "SENTSTART that's what she said ! SENTEND")

    def test_sentence_final_punct3(self):
        self.assertEqual(preprocess.preprocess("That's what they said?\n", "e"), "SENTSTART that's what they said ? SENTEND")

    def test_sentence_final_punct4(self):
        self.assertEqual(preprocess.preprocess("Mr. John, please take a seat.\n", "e"), "SENTSTART mr. john, please take a seat . SENTEND")

    def test_sentence_final_punct4(self):
        self.assertEqual(preprocess.preprocess("12.10 p.m.", "e"), "SENTSTART 12.10 p.m . SENTEND")

    def test_regex1(self):
        self.assertEqual(preprocess.preprocess("Mr. Michel Guimond (Beauport-Montmorency-Orleans, BQ)", "e"), "SENTSTART mr. michel guimond ( beauport - montmorency - orleans , bq ) SENTEND")

    def test_regex2(self):
        self.assertEqual(preprocess.preprocess("He said, \"I am the one who knocks.\"", "e"), "SENTSTART He said ,  \" i am the one who knocks. \" SENTEND")

    def test_regex2(self):
        self.assertEqual(preprocess.preprocess("Hon. Jim Peterson (Secretary of State (International Financial Institutions), Lib.):", "e"), "SENTSTART hon. jim peterson ( secretary of state ( international financial institutions ) , lib. ) : SENTEND")

    def test_french1(self):
        self.assertEqual(preprocess.preprocess("(Les deputes recoivent leur bulletin de vote, qu'ils remplissent en secret dans les isoloirs.)  ", "f"), "SENTSTART ( les deputes recoivent leur bulletin de vote , qu ' ils remplissent en secret dans les isoloirs. ) SENTEND")

    def test_empty(self):
        self.assertEqual(preprocess.preprocess("", "f"), "")

    def test_french_end(self):
        self.assertEqual(preprocess.preprocess("j'ai", "f"), "SENTSTART j ' ai SENTEND")

    def test_french2(self):
        self.assertEqual(preprocess.preprocess("he d'ailleurs", "f"), "SENTSTART he d'ailleurs SENTEND")

    def test_french3(self):
        self.assertEqual(preprocess.preprocess("puisqu'on bleh", "f"), "SENTSTART puisqu ' on bleh SENTEND")

if __name__ == '__main__':
    unittest.main()
