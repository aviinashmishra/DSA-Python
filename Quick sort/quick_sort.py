#write a python function to impliment quick sort


def quick_sort(data):
    if len(data)<=1:
        return data
    else:
        pivot=data[0]
        lesser=[x for x in data[1:] if x<=pivot]
        greater=[x for x in data[1:] if x>pivot]
        return quick_sort(lesser)+[pivot]+quick_sort(greater)
    
mylist=[11,23,12,32,43,23,45,34,23,66,77,23,44,65,67,45,24,34,56,43]
mylist=quick_sort(mylist)
print(mylist)