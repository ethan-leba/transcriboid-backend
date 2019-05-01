import random

def weighted_random(weights):
	tally = random.random()
	for i, wt in enumerate(weights):
		if tally <= wt:
			return i
		else:
			tally -= wt