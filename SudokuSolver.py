import random

filename = "puzzle.txt"
with open(filename) as f:
    mylist = f.read().splitlines()

sudoku = []
for i in range(len(mylist)):
	row = mylist.pop(0)
	row = list(map(int,row.strip().split()))
	sudoku.append(row)

# print(sudoku)
total_rows = len(sudoku)
total_columns = len(sudoku[0])

temp = [[False for j in range(total_columns)] for i in range(total_rows)]
for i in range(total_rows):
	for j in range(total_columns):
		if(sudoku[i][j] == 0):
			temp[i][j] = True

cross_over_rate = 0.5
mutaion_rate = 0.1
total_population = 100
population = []

def copy(new_sudoku):
	newList = [[new_sudoku[i][j] for j in range(total_columns)] for i in range(total_rows)]
	return newList

def fit_function(new_sudoku):
	y_real = 45
	loss = 0
	for epoch in range(total_rows):
		y_pred = sum(new_sudoku[epoch])
		loss += abs(y_real-y_pred)

	return loss

def cross_over():
	cross_over_size = len(population)/2
	for epoch in range(1):
		parent1 = population.pop(0)
		parent2 = population.pop(0)
		# Crossover Function
		child1 = copy(sudoku)
		child2 = copy(sudoku)
		for epoch_x in range(total_rows):
			for epoch_y in range(total_columns):
				if(temp[epoch_x][epoch_y]):
					# First child
					temp11 = (parent1[1][epoch_x][epoch_y] & 12)
					temp12 = (parent2[1][epoch_x][epoch_y] & 3)
					child1[epoch_x][epoch_y] = (temp11 | temp12)
					# Second child
					temp21 = (parent1[1][epoch_x][epoch_y] & 3)
					temp22 = (parent2[1][epoch_x][epoch_y] & 12)
					child2[epoch_x][epoch_y] = (temp21 | temp22)

					# print(child1[epoch_x][epoch_y],child2[epoch_x][epoch_y])
					# child2[epoch_x][epoch_y] = (parent1[1][epoch_x][epoch_y] or parent2[1][epoch_x][epoch_y])
		loss1 = fit_function(child1)
		loss2 = fit_function(child2)

		population.append((loss1,child1))
		population.append((loss2,child2))
		population.append(parent1)
		population.append(parent2)
		# population.sort()

def mutation():
	mutation_size = int(len(population)*mutaion_rate)
	for epoch in range(mutation_size):
		parent = population.pop()
		child = copy(parent[1])
		# Mutation Function
		while True:
			row_bit_pos = random.randint(0,8)
			column_bit_pos = random.randint(0,8)
			if(temp[row_bit_pos][column_bit_pos]):
				break
		# print(parent[1][row_bit_pos][column_bit_pos])
		child[row_bit_pos][column_bit_pos] = (child[row_bit_pos][column_bit_pos] & 1101)
		loss = fit_function(child)

		population.append((loss,child))

def generate_initial_population():
	for epoch in range(total_population):
		new_sudoku = copy(sudoku)
		for i in range(0,total_rows):
			for j in range(0,total_columns):
				if(temp[i][j]):
					new_sudoku[i][j] = random.randint(1,9)
		loss = fit_function(new_sudoku)
		population.append((loss,new_sudoku))
		population.sort()

def SudokuSolver():

	generate_initial_population()
	flag=1
	# print(population)
	# for _ in range(100):
	while flag :
		for chromosome in population:
			# print(chromosome[0])
			if(chromosome[0] == 0):
				print("Solved")
				flag=0
				break
			# print(chromosome)
		# print(population[0][0])

		for epoch in range(int(len(population)-((len(population)*cross_over_rate)))):
			population.pop()
		# Crossover function
		cross_over()
		# Mutation Function
		mutation()
		# Sort the population to get the the most fittest chromosome
		population.sort()

SudokuSolver()






