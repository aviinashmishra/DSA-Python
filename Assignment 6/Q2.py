# 2. Define a class CDLL to implement Circular Doubly Linked List with _init__() method to create and initialise last reference variable.


class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
class CDLL:
    def __init__(self,start=None):
        self.start=start