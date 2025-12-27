# Stack (list) 
class Stack:
	def __init__(self, arr=None):
		self._stack = list(arr) if arr else []
		self.len = len(self._stack)
	
	def pop(self):
		if self.is_empty():
			raise IndexError("Stack is empty")
		self.len -= 1
		return self._stack.pop(0)
		
	def push(self, data):
		self._stack.append(data)
		self.len += 1
	
	def peek(self):
		if is_empty():
			return
		return self._stack[0]
		
	def is_empty(self):
		return self.len == 0
		
	def __repr__(self):
		stack_contents = "\n".join(f"[{repr(item)}]" for item in self._stack)
		return "Stack(\n" + stack_contents + "\n)"
		
	def __len__(self):
		return self.len
		
	def __iter__(self):
		if self.is_empty():
			return
		for element in self._stack:
			yield element
		

class Node:  # acts like pointer
	def __init__(self, data):
		self.data = data
		self.next = None


# Stack using Linkedlist	
class LinkedStack:
	def __init__(self, arr=None):
		self.len = 0
		self.head = None
		self.tail = None
		
		if arr:
			self.build(arr)
			
	def build(self, arr): # O(n)
		if not arr: return None
		self.head = self.tail = Node(arr[0])
		self.len = 1
		
		for element in arr[1:]:
			new_node = Node(element)
			self.tail.next = new_node
			self.tail = new_node
			self.len += 1
	
	def pop(self): # O(1)
		if self.head is None:
			return
		
		current = self.head
		self.head = current.next
		self.len -= 1
		return current.data
		
			
	def push(self, data): # O(1)
		if self.head is None:
			return
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node
		self.len += 1
		
	def peek(self): # O(1)
		if self.head is None:
			return 
		top = self.head
		return top.data
	
	def is_empty(self):
		return self.len == 0
		
		
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