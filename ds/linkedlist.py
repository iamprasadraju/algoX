import random

arr = [random.randint(1, 10) for _ in range(5)]
print(arr)


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self, arr=None):
		self.head = None
		self.arr = arr
		self.len = 0
		
		if arr:
			self.build(arr)
		
	def build(self, arr):
		if not arr: return None
		self.head = Node(arr[0])
		self.len = 1
		tail = self.head
		
		for element in arr[1:]:
			tail.next = Node(element)
			tail = tail.next
			self.len += 1
		 
	def postappend(self, data):
		pass
		
	def preappend(slef, data):
		pass
	
	def __iter__(self):
		current = self.head
		while current:
			yield current.data
			current = current.next
			
	def __repr__(self):
		if not self.head:
			return 'LinkedList()'
		result = []
		current = self.head
		while current:
			result.append(str(current.data))
			current = current.next
		return f"{'->'.join(result)}"
		
	def __len__(self):
		return self.len
		
	def remove(self, idx):
		pass
		
	def insert(self, idx):
		pass
		


ll = LinkedList(arr)
print(ll)

print(len(ll))
for l in ll:
	print(l)