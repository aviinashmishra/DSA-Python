# 1. Define a class Stack to implement stack data structure by extending list class.



class Stack(list):
    def is_empty(self):
        return len(self)==0
