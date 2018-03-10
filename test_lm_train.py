import lm_train

#data_dir = "A2_SMT/data/Hansard/Training/"
data_dir = "/u/cs401/A2_SMT/data/Hansard/Training/"

def main():
	lm_train.lm_train(data_dir, "e", "english")
	lm_train.lm_train(data_dir, "f", "french")

if __name__ == '__main__':
	main()