# 7. Implement a way to restrict use of insert() method of list class from stack object.



class Stack(list):
    def is_empty(self):
        return len(self)==0
    def push(self,data):
        self.append(data)
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Stack is Empty")
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is Empty")
    def size(self):
        return len(self)
    def insert(self,index,data):
        raise AttributeError("No attribute 'insert' in stack")

s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
print("top value=",s1.peek())