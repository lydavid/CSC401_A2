from lm_train import *
from log_prob import *
from preprocess import *
from math import log
import os
import pickle
import glob

SENTSTART = "SENTSTART"
SENTEND = "SENTEND"

def align_ibm1(train_dir, num_sentences, max_iter, fn_AM):
    """
	Implements the training of IBM-1 word alignment algoirthm. 
	We assume that we are implemented P(foreign|english)
	
	INPUTS:
	train_dir : 	(string) The top-level directory name containing data
					e.g., '/u/cs401/A2_SMT/data/Hansard/Testing/'
	num_sentences : (int) the maximum number of training sentences to consider
	max_iter : 		(int) the maximum number of iterations of the EM algorithm
	fn_AM : 		(string) the location to save the alignment model
	
	OUTPUT:
	AM :			(dictionary) alignment model structure
	
	The dictionary AM is a dictionary of dictionaries where AM['english_word']['foreign_word'] 
	is the computed expectation that the foreign_word is produced by english_word.
	
			LM['house']['maison'] = 0.5
	"""
    AM = {}
    
    # Read training data
    # we will have this return a 2D list of form [[1.e.1, 1.e.2, ...], [1.f.1, 1.f.2, ...]]
    # 1.e.2 is sentence 2 of file 1.e, the same index between the two sublists represents alignment of the sentences
    aligned_sentences = read_hansard(train_dir, num_sentences)
    #print(aligned_sentences)

    # Initialize AM uniformly
    # let's just pass in this list of list and have initialize handle everything
    AM = initialize(aligned_sentences)
    
    # manually insert SENTSTART/SENTEND
    AM[SENTSTART] = {}
    AM[SENTSTART][SENTSTART] = 1
    AM[SENTEND] = {}
    AM[SENTEND][SENTEND] = 1

    # Iterate between E and M steps
    #for i in range(len(aligned_sentences[0])):
    eng_sentences = aligned_sentences[0]
    fre_sentences = aligned_sentences[1]
    for i in range(max_iter):
        em_step(AM, eng_sentences, fre_sentences)  # pass AM to function and have it modify it directly!

    return AM
    

# ------------ Support functions --------------
def read_hansard(train_dir, num_sentences):
    """
	Read up to num_sentences from train_dir.
	
	INPUTS:
	train_dir : 	(string) The top-level directory name containing data
					e.g., '/u/cs401/A2_SMT/data/Hansard/Training/'
	num_sentences : (int) the maximum number of training sentences to consider

	OUTPUT:
	aligned_sentences : (list of list of string) aligned_sentences[0][n] is the English sentence aligned with the French sentence aligned_sentences[1][n]
	
	
	Make sure to preprocess!
	Remember that the i^th line in fubar.e corresponds to the i^th line in fubar.f.
	
	Make sure to read the files in an aligned manner.
	"""

    # we assume for that for each .e file, there is a corresponding .f file with the same name in the directory

    aligned_sentences = [[], []]
    e_sentences_read = 0
    f_sentences_read = 0
    

    for filename in glob.iglob(train_dir + "*.e"):

        base_name = os.path.basename(filename)[:-2]
        f_filename = glob.glob(train_dir + base_name + ".f")[0]

        # English
        with open(filename) as english_file:

            if e_sentences_read >= num_sentences:
                break

            for line in english_file:
                if e_sentences_read >= num_sentences:
                    break
                aligned_sentences[0].append(preprocess(line, "e"))
                e_sentences_read += 1

        # French
        with open(f_filename) as french_file:

            if f_sentences_read >= num_sentences:
                break

            for line in french_file:
                if f_sentences_read >= num_sentences:
                    break
                aligned_sentences[1].append(preprocess(line, "f"))
                f_sentences_read += 1

    return aligned_sentences


def initialize(aligned_sentences):
    """
	Initialize alignment model uniformly.
	Only set non-zero probabilities where word pairs appear in corresponding sentences.

    INPUTS:
    aligned_sentences : (list of list of string)
	"""

    initialized_AM = {}

    eng_sentences = aligned_sentences[0]
    fre_sentences = aligned_sentences[1]

    # iterate over eng_sentences
    # build a dictionary with eng word as keys and a set of fre words as values
    # {"house" : set(["maison", "la", "bleu"]), ...}
    eng_word_to_occurence_with_fre_words = {}

    for i in range(len(eng_sentences)):
        eng_tokens = tokenize_and_clean(eng_sentences[i])  # Remove SENTSTART/SENTEND
        fre_tokens = tokenize_and_clean(fre_sentences[i])

        # for each English token, if it's not in our dict, add it with an empty set as its value
        # union to its set a set of all French tokens in this sentence
        for eng_token in eng_tokens:
            if eng_token not in eng_word_to_occurence_with_fre_words:
                eng_word_to_occurence_with_fre_words[eng_token] = set()
            eng_word_to_occurence_with_fre_words[eng_token] |= set(fre_tokens)

    # now build our initialized AM with a uniform probability distribution
    for eng_word in eng_word_to_occurence_with_fre_words.keys():
        num_words_occurences = len(eng_word_to_occurence_with_fre_words[eng_word])  # number of fre words it occurred with
        initialized_AM[eng_word] = {}
        for fre_word in eng_word_to_occurence_with_fre_words[eng_word]:
            initialized_AM[eng_word][fre_word] = 1.0 / num_words_occurences

    return initialized_AM


def tokenize_and_clean(s):
    """
    Tokenize and remove SENTSTART and SENTEND.
    """
    tokens = s.split()
    return tokens[1:-1]

    
def em_step(t, eng, fre):
    """
	One step in the EM algorithm.
	Follows the pseudo-code given in the tutorial slides.
	"""


    # t refers to model parameters, contents of AM
    # In this sense, AM is essentially the t distribution from class, e.g.,
    # >> AM[‘bird’][‘oiseau’] = 0.8   % t(oiseau|bird) = 0.8

    # since we are running the EM algorithm 5-25 times, what is the thing that changes between iterations?
    # from the tut slides, each iter seems to narrow down on alignment of eng to fre words...
    # looks like we can modify the AM itself in the Maximize step
    # which we then use in each iteration for the Expectation step

    # Initialization already handled outside this function

    #eng_words = tokenize_and_clean(eng)
    #fre_words = tokenize_and_clean(fre)

    t_count = {}
    total = {}

    # for each sentence pairs
    for i in range(len(eng)):
        eng_sentence = eng[i]
        fre_sentence = fre[i]
        eng_words = tokenize_and_clean(eng_sentence)
        fre_words = tokenize_and_clean(fre_sentence)

        # Expectation step
        for eng_word in set(eng_words):
            denom_c = 0
            for fre_word in set(fre_words):
                denom_c += t[eng_word][fre_word] * eng_words.count(eng_word)

            if eng_word not in t_count:
                t_count[eng_word] = {}
            for fre_word in set(fre_words):
                if fre_word not in t_count[eng_word]:
                    t_count[eng_word][fre_word] = 0
                t_count[eng_word][fre_word] += (t[eng_word][fre_word] * eng_words.count(eng_word) * fre_words.count(fre_word)) / denom_c

                if fre_word not in total:
                    total[fre_word] = 0
                total[fre_word] += (t[eng_word][fre_word] * eng_words.count(eng_word) * fre_words.count(fre_word)) / denom_c

        #print(t_count)
        #print(total)

    # Maximization step
    for fre_word in total:
        for eng_word in t_count:
            if fre_word in t_count[eng_word]:
                t[eng_word][fre_word] = t_count[eng_word][fre_word] / total[fre_word]
