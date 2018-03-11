from BLEU_score import *
from decode import *
from preprocess import *
import pickle

french_path = "/u/cs401/A2_SMT/data/Hansard/Testing/Task5.f"
#french_path = "A2_SMT/data/Hansard/Testing/Task5.f"

human_ref = "/u/cs401/A2_SMT/data/Hansard/Testing/Task5.e"
#human_ref = "A2_SMT/data/Hansard/Testing/Task5.e"

google_ref = "/u/cs401/A2_SMT/data/Hansard/Testing/Task5.google.e"
#google_ref = "A2_SMT/data/Hansard/Testing/Task5.google.e"

LM_path = "english.pickle"
AM_path = "am.pickle"


def evalAlign(fre_dir, LM_path, AM_path):
    LM = {}
    with (open(LM_path, "rb")) as openfile:
        LM = pickle.load(openfile)

    AM = {}
    with (open(AM_path, "rb")) as openfile:
        AM = pickle.load(openfile)

    english_candidates = []

    with open(french_path) as french_file:
        for sentence in french_file:
            english = decode(preprocess(sentence, "f"), LM, AM)  # make sure to preprocess the sentence!
            english_candidates.append(english)
            print(english)

    e_refs = []
    with open(human_ref) as english_file:
        for sentence in english_file:
            e_refs.append(preprocess(sentence, "e"))

    google_e_refs = []
    with open(google_ref) as english_file:
        for sentence in english_file:
            google_e_refs.append(preprocess(sentence, "e"))


    for n_grams_level in range(1, 4):

        print("n_grams_level=%d" % n_grams_level)

        # Calculate BLEU scores
        for i in range(len(english_candidates)):
            bleu_score = BLEU_score(english_candidates[i], [e_refs[i], google_e_refs[i]], n_grams_level)
            print(bleu_score)


if __name__ == "__main__":
    evalAlign(french_path, LM_path, AM_path)
