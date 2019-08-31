class Node:
	"""
	Node - main element of the DoublyLinkedList,
		every Node has following data:
			- data, could be anything;
			- link to the next node object;
			- link to the previous node object. 
	"""
	
	def __init__(self, data):
		self.previous = None
		self.next = None
		self.data = data
	
	def __del__(self):
		pass

	def __repr__(self):
		next_node_data = self.next.data if self.next else None
		prev_node_data = self.previous.data if self.previous else None
		return str(f'Data -> {self.data}; Previous Node -> {prev_node_data}; Next Node -> {next_node_data}')


class DoublyLinkedList:
	"""
	Doubly linked List class, with three methods:
		add_node - to add node from start or end position;
		rmv_node - to remove node from start or end of list;
		get_node - returns following info for node mentioned by position:
					data, next node, previous node.
	"""
						
	def __init__(self):
		"""
		creates a doubly linked list
		"""
		self.tail = None
		self.head = None
		self.size = 0
		
	def add_node(self, data, position='start'):
		"""
		adds node to the list,
		to the start or the end of the list
		"""
		current_node = Node(data)
		if self.size == 0:
			self.tail = current_node
			self.head = current_node
			self.size += 1
		else:
			if position == 'end':
				current_node.previous = self.tail
				self.tail.next = current_node
				self.tail = current_node
			else:
				current_node.next = self.head
				self.head.previous = current_node
				self.head = current_node
			self.size += 1

	def rmv_node(self, position='start'):
		"""
		removes node from the list,
		from the start or the end of the list
		returns deleted node's data
		"""
		data = None
		if position == 'end':
			current_node = self.tail
			current_node.previous.next = None
			self.tail = current_node.previous
			data = current_node.data
			del current_node
		else:
			current_node = self.head
			current_node.next.previous = None
			self.head = current_node.next
			data = current_node.data
			del current_node
		self.size -= 1
		return data

	def get_node(self, position='start'):
		"""
		gets node info by given position,
		positions could be:
			'start', 'end', any number in range of size of the list
			(position counted starting from 0)
		information to receive:
			data, next node data, previous node data
		"""
		if position == 'start':
			return self.head.__repr__()
		elif position == 'end':
			return self.tail.__repr__()
		else:
			if position in range(self.size):
				the_middle = (self.size-1)//2
				if position <= the_middle:
					numb = 0
					current_node = self.head
					while numb < position:
						current_node = current_node.next
						numb += 1
				else:
					numb = self.size - 1
					current_node = self.tail
					while numb > position:
						current_node = current_node.previous
						numb -= 1
				return current_node.__repr__()
			else:
				return 'Please enter correct position!'
