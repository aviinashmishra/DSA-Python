# 5. In class DLL, define a method insert_at_last() to insert an element at the end of the list.

class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

class DLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,data):
        n=Node(None,data,self.start)
        if not self.is_empty():
            self.start.prev=n
        self.start=n
    def insert_at_last(self,data):
        temp=self.start
        if self.start!=None:
            while temp.next!=None:
                temp=temp.next
        
        n=Node(temp,data,None)
        if temp==None:
            self.start=n
        else:
            temp.next=n