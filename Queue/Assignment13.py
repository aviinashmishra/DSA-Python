# 1. Define a class Queue to implement queue data structure using list. Define _init__() method to create an empty list object as instance object member of Queue.
# 2. Define a method is_empty() to check if the queue is empty in Queue class.
# 3. In Queue class, define enqueue() method to add data at the rear end of the queue.
# 4. In Queue class, define dequeue() method to remove front element from the queue.
# 5. In Queue class, define get_front() method to return front element of the queue.
# 6. In Queue class, define get_rear() method to return rear element of the queue.
# 7. In Queue class, define size() method to return size of the queue that is number of items present in the queue.



class Queue:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def enqueue(self,data):
        self.items.append(data)
    def dequeue(self):
        if not self.is_empty():
            self.items.pop(0)
        else:
            raise IndexError("Queue Underflow")
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue Underflow")
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Queue Underflow")
    def size(self):
        return len(self.items)
    

q1=Queue()
try:
    print(q1.get_front())
except IndexError as e:
    print(e.args[0])

q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
q1.enqueue(60)
print("front=",q1.get_front(),"Rear=",q1.get_rear())
try:
    q1.dequeue()
    print("Queue has now",q1.size(),"elements")
except IndexError as e:
    print(e.args[0])



