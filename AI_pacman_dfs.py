# python 2.7

# Input section
px,py = map(int,raw_input().strip().split())
fx,fy = map(int,raw_input().strip().split())
rows,columns = map(int,raw_input().strip().split())

matrix = []
for r in range(rows):
	x = map(str,raw_input().strip().split())
	matrix.append(x)

row_size = len(matrix)
column_size = len(matrix[0])


# Main code
x = [-1,0,0,1]
y = [0,-1,1,0]

def is_feasible(current_row,current_column,current_matrix):
	if ( (current_column >=0) and (current_column < columns) and (current_row < rows) \
		 and (current_row >=0) and (current_matrix[current_row][current_column] != '%')) :
		return 1
	else:
		return 0

stack=[]
current_matrix = matrix
flag=1

while flag:
# for epoch in range(3):

	# print(current_matrix)

	for i in range(row_size):
		for j in range(column_size):
			if(current_matrix[i][j] == 'P'):
				current_pac_x = i
				current_pac_y = j
				break

	print(current_pac_x,current_pac_y)

	if( (current_pac_x == fx) and (current_pac_y == fy)):
		print(" Pacman Got the food" ,(current_pac_x,current_pac_y))
		break
	

	for i in range(4):
		new_pac_x = current_pac_x+x[i]
		new_pac_y = current_pac_y+y[i]
		if(is_feasible(new_pac_x,new_pac_y,current_matrix)):
			# print(new_pac_x,new_pac_y)
			new_matrix = [[0 for _ in range(column_size)] for _ in range(row_size)] 
			for m in range(row_size):
				for n in range(column_size):
					new_matrix[m][n] = current_matrix[m][n]


			new_matrix[current_pac_x][current_pac_y],new_matrix[new_pac_x][new_pac_y] = \
			new_matrix[new_pac_x][new_pac_y],new_matrix[current_pac_x][current_pac_y]
			# swap(new_matrix[current_pac_x][current_pac_y],new_matrix[new_pac_x][new_pac_y])
			stack.append(new_matrix)

	# for size in range(len(stack)):
	# 	print(stack.pop())
	if(len(stack) != 0):
		current_matrix = stack.pop()
	else:
		print("Pacman can't get the food")
		flag=0





