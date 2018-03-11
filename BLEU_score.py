import math
import sys

def BLEU_score(candidate, references, n):
    """
	Compute the LOG probability of a sentence, given a language model and whether or not to
	apply add-delta smoothing
	
	INPUTS:
	sentence :	(string) Candidate sentence.  "SENTSTART i am hungry SENTEND"
	references:	(list) List containing reference sentences. ["SENTSTART je suis faim SENTEND", "SENTSTART nous sommes faime SENTEND"]
	n :			(int) one of 1,2,3. N-Gram level.

	
	OUTPUT:
	bleu_score :	(float) The BLEU score
	"""
	
	#TODO: Implement by student.
    bleu_score = 0

    candidate_tokens = candidate.split()
    c = len(candidate_tokens)

    r = float("inf")
    references_tokens = []
    for reference in references:
        
        ref_tokens = reference.split()
        references_tokens.append(ref_tokens)
        ref_len = len(ref_tokens)
        if (abs(ref_len - c) < r):
            r = ref_len  # trying to find closest matching token length

    brevity = float(r) / c

    # brevity penalty
    if brevity < 1:
        bp = 1
    else:
        bp = math.exp(1 - brevity)

    # n-gram precision up to n
    # assume cap=2, nevermind, no capping needed
    p1 = 0
    if n >= 1:
        for token in candidate_tokens:
            for ref in references_tokens:
                if token in ref:
                    p1 += 1
                    break
        p1 /= c
        bleu_score = bp * math.pow(p1, 1.0 / n)

    p2 = 0
    if n >= 2:

        # need to construct a list of adjacent pair tuples...
        all_bigram_pairs = []
        for ref in references_tokens:
            bigram_pairs = []
            for i in range(1, len(ref) - 1):
                bigram_pairs.append((ref[i - 1], ref[i]))
            all_bigram_pairs.append(bigram_pairs)

        for i in range(1, len(candidate_tokens) - 1):
            for bigram_pair in bigram_pairs:
                if (candidate_tokens[i - 1], candidate_tokens[i]) in bigram_pair:

                    p2 += 1
                    break
        p2 /= c
        bleu_score = bp * math.pow(p1 * p2, 1.0 / n)




    
    return bleu_score