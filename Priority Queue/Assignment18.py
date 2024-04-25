# 1. Define a Node class with instance member variables item, priority and next.
# 2. Define a class PriorityQueue to implement priority queue data structure using singly linked list. Provide _init_() method to create a start reference variable (initially containing None) and item_count variable (initially 0).
# 3. Define a push method in PriorityQueue class to insert new data with given priority.
# 4. Define a pop method in PriorityQueue class, which returns the highest priority data stored in the priority queue data structure. Raise exception if priority queue is empty.
# 5. Define is_empty method in PriorityQueue class to check if the priority queue is empty.
# 6. In class PriorityQueue, define a method size to return the number of elements present in the priority queue.



class Node:
    def __init__(self,item=None,priority=None,next=None):
        self.item=item
        self.priority=priority
        self.next=next
class PriorityQueue:
    def __init__(self):
        self.start=None
        self.item_count=0
    def push(self,data,priority):
        n=Node(data,priority)
        if not self.start or priority<self.start.priority:
            n.next=self.start
            self.start=n
        else:
            temp=self.start
            while temp.next and temp.next.priority<=priority:
                temp=temp.next
            n.next=temp.next
            temp.next=n
            self.item_count+=1
    def is_empty(self):
        return self.start==None
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is Empty")
        data=self.start.item
        self.start=self.start.next
        self.item_count-=1
        return data
    def size(self):
        return self.item_count
    
p=PriorityQueue()
p.push("avi",4)
p.push("ram",7)
p.push("Ravi",2)
p.push("Anvi",5)
p.push("ashu",8)
p.push("hari",1)

while not p.is_empty():
    print(p.pop())
