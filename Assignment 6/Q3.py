# 3. Define a method is_empty() to check if the linked list is empty in CDLL class.



class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
class CDLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        self.start=None
    