
rows=[0,-1,-1,-1,0,1,1,1]
columns=[-1,-1,0,1,1,1,0,-1]

def is_safe(row,col):
	if((row>=0) and (row<m) and (col>=0) and (col<n)):
		return True
	return False


def solve(row,col,status):

	for rn in roll_numbers:
		if(not status[rn]):
			flag=1
			for i in range(8):
				new_row=row+rows[i]
				new_col = col+columns[i]
				if(is_safe(new_row,new_col) and sit_arr[new_row][new_col] !=0):
					if(rn not in student[sit_arr[new_row][new_col]]):
						# print(rn,sit_arr[new_row][new_col])
						flag = 0
						break
			if(flag):
				sit_arr[row][col]=rn
				status[rn]=1
				print(sit_arr)
				# print(row,col)
				if(col==n-1 and row<m-1):
					ans = solve(row+1,0,status)
				elif(col<n-1):
					ans = solve(row,col+1,status)
				else:
					return True

				if(ans):
					return True
				else:
					sit_arr[row][col]=0
					status[rn]=0

	return False

t=int(input())
m,n=map(int,raw_input().strip().split())
student={}
for i in range(m*n):
	info=list(map(int,raw_input().strip().split()))
	if info[0] not in student:
		student[info[0]]=[]
	for j in range(2,len(info)):
		student[info[0]].append(info[j])
# print(student)

roll_numbers=student.keys()
status={}
for rn in roll_numbers:
	status[rn]=0

# print(status)

sit_arr = [[0 for i in range(n)] for j in range(m)]
print(sit_arr)
ans = solve(0,0,status)
if(ans):
	print(sit_arr)
else:
	print("No Solution Possible")

