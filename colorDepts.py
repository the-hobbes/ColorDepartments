'''
	Your goal is to color a map of these regions with two requirements: 
	1) make sure that each adjacent department do not share a color, so you can clearly distinguish each 
	department, and 
	2) minimize these numbers of colors.
	
	The input will be a variation of the list of French departments, represented as an adjacency list[5] . This challenge is essentially solving for Graph coloring[6] , where 
	you must print each department's color (a unique integer).

	Input Description:
		On standard console input, you will be given an integer N which represents the following N-lines of an adjacency list. These lines of data will always be in the format 
		of integers A B C D ... where A is the source node / vertex that points to vertices B C D... etc. Remember that this data really means that A is the ID of a department, 
		and B C D ... are the bordering departments.
		Writing up the French department list as an adjacency list is very tedious; feel free to only work on a subset.
	Output Description:
		For each given node (a department), print the unique color identifier after it. A color identifier is unique integer, starting from 0, that represents a unique color. 
		Remember that bordering departments (e.g. adjacent nodes) cannot have the same color index!
'''
import random
DEBUG = True
class District():
	'''
		district class used to encode representations of a set of district and its adjacent neighbors
	'''
	districtId = ''
	neighbors = []
	color = 0

	def __init__(self, districtId, neighbors, color):
		self.districtId = str(districtId)
		self.neighbors = neighbors
		self.color = color

	def getNeighbors(self):
		return neighbors

	def getId(self):
		return districtId

	def getColor(self):
		return color

	def __str__(self):
		stringRepresentation = " Id = %s, Color = %s, Neighbors = [%s] " %( self.districtId, str(self.color), ', '.join(map(str, self.neighbors)) )
		return stringRepresentation

def read_adjlist():
	'''
		function used to read in the input and create an adjacency list from it. 
	'''
	# open the input file and make a dictionary of lists, where the keys are the verticies and the lists are the nodes
	f = open('input.txt')
	n = int(f.readline())
	li = [f.readline().split() for _ in range(n)]
	vers = [sl[0] for sl in li]
	return {sl[0]:[v for v in sl[1:] if v in vers] for sl in li}

# dataInput = read_adjlist()

def initialize_population(adjacencyList):
	'''
		generate a random individual answer for population creation
		you must make many of these to seed an initial population
	'''
	districts = []
	for item in adjacencyList:
		newList = [{adjacencyList[item][x]:random.randrange(0,7)} for x in range(len(adjacencyList[item]))]
		newObj = District(item, newList, random.randrange(0,7))	
		districts.append(newObj)	

	return districts
	

def fitness_function():
	'''
		fitness function to determine fit of individuals in the population
		the best individuals don't have the same color as their adjacent districts according to the criteria, and the best solutions have the fewest colors
	'''
	pass
	

def crossover():
	'''
		crossover method for population
	'''
	pass

def mutation():
	'''
		mutation method for population
	'''
	pass

def run_experiment():
	'''
		run genetic algorithm
	'''
	adjacencyList = read_adjlist()
	population = []
	for i in range(100):
		# generate initial population of 100 randomly colored individuals
		population.append(initialize_population(adjacencyList))
	
	if DEBUG:
		for x in population:
			print x[0], x[1], x[2]

	# generations 
	n = 100
	# crossover rate
	crossoverRate = .5
	# mutation rate 
	mutationRate = .5

	# iterate through n generations, doing the following:
	for x in range(n):
		# evaluate the fitness of every individual in the generation
		# stochastically select the most fit individuals from the generation
		# recombine two fit individual to produce an offspring
		# mutate some of these offspring randomly
		# repeat
		pass

run_experiment()