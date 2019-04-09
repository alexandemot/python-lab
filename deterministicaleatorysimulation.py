
import random as rand

class Simulator:

	def runsimulation():
		if ((rand.randint(0, 100) >= 80)):
			response = True
		else:
			response = False
			
		return response