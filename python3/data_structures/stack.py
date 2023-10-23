from .node import Node

# not tested

class Stack:
    def __init__(self):
        self.top = None

    def _is_empty(self):
        return (self.top == None)

    def peek(self):
        if !self._is_empty():
            return self.top

    def push(self, val):
        node = Node(val)

        if self._is_empty():
            self.top = Node(val)
        else:
            node.next = self.top
            self.top = node

    def pop(self):
        if self._is_empty():
            return
        else:
            val = self.top.val
            self.top = self.top.next

            return val

