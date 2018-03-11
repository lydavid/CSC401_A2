from lm_train import *
from log_prob import *
from preprocess import *
from math import log
import os
import pickle
import glob

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

    print(aligned_sentences)
    # Initialize AM uniformly

    
    # Iterate between E and M steps

    

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


def initialize(eng, fre):
    """
	Initialize alignment model uniformly.
	Only set non-zero probabilities where word pairs appear in corresponding sentences.
	"""
	# TODO
    
def em_step(t, eng, fre):
    """
	One step in the EM algorithm.
	Follows the pseudo-code given in the tutorial slides.
	"""
	# TODO