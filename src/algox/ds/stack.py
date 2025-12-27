
# Stack (list) 
class Stack:
	def __init__(self, arr=None):
		self._stack = list(arr) if arr else []
		self.len = len(self._stack)
	
	def pop(self):
		if self.len == 0:
			raise IndexError("Stack is empty")
		self.len -= 1
		return self._stack.pop(0)
		
	def push(self, data):
		self._stack.append(data)
		self.len += 1
		
	def __repr__(self):
		return f"Stack({self._stack})"
		
	def __len__(self):
		return self.len
		
	def __iter__(self):
		pass
		

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		
class LinkedStack:
	def __init__(self, arr=None):
		self.len = 0
		self.head = None
		
		if arr:
			self.build(arr)
			
	def build(self, arr):
		if not arr: return None
		self.head = Node(arr[0])
		self.len = 1
		current = self.head
		
		for element in arr[1:]:
			new_node = Node(element)
			current.next = new_node
			current = new_node
			self.len += 1
	
	def pop(self):
		if self.head is None:
			return
		
		current = self.head
		self.head = current.next
		self.len -= 1
		return current.data
		
			
	def push(self, data):
		if self.head is None:
			return
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node
		self.len += 1
		
	def __repr__(self):
		if self.head is None:
			return "LinkedStack()"
		
		str = ""
		current = self.head
		while current:
			str += f"[{current.data}]\n"
			current = current.next
		return "Stack(\n" + str + ")"
		
	def __iter__(self):
		if self.head is None:
			return None
			
		current = self.head
		
		while current:
			data = current.data
			current = current.next
			yield data
		
	def __len__(self):
		return self.len