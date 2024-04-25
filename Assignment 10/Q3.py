# 3. Define a method is_empty() to check if the stack is empty in Stack class.


from Assignment3 import*

class Stack:
    def __init__(self):
        self.mylist=SLL()
    def is_empty(self):
        return self.mylist.is_empty()
