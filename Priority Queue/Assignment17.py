# 1. Define a class PriorityQueue to implement priority queue data structure using list. Provide_init_() method to create a list object (initially empty).
# 2. Define a push method in PriorityQueue class to insert new data with given priority.
# 3. Define a pop method in PriorityQueue class, which returns the highest priority data stored in the priority queue data structure. Raise exception if priority queue is empty.
# 4. Define is_empty method in PriorityQueue class to check if the priority queue is empty.
# 5. In class Priority Queue, define a method size to return the number of elements present in the priority queue.



class PriorityQueue:
    def __init__(self):
        self.items=[]
    def push(self,data,priority):
        Index=0
        while Index<len(self.items) and self.items[Index][1]<=priority:
            Index+=1
        self.items.insert(Index,(data,priority))
    def is_empty(self):
        return len(self.items)==0
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is Empty")
        return self.items.pop(0)[0]
    def size(self):
        return len(self.items)
    
p=PriorityQueue()
p.push("avi",4)
p.push("ram",7)
p.push("Ravi",2)
p.push("Anvi",5)
p.push("ashu",8)
p.push("hari",1)

while not p.is_empty():
    print(p.pop())
