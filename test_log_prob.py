import log_prob
import preprocess
import pickle

training_corpus_file = "english.pickle"

def main():


    LM = {}
    with (open(training_corpus_file, "rb")) as openfile:
        LM = pickle.load(openfile)

    vocab_size = len(LM["uni"])
    print(vocab_size)

    #print(LM)
    #sent = preprocess.preprocess("The Presiding Officer (Mr. Caccia) ", "e")
    #sent = preprocess.preprocess("The Clerk of the House:", "e")
    sent = preprocess.preprocess("clerk the house", "e")
    print(log_prob.log_prob(sent, LM, smoothing=False))#, delta=0.01, vocabSize=vocab_size))

if __name__ == "__main__":
	main()