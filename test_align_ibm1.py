from align_ibm1 import *

#train_dir = "/u/cs401/A2_SMT/data/Hansard/Training/"
train_dir = "A2_SMT/data/Hansard/Training/"
output_path = "align"  # will become align.pickle, and saved in this directory
num_sentences = 100
max_iter = 15  # range from 5-25

def main():

    # we are supposed to use Training dir, Testing dir is for Task 5
    print(align_ibm1(train_dir, num_sentences, max_iter, output_path))

if __name__ == "__main__":
    main()