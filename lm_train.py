from preprocess import *
import pickle
import os

def lm_train(data_dir, language, fn_LM):
    """
	This function reads data from data_dir, computes unigram and bigram counts,
	and writes the result to fn_LM
	
	INPUTS:
	
    data_dir	: (string) The top-level directory continaing the data from which
					to train or decode. e.g., '/u/cs401/A2_SMT/data/Toy/'
	language	: (string) either 'e' (English) or 'f' (French)
	fn_LM		: (string) the location to save the language model once trained
    
    OUTPUT
	
	LM			: (dictionary) a specialized language model
	
	The file fn_LM must contain the data structured called "LM", which is a dictionary
	having two fields: 'uni' and 'bi', each of which holds sub-structures which 
	incorporate unigram or bigram counts
	
	e.g., LM['uni']['word'] = 5 		# The word 'word' appears 5 times
		  LM['bi']['word']['bird'] = 2 	# The bigram 'word bird' appears 2 times.
    """
	
	# TODO: Implement Function

    language_model = {"uni" : {}, "bi" : {}}

    for filename in os.listdir(data_dir):
        if filename.endswith("." + language):
            #print(filename)
            with open(os.path.join(data_dir, filename), "r") as file:
                for line in file:
                    # pass it through preprocessing
                    preprocessed_line = preprocess(line, language)
                    #print(preprocessed_line)

                    # split into tokens
                    tokens = preprocessed_line.split()

                    # each token will be added to uni, incrementing its respective count or making a new entry if it does not exist

                    # each pair of adjacent token will be added to bi, in order

                    # for i == 0 and i == len(tokens) - 1, SENTSTART and SENTEND will be paired with the first and last token respectively
                    # they will also be incremented in uni

                    

                
        

    #Save Model
    with open(fn_LM+'.pickle', 'wb') as handle:
        pickle.dump(language_model, handle, protocol=pickle.HIGHEST_PROTOCOL)
        
    return language_model