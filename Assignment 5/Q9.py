# 9. In class CLL, implement iterator for CLL to access all the elements of the list in a sequence.


class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class CLL:
    def __init__(self, last=None):
        self.last = last

    def is_empty(self):
        return self.last == None

    def insert_at_start(self, data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n

    def insert_at_last(self, data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            self.last.next = n
            self.last = n
            n.next = self.last.next

    def search(self, data):
        if self.is_empty():
            return None
        temp = self.last.next
        while temp != self.last:
            if temp.item == data:
                return temp
            temp = temp.next
        if temp.item == data:
            return temp
        return None

    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(data, temp.next)
            temp.next = n
            if temp == self.last:
                self.last = n

    def print_list(self):
        if not self.is_empty():
            temp = self.last.next
            while temp != self.last:
                print(temp.item, end=' ')
                temp = temp.next
            print(temp.item)  # Print the last element as well

    def delete_item(self, data):
        if not self.is_empty():
            if self.last.next == self.last:  # Handle single-node case
                if self.last.item == data:
                    self.last = None
            else:
                prev = self.last  # Use a previous pointer to track the node before the one to delete
                temp = self.last.next
                while temp != self.last:
                    if temp.next == self.last:
                        if self.last.item == data:  # Check last node's data here
                            prev.next = self.last.next
                            self.last = prev
                            break
                    if temp.next.item == data:
                        prev.next = temp.next
                        break
                    prev = temp
                    temp = temp.next

    def __iter__(self):
        if self.last == None:
            return CLLIterator(None)
        else:
            return CLLIterator(self.last.next)

class CLLIterator:
    def __init__(self, start):
        self.current = start
        self.start = start
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == None:
            raise StopIteration
        # No need to check for self.current == self.start and self.count == 1
        else:
            self.count = 1
            data = self.current.item
            self.current = self.current.next
            return data

# Driver code
cll = CLL()
cll.insert_at_start(10)
cll.insert_at_start(20)
cll.insert_at_last(30)
cll.insert_at_last(40)
cll.insert_after(cll.search(10), 50)
for x in cll:
    print(x, end=' ')
print()
cll.print_list()













# class Node:
#     def __init__(self,item=None,next=None):
#         self.item=item
#         self.next=next
# class CLL:
#     def __init__(self,last=None):
#         self.last=last
#     def is_empty(self):
#         return self.last==None
#     def insert_at_start(self,data):
#         n=Node(data)
#         if self.is_empty():
#             n.next=n
#             self.last=n
#         else:
#             n.next=self.last.next
#             self.last.next=n
#     def insert_at_last(self,data):
#         n=Node(data)
#         if self.is_empty():
#             n.next=n
#             self.last=n
#         else:
#             self.last.next=n
#             self.last=n
#             n.next=self.last.next
#     def search(self,data):
#         if self.is_empty():
#             return None
#         temp=self.last.next
#         while temp!=self.last:
#             if temp.item==data:
#                 return temp
#             temp=temp.next
#         if temp.item==data:
#             return temp
#         return None
#     def insert_after(self,temp,data):
#         if temp is not None:
#             n=Node(data,temp.next)
#             temp.next=n
#             if temp==self.last:
#                 self.last=n
#     def print_list(self):
#         if not self.is_empty():
#             temp=self.last.next
#             while temp!=self.last:
#                 print(temp.item,end=' ')
#                 temp=temp.next
#             print(temp.item)
#     def delete_first(self):
#         if not self.is_empty():
#             if self.last.next==self.last:
#                 self.last=None
#             else:
#                 self.last.next=self.last.next.next
#     def delete_last(self):
#         if not self.is_empty():
#             if self.last.next==self.last:
#                 self.last=None
#             else:
#                 temp=self.last.next
#                 while temp.next!=self.last:
#                     temp=temp.next
#                 temp.next=self.last.next
#                 self.last=temp
#     def delete_item(self,data):
#         if not self.is_empty():
#             if self.last.next==self.last:
#                 if self.last.item==data:
#                     self.last=None
#                 else:
#                     if self.last.next.item==data:
#                         self.delete_first()
#                     else:
#                         temp=self.last.next
#                         while temp!=self.last:
#                             if temp.next==self.last:
#                                 if self.last.item==data:
#                                   self.delete_last()
#                                 break
#                             if temp.next.item==data:
#                                 temp.next=temp.next.next
#                                 break
#                             temp=temp.next
#     def __iter__(self):
#         if self.last==None:
#             return CLLIterator(None)
#         else:
#             return CLLIterator(self.last.next)

# class CLLIterator:
#     def __init__(self,start):
#         self.current=start
#         self.start=start
#         self.count=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.current==None:
#             raise StopIteration
#         if self.current==self.start and self.count==1:
#             raise StopIteration
#         else:
#             self.count=1
#         data=self.current.item
#         self.current=self.current.next

#         return data
    

# #Driver code
    

# cll=CLL()
# cll.insert_at_start(10)
# cll.insert_at_start(20)
# cll.insert_at_last(30)
# cll.insert_at_last(40)
# cll.insert_after(cll.search(10),50)
# for x in cll:
#     print(x,end=' ')
# print()
# cll.print_list()