# 4. In class SLL, define a method insert_at_start() to insert an element at the starting of the list.

class Node:
    def __init__(self, item=None,next=None):
        self.item=item
        self.next=next
class SLL:
    def __init__(self, start=None):
        self.start=start 

    def is_empty(self):
        return self.start==None
    
    def insert_at_start(self,data):
        n=Node(data,self.start)
        self.start=n