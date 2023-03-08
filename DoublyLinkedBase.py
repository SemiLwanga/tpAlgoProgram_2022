# -*- coding: utf-8 -*-


class _DoublyLinkedBase:
    """A base class providing a doubly linked
    trailerlist representation"""
    
    class _Node:
        """Lightweight, nonpublic class
        for storing doubly linked node """
        __slots__ = 'element', '_prev', '_next'
        
        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next
            
    def __init__(self):
        """Create an empty list"""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0
        
    def __len__(self):
        """Return the number of elements in the list"""
        return self._size
    
    def is_empty(self):
        """Return True if the lis is empty"""
        return self._size == 0
    
    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes
        and return the new node"""
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest
    
    def delete_node(self, node):
        """Delete nosentinel node from
        the list and return its element"""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element 
        node._prev = node._next = node._element = None
        return element
        