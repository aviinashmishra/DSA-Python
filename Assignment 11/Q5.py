# 5. In Stack class, define pop() method to remove top element from the stack.

from Assignment3 import*
class Stack:
    def is_empty(self):
        return super().is_empty()
    def push(self,data):
        self.insert_at_start(data)
    def pop(self):
        if not self.is_empty():
            self.delete_first()