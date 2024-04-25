# 1. Define a class Deque to implement deque data structure using list. Define _init__() method to create an empty list object as instance object member of Deque.
# 2. Define a method is_empty() to check if the deque is empty in Deque class.
# 3. In Deque class, define insert_front() method to add data at the front end of the deque.
# 4. In Deque class, define insert_rear() method to add data at the rear end of the deque.
# 5. In Deque class, define delete_front() method to remove front element from the deque.
# 6. In Deque class, define delete_rear() method to remove rear element from the deque.
# 7. In Deque class, define get_front() method to return front element of the deque.
# 8. In Deque class, define get_rear() method to return rear element of the deque.
# 9. In Deque class, define size() method to return size of the deque that is number of items present in the deque.





class Deque:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def insert_front(self,data):
        self.items.insert(0,data)
    def insert_rear(self,data):
        self.items.append(data)
    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deque is Empty")
        else:
            self.items.pop(0)
    def delete_rear(self):
        if self.is_empty():
            raise IndexError("Deque is Empty")
        else:
            self.items.pop()
    def get_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            return self.items[0]
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        else:
            return self.items[-1]
    def size(self):
        return len(self.items)


d1=Deque()
d1.insert_front(10)
d1.insert_front(20)
d1.insert_rear(30)
d1.insert_rear(40)
print(d1.get_front(), d1.get_rear())
