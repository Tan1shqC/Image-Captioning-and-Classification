class _DoubleLinkedBase:
	""" A base class providing a doubly linked list representation."""

	class _Node:
		""" Lightweight, nonpublic class for storing a doubly linked node"""
		__slots__ = '_element', '_prev', '_next' # streamline memory

		def __init__(self, element, prev, next): # initialize node's fields
			self._element = element
			self._prev = prev
			self._next = next
            
	def __init__(self):
		"""Create an empty list"""
		self._header = self._Node(None, None, None)
		self._trailer = self._Node(None, None, None)
		self._header._next = self._trailer
		self._trailer._prev = self._header
		self._size = 0 # number of elements

	def __len__(self):
		node = self._header._next
		len = 0
		while node != self._trailer :
			len += 1
			node = node._next
		return len

	def is_empty(self):
		if self._header._next == self._trailer :
			return True
		else :
			return False

	def _insert_between(self, e, predecessor, successor):
		"""Add element e between two existing nodes and return new node"""
		if predecessor._next == successor:
			newest = self._Node(e, predecessor, successor)
			predecessor._next = newest
			successor._prev = newest

	def _delete_node(self, node):
		prev = node._prev
		next = node._next
		prev._next = next._prev
		del node

DoubleLinkedBase = _DoubleLinkedBase()
DoubleLinkedBase._insert_between(12, DoubleLinkedBase._header, DoubleLinkedBase._header._next)
DoubleLinkedBase._insert_between(11, DoubleLinkedBase._header, DoubleLinkedBase._header._next)
DoubleLinkedBase._insert_between(10, DoubleLinkedBase._header, DoubleLinkedBase._header._next)
print(DoubleLinkedBase.__len__())
