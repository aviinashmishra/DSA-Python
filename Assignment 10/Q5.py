# 5. In Stack class, define pop() method to remove top element from the stack.

from Assignment3 import*

class Stack:
    def __init__(self):
        self.mylist=SLL()
        self.item_count=0
    def is_empty(self):
        return self.mylist.is_empty()
    def push(self,data):
        self.mylist.insert_at_start(data)
        self.item_count+=1
    def pop(self):
        if not self.is_empty():
            self.mylist.delete_first()
            self.item_count-=1
    