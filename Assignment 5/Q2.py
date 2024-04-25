# 2. Define a class CLL to implement Circular Linked List with __init_() method to create and initialise last reference variable.



class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class CLL:
    def __init__(self,last=None):
        self.last=last