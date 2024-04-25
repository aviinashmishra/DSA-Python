# 2. Define a class SLL to implement Singly Linked List with_init_() method to create and initialise start reference variable.


class Node:
    def __init__(self, item=None,next=None):
        self.item=item
        self.next=next
class SLL:
    def __init__(self, start=None):
        self.start=start        