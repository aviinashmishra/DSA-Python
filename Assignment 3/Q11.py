# 11. In class SLL, define a method delete_last() to delete last element from the list.

class Node:
    def __init__(self, item=None,next=None):
        self.item=item
        self.next=next
class SLL:
    def __init__(self, start=None):
        self.start=start 

    def is_empty(self):
        return self.start==None
    
    def insert_at_start(self,data):
        n=Node(data,self.start)
        self.start=n
    
    def insert_at_last(self,data):
        n=Node(data)
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
        else:
            self.start=n
    
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next
    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=None




# Drive code
mylist=SLL()
mylist.insert_at_start(20)
mylist.insert_at_start(10)
mylist.insert_at_last(30)
mylist.insert_at_last(240)
mylist.insert_at_last(205)
mylist.insert_after(mylist.search(20),25)
mylist.print_list()