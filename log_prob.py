from preprocess import *
from lm_train import *
from math import log


def word_prob(word, context, LM, smoothing=False, delta=0, vocabSize=0):
    """
    Helper function to compute the MLE or Add-delta smoothing Laplace of a single word given context.
    The rest of the inputs are the same as from log_prob.
    Since python passes arguments by reference, it won't slow down performance passing huge dict LM.
    """

    # make sure word exist in our unigram dict
    if (word in LM["uni"]):
        word_count = LM["uni"][word]
    else:
        word_count = 0

    # make sure word exist in our bigram dict under context and that context exists
    if (context in LM["bi"] and word in LM["bi"][context]):
        word_with_context_count = LM["bi"][context][word]
    else:
        word_with_context_count = 0

    # separate our calculations in case of erroneous inputs of smoothing=False, delta=n, n!=0
    if smoothing:
        word_prob = log(word_with_context_count + delta, 2) / float(word_count + delta * vocabSize)
    else:
        # MLE
        if (word_count == 0 or word_with_context_count == 0):
            return 0
        else:
            word_prob = log(word_with_context_count, 2) / float(word_count)

    return word_prob


def log_prob(sentence, LM, smoothing=False, delta=0, vocabSize=0):
    """
	Compute the LOG probability of a sentence, given a language model and whether or not to
	apply add-delta smoothing
	
	INPUTS:
	sentence :	(string) The PROCESSED sentence whose probability we wish to compute
	LM :		(dictionary) The LM structure (not the filename)
	smoothing : (boolean) True for add-delta smoothing, False for no smoothing
	delta : 	(float) smoothing parameter where 0<delta<=1
	vocabSize :	(int) the number of words in the vocabulary
	
	OUTPUT:
	log_prob :	(float) log probability of sentence
	"""
	
	#TODO: Implement by student.
    print(sentence)

    # those formulas given in handout allows us to compute the prob of current word given previous word
    # for this task, we must do that for each word and return the log prob of the entire sentence
    if (smoothing):
        print("add-delta")
    else:
        print("mle")

    # add rather then multiply for log probabilities (normal probabilities is multiply)
    log_prob = 0  # starting prob, will work cause we are multiplying a bunch of probs < 1
    # compute word_prob for each pair of adjacent tokens and multiply their results together
    tokens = sentence.split()  # from our preprocess, we can split on spaces

    if (len(tokens) > 1):

        # we start on the token right after SENTSTART
        for i in range(1, len(tokens)):
            # current token is the word we wish to find prob of, and word before this word is the context for our bigram
            log_prob += word_prob(tokens[i], tokens[i - 1], LM, smoothing, delta, vocabSize)

    return log_prob
