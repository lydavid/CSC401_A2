from log_prob import *
from preprocess import *
import pickle
from perplexity import *

english_training_corpus_file = "english.pickle"
french_training_corpus_file = "french.pickle"

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
    sent = preprocess("The Presiding Officer (Mr. Caccia) ", "e")
    #sent = preprocess("The Clerk of the House:", "e")
    #sent = preprocess("clerk the house", "e")
    print(log_prob(sent, e_LM, smoothing=False))#, delta=0.01, vocabSize=vocab_size))


    # let's run perplexity from here as well

    ### English model

    # MLE

    # add-delta x5


    ### French model

    # MLE

    # add-delta x5



if __name__ == "__main__":
	main()