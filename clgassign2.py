print("************************************QUESTION 1***************************************")
#  Implement  a  class  called  Car  with  attributes  such  as  make,  model,  year,  and 
# mileage.  Create  instances  of  the  Car  class  and  demonstrate  accessing  and 
# modifying their attributes. 


class Car:
  def __init__(self, maker, model, year, mileage=0):
    self.maker = maker
    self.model = model
    self.year = year
    self.mileage = mileage

  def car_details(self):
    names = f"{self.year} {self.maker} {self.model}"
    return names.title()

car1 = Car("Hondaa", "Hundai", 2023, 55000)
car2 = Car("Maruti", "Maruti Suzuki", 2024, 90000)

print(f"Car 2: {car2.car_details()}")
print(f"Car 2 mileage: {car2.mileage} miles")

car1.mileage += 6000 
print(f"Car 1 updated mileage: {car1.mileage} miles")

print("")
print("")

print("**********************************QUESTION 2*****************************************")
# Create  a  base  class  called  Shape  with  methods  for  calculating  area  and 
# perimeter.  Implement  subclasses  such  as  Rectangle,  Circle,  and  Triangle 
# inherited  from  Shape  and  override  the  area  and  perimeter  methods  with 
# appropriate calculations for each shape. 


class Shape:
  def __init__(self):
    pass
  def area_calculation(self):
    raise NotImplementedError("Area is not implemented for the base Shape class")

  def perimeter_calculation(self):
    raise NotImplementedError("Perimeter is not implemented for the base Shape class")

class Rectangle(Shape):
  def __init__(self, length, width):
    super().__init__()
    self.length = length
    self.width = width

  def area_calculation(self):
    return self.length * self.width

  def perimeter_calculaton(self):
    return 2 * (self.length + self.width)
  
class Circle(Shape):
  def __init__(self, radius):
    super().__init__()
    self.radius = radius

  def area_calculation(self):
    import math
    return math.pi * self.radius**2

  def perimeter_calculaton(self):
    import math
    return 2 * math.pi * self.radius

class Triangle(Shape):
  def __init__(self, base, height, side1, side2=None):
    super().__init__()
    self.base = base
    self.height = height
    self.side1 = side1
    self.side2 = side2 or side1  
    if any(a + b <= c for a, b, c in [(self.base, self.height, self.side1), (self.base, self.side1, self.side2), (self.height, self.side1, self.side2)]):
      raise ValueError("Invalid triangle side length")

  def area_calculation(self):
    return 0.5 * self.base * self.height

  def perimeter_calculation(self):
    return self.side1 + self.side2 + self.base

#Driver code
rect = Rectangle(10, 7)
print(f"Area of Rectriangle: {rect.area_calculation()}") 
print(f"Perimeter of Rectriangle: {rect.perimeter_calculaton()}") 
circle = Circle(7)
print(f"Area of Circle: {circle.area_calculation()}") 
print(f"Perimeter of Circle: {circle.perimeter_calculaton()}")  
triangle = Triangle(5, 6, 8)
print(f"Area of Triangle: {triangle.area_calculation()}")
print(f"Perimeter of Triangle: {triangle.perimeter_calculation()}")


print("")
print("")


print("************************************QUESTION 3****************************************")

#  Write a function to reverse a linked list. (Take any 5 integers in a linked list) 





class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def reverse_L_L_itretive(header):
  prev = None
  temp = header
  while temp:
    next_node = temp.next
    temp.next = prev
    prev = temp
    temp = next_node
  return prev

def reverse_L_L_recursive(header):
  if not header:
    raise ValueError("Cannot reverse linked list is Empty")
  if not header.next:
    return header

  new_header = reverse_L_L_recursive(header.next)
  header.next.next = header
  header.next = None
  return new_header

header = Node(1)
header.next = Node(2)
header.next.next = Node(3)
header.next.next.next = Node(4)
header.next.next.next.next = Node(5)

reversed_header_iterative = reverse_L_L_itretive(header)

reversed_header_recursive = reverse_L_L_recursive(header)  

def print_LL(header):
  while header:
    print(header.data, end=" -> ")
    header = header.next
  print("None")

print("Original linked list:")
print_LL(header)

print("Linked List reversed iteratively:")
print_LL(reversed_header_iterative)

print("Linked List reversed recursively:")
print_LL(reversed_header_recursive)



print("")
print("")

print("*************************************QUESTION 4*************************************")


#Implement a stack data structure using queues. Try to implement both push and pop operations efficiently.


from collections import deque

class Stack:
    def __init__(self):
        self.q11 = deque()
        self.q12 = deque()

    def push(self, value):
        self.q11.append(value)

    def pop(self):
        while len(self.q11) > 1:
            self.q12.append(self.q11.popleft())
        top_element = self.q11.popleft()
        self.q11, self.q12 = self.q12, self.q11
        return top_element
    def top_element(self):
        while len(self.q11) > 1:
            self.q12.append(self.q11.popleft())        
        top_element = self.q11[0]
        self.q12.append(self.q11.popleft())
        self.q11, self.q12 = self.q12, self.q11
        return top_element
    def empty(self):
        return not self.q11 and not self.q12

# Driver Code for Question $
stack = Stack()
stack.push(123)
stack.push(234)
stack.push(654)
stack.push(854)
stack.push(864)
stack.push(345)

print("Top element is :", stack.top_element())
print("Pop is:", stack.pop())        
print("Top element is:", stack.top_element())
print("Is stack empty now?", stack.empty())

print("")
print("")

print("**************************************************************************************")
