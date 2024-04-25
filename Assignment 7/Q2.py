# 2. Define a method is_empty() to check if the stack is empty in Stack class



class stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0