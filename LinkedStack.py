# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 18:33:03 2022

@author: HP
"""

class LinkedStack:
    """LIFO stack implementing
    a single storage list for list"""
    
    class _Node:
        __slots__ = 'element', '_next'
        
        def __init__ (self, element, next):
            self._element = element
            self._next = next
            
    def __init__(self):
        """Create an empty stack."""
        self._head = None  # reference to the head node
        self._size = 0  # number of stack elements
        
    def __len__(self):
        """Return the number of elements in the stack"""
        return self._size
    
    def is_empty(self):
        """Return True if the stack is empty."""
        return self._size == 0
    
    def push(self, e):
        """Add element e to the top of the stack."""
        self._head = self._Node(e, self._head)
        self._size += 1
        
    def top(self):
        """Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element
    
    def pop(self):
        """Remove and return the element form the top of the stack
        Raise Empty exception if the stack is empty""" 
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next 
        self._size -= 1
        return answer

    
    
        
    