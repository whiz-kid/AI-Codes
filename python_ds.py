from collections import deque

#Queue Implementation
class queue(deque):
	enqueue=deque.append
	dequeue=deque.popleft
	def front(self):
		return self[-1]
	def size(self):
		return len(self)

# Stack Implementation
class stack(deque):
	push=deque.append
	pop=deque.pop
	def is_empty(self):
		return not self


# Hachmap Implementation
table=[[] for x in range(10)]

def hashFunction(x):
	return x%10

def insert(table,input,value):
	table[hashFunction(input)].append((input,value))

x=list(map(str,raw_input().strip().split()))
print(x)