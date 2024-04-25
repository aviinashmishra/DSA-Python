# 5. In class CDLL, define a method insert_at_last() to insert an element at the end of the list.

class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
class CDLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            n.prev=n
        else:
            n.next=self.satrt
            n.prev=self.start.prev
            self.start.prev.next=n
            self.start.prev=n
        self.start=n
    def insert_at_last(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            n.prev=n
            self.start=n
        else:
            n.next=self.start
            n.prev=self.start.prev
            self.start.prev=n
            n.prev.next=n


