import re
import string

sentence_ending_puncts = [".", "!", "?"]
other_puncts = [",", ":", ";", "(", ")", "+", "-", "<", ">", "=", "'", '"']

def preprocess(in_sentence, language):
    """ 
    This function preprocesses the input text according to language-specific rules.
    Specifically, we separate contractions according to the source language, convert
    all tokens to lower-case, and separate end-of-sentence punctuation 
	
	INPUTS:
	in_sentence : (string) the original sentence to be processed
	language	: (string) either 'e' (English) or 'f' (French)
				   Language of in_sentence
				   
	OUTPUT:
	out_sentence: (string) the modified sentence
    """
    # TODO: Implement Function
    
    # first let's strip any trailing whitespaces
    out_sentence = in_sentence.strip()

    # for sentence-ending punctuations ".!?", check the last token in in_sentence and if it has a punctuation as its last character, separate that
    # if that string belongs to the list of abbrev, then add a whitespace  followed by a period without removing it (12.10 p.m. -> 12.10 p.m. .)
    # Actually, let's just not handle abbreviations cause it's not on the handout
    tokens = out_sentence.split()  # split into individual tokens

    # check last token
    if (tokens[-1][-1] in sentence_ending_puncts):
        # remove it from tokens list
        token = tokens.pop(-1)
        # and re-add as two separatae tokens
        tokens.append(token[:-1])
        tokens.append(token[-1])

    out_sentence = tokens[0]

    # ensure we don't run into out of index error
    if len(tokens) > 1:
        for i in range(1, len(tokens)):
            out_sentence += " " + tokens[i]

    # add spaces between commas, colons, semi-colons, parentheses, dashes between parentheses, math ops, and quotations (assuming they are double quotes)
    # do we need to handle apostrophes? not on the handout...
    out_sentence = re.sub(r"([\,\:\;\(\)\+\-\<\>\=\"])", r" \1 ", out_sentence)

    # remove trailing whitespaces caused by our regex
    out_sentence = out_sentence.strip()

    # convert to tokens then back to remove extra whitespaces in the string
    tokens = out_sentence.split()
    out_sentence = tokens[0]

    # ensure we don't run into out of index error
    if len(tokens) > 1:
        for i in range(1, len(tokens)):
            out_sentence += " " + tokens[i]
    


    return out_sentence