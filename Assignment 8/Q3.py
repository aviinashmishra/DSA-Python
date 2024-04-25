# 3. In Stack class, define push() method to add data onto the stack.


class Stack(list):
    def is_empty(self):
        return len(self)==0
    def push(self,data):
        self.append(data)
