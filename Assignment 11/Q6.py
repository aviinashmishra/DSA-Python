# 6. In Stack class, define peek() method to return top element on the stack.



from Assignment3 import*
class Stack:
    def is_empty(self):
        return super().is_empty()
    def push(self,data):
        self.insert_at_start(data)
    def pop(self):
        if not self.is_empty():
            self.delete_first()
        else:
            raise IndexError("Stack Underflow")
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("Stack Underflow")