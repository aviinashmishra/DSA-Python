# 1. Define a class Queue to implement queue data structure using singly linked list concept. Define _init_() method to initialise front and rear reference variable; and item_count variable to keep track of number of elements in the queue.
# 2. Define a method is_empty() to check if the queue is empty in Queue class.
# 3. In Queue class, define enqueue() method to add data into the queue.
# 4. In Queue class, define dequeue() method to remove front element from the queue.
# 5. In Queue class, define get_front() method to return front element of the queue.
# 6. In Queue class, define get_rear() method to return rear element of the queue.
# 7. In Queue class, define size() method to return size of the queue that is number of items present in the queue.


class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0
    def is_empty(self):
        return self.front==None
    def enqueue(self,data):
        n=Node(data)
        if self.is_empty():
            self.front=n
        else:
            self.rear.next=n
        self.rear=n
        self.item_count+=1
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Empty Queue")
        elif self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next
        self.item_count-=1
    def get_front(self):
        if self.is_empty():
            raise IndexError("Empty Queue")
        else:
            return self.front.item
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Empty Queue")
        else:
            return self.rear.item
    def size(self):
        return self.item_count


q1=Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
print(q1.get_front(),q1.get_rear())
q1.dequeue()
print(q1.get_front(),q1.get_rear())




