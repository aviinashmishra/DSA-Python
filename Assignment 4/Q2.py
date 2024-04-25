# 2. Define a class DLL to implement Doubly Linked List with_init_() method to create and initialise start reference variable.


class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

class DLL:
    def __init__(self,start=None):
        self.start=start