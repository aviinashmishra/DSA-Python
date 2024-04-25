# 1. Define a class Node to describe a node of a doubly linked list.

class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next