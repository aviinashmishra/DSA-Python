# 4. In Stack class, define push() method to add data onto the stack.

from Assignment3 import*
class Stack:
    def is_empty(self):
        return super().is_empty()
    def push(self,data):
        self.insert_at_start(data)