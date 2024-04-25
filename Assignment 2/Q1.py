# 1. Define a python class Person with instance object variables name and age. Set Instance object variables in_init_() method. Also define show() method to display name and age of a person.
class Person:
    def __init__(self,name : str,age : int):
        self.name = name
        self.age = age
    def show(self):
        print(f"Name : {self.name}\nAge : {self.age}")

Person1 = Person("Pandit",19)
Person1.show()