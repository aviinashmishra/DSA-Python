# 2. Define a method is_empty() to check if the stack is empty in Stack class.

class Stack(list):
    def is_empty(self):
        return len(self)==0