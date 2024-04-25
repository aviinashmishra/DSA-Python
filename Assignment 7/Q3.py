# 3. In Stack class, define push() method to add data onto the stack.



class stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def push(self,data):
        self.items.append(data)