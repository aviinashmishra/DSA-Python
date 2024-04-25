# 3. In Stack class, define push() method to add data onto the stack.


class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class stack:
    def __init__(self):
        self.start=None
        self.item_count=0
    def is_empty(self):
        return self.start==None
    def push(self,data):
        n=Node(data,self.start)
        self.start=n
        self.item_count+=1

