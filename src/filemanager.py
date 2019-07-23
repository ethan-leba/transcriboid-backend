import pickle


# Saves the markov chain object
def save(mkv):
    pickle.dump(mkv, open(constants.matrix_path, "wb"))


# Loads the markov chain object
def load():
    return pickle.load(open(constants.matrix_path, "rb"))

def main():
    print("Markov chain has been updated at " + constants.save_matrix_path)
    save(mark)
