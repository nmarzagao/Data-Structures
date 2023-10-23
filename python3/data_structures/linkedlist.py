from .node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def _is_empty(self):
        return (self.head == None)
    
    def insert_first(self, val):
        node = Node(val)

        if self._is_empty():
            self.head = Node(val)

        else:
            node.next = self.head
            self.head = node

    def insert_last(self, val):
        node = Node(val)

        if self._is_empty():
            self.head = node 

        else:
            tmp = self.head
            while tmp.next is not None:
                tmp = tmp.next
            
            tmp.next = node
        
    def pop_first(self):
        if self._is_empty():
            return None
        
        else:
            val = self.head.val
            self.head = self.head.next

            return val

    def pop_last(self):
        if self._is_empty():
            return None
            
        elif self.head.next is None:
            val = self.head.val
            self.head = None
            
            return val

        else:
            last = self.head
            prev = None
            while last.next is not None:
                prev = last
                last = last.next
                
            val = last.val
            prev.next = None
            return val