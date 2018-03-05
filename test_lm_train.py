import lm_train

data_dir = "A2_SMT/data/Hansard/Training/"

def main():
	lm_train.lm_train(data_dir, "e", "english")

if __name__ == '__main__':
	main()