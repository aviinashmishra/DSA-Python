# 1. Define a class Stack to implement stack data structure using singly linked list concept. Define _init_() method to initialise start reference variable and item_count variable to keep track of number of elements in the stack.


class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class stack:
    def __init__(self):
        self.start=None
        self.item_count=0
    
    