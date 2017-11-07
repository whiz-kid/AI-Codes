# python 2.7

# Input Section
px,py = map(int,raw_input().strip().split())
fx,fy = map(int,raw_input().strip().split())
rows,columns = map(int,raw_input().strip().split())

matrix = []
for r in range(rows):
	x = map(str,raw_input().strip())
	matrix.append(x)

row_size = len(matrix)
column_size = len(matrix[0])


# Main Code
x = [-1,0,0,1]
y = [0,-1,1,0]

def is_feasible(current_row,current_column,current_matrix):
	if ( (current_column >=0) and (current_column < columns) and (current_row < rows) \
		 and (current_row >=0) and (current_matrix[current_row][current_column] != '%')) :
		return 1
	else:
		return 0

def find_hue(current_pac_x,current_pac_y):
	return (abs(fx-current_pac_x) + abs(fy-current_pac_y))


class Node:

	def __init__(self,data,level=0,hue=0):
		self.data = data
		self.child = []
		self.level = level
		self.hue = hue


current_hue = find_hue(px,py)
root = Node(matrix,0,current_hue)
current_node = root
# stack=[]
# stack.append(root)

# while(len(stack) != 0 ):
priority_queue = []
priority_queue.append((0,current_node))
epoch=0
# while True:
# for epoch in range(100):
visited=[]
while priority_queue:

	# current_node = stack.pop()
	_,current_node = priority_queue.pop(0)
	current_matrix = current_node.data
	current_level = current_node.level
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
		if((new_pac_x,new_pac_y) not in visited):
			if(is_feasible(new_pac_x,new_pac_y,current_matrix)):
				visited.append((new_pac_x,new_pac_y))
				# print(new_pac_x,new_pac_y)
				new_matrix = [[0 for _ in range(column_size)] for _ in range(row_size)] 
				for m in range(row_size):
					for n in range(column_size):
						new_matrix[m][n] = current_matrix[m][n]


				new_matrix[current_pac_x][current_pac_y],new_matrix[new_pac_x][new_pac_y] = \
				new_matrix[new_pac_x][new_pac_y],new_matrix[current_pac_x][current_pac_y]

				new_level = current_level + 1
				new_hue = find_hue(new_pac_x,new_pac_y)
				new_node = Node(new_matrix,new_level,new_hue)
				current_node.child.append(new_node)
				priority_queue.append((new_hue+new_level,new_node))

	priority_queue.sort()
	epoch+=1

print(epoch)

	# for i in range(len(priority_queue)):
	# 	_,node = priority_queue.pop()
	# 	print(node.hue)
	# optimum = 1000
	# for i in range(len(current_node.child)):
	# 	node = current_node.child[i]
	# 	hue = current_node.hue
	# 	level = current_node.level

	# 	if(level+hue < optimum):
	# 		new_node = node
	# 		optimum = level+hue



