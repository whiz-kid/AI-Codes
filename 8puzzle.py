# 8 Puzzle problem -->  Using DFS

columns=[-1,0,1,0]
rows=[0,-1,0,1]


def is_feasible(new_row,new_column):
	if new_row>=0 and new_row <3 and new_column>=0 and new_column <3:
		return True
	else:
		return False

def swap(board,i,j,k,l):
	temp=board[i][j]
	board[i][j]=board[k][l]
	board[k][l]=temp

	return board

def count_wrong_placed(board,goal):

	count=0
	for i in range(3):
		for j in range(3):
			if(board[i][j] != goal[i][j]):
				count += 1
	return count

class Node:

	def __init__(self,data=None,parent=None,level=0,hue=0):
		self.data=data
		self.parent=parent
		self.child=[]
		self.level=level
		self.hue = hue

	def add_child(self,child):
		self.child.append(child)
		child.parent=self

	def get_children(self):
		return self.child

	def get_parent(self):
		return self.parent	


board=[ [4,-1,1],
		[7,5,3],
		[8,2,6] ]
goal_state= [[1,2,3],[4,5,6],[7,8,-1]]



root=Node(board,None,0)
current_node = root
total_epoch=100
priority_queue = []
priority_queue.append((0,current_node))
epoch=0
visited=[]
# for epoch in range(total_epoch):
while priority_queue:

	_,current_node = priority_queue.pop(0)  
	current_board = current_node.data
	print("State of board at epoch " + str(epoch),current_board)
	current_empty=[0,0]
	for i in range(3):
		for j in range(3):
			if(current_board[i][j]==-1):
				current_empty=[i,j]
				break
	current_row=current_empty[0]
	current_column=current_empty[1]
	if(current_board == goal_state):
		print("Got right config after " + str(epoch) + " epoch -> " ,current_node.data)
		break

	for i in range(4):
		new_row=current_row+rows[i]
		new_column=current_column+columns[i]

		if((new_row,new_column) not in visited):
			if(is_feasible(new_row,new_column)):
				visited.append((new_row,new_column))
				new_current_board=[[0,0,0],[0,0,0],[0,0,0]]
				for m in range(3):
					for n in range(3):
						new_current_board[m][n]=current_board[m][n]
				new_board = swap(new_current_board,current_row,current_column,new_row,new_column)
				new_level = current_node.level+1
				new_hue = count_wrong_placed(new_board,goal_state)
				new_node = Node(new_board,current_node,new_level,new_level)
				current_node.child.append(new_node)
				priority_queue.append((new_hue+new_level,new_node))

	priority_queue.sort()
	epoch+=1

	# total_wrong_count=10
	# initial_level=total_epoch

	# for i in range(len(current_node.child)):
	# 	new_node = current_node.child[i]
	# 	wrong_count = count_wrong_placed(new_node.data,goal_state)
	# 	if(wrong_count+new_node.level < total_wrong_count + initial_level):
	# 	# if(wrong_count < total_wrong_count):
	# 		new_current_node = new_node
	# 		total_wrong_count = wrong_count
	# 		initial_level = new_node.level



















