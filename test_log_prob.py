from log_prob import *
from preprocess import *
import pickle
from perplexity import *

english_training_corpus_file = "english.pickle"
french_training_corpus_file = "french.pickle"

test_dir = "/u/cs401/A2_SMT/data/Hansard/Testing/"
#test_dir = "A2_SMT/data/Hansard/Testing/"

def main():


    e_LM = {}
    with (open(english_training_corpus_file, "rb")) as openfile:
        e_LM = pickle.load(openfile)

    e_vocab_size = len(e_LM["uni"])

    f_LM = {}
    with (open(french_training_corpus_file, "rb")) as openfile:
        f_LM = pickle.load(openfile)

    f_vocab_size = len(f_LM["uni"])
    
    #print(vocab_size)

    #print(LM)
    #sent = preprocess("The Presiding Officer (Mr. Caccia) ", "e")
    #sent = preprocess("The Clerk of the House:", "e")
    #sent = preprocess("clerk the house", "e")
    #print(log_prob(sent, e_LM, smoothing=False))#, delta=0.01, vocabSize=vocab_size))


    # let's run perplexity from here as well

    ### English model
    print("###English")

    # MLE
    print("MLE: %.2f" % preplexity(e_LM, test_dir, "e"))

    # add-delta
    for i in range(0, 21):
        delta = i * 0.05
        #print("delta %2f" % delta, flush=True)
        print("delta %.2f: %.2f" % (delta, preplexity(e_LM, test_dir, "e", smoothing=True, delta=delta)), flush=True)

    ### French model
    print("###French")

    # MLE
    print("MLE: %.2f" % preplexity(f_LM, test_dir, "f"))

    # add-delta
    for i in range(0, 21):
        delta = i * 0.05
        print("delta %.2f: %.2f" % (delta, preplexity(f_LM, test_dir, "f", smoothing=True, delta=delta)), flush=True)
        #print(round(, flush=True), 2)


if __name__ == "__main__":
    main()