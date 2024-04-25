# 4. In Stack class, define push() method to add data onto the stack

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
        
