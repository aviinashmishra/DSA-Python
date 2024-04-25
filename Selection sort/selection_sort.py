# Write a python function to impliment selection sort

# def selection_sort(list1):
#     n=len(list1)
#     for i in range(n-1):
#         min_index=i
#         for j in range(i+1,n):
#             if list1[j]<list1[min_index]:
#                 min_index=j
#         list1[i],list1[min_index]=list1[min_index],list1[i]
# l1=[64,35,26,37,45,17,66]
# selection_sort(l1)
# print(l1)



def sel_sort(data):
    n=len(data)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if data[j]<data[min_index]:
                min_index=j
        data[i],data[min_index]=data[min_index],data[i]
l=[23,12,34,23,34,56,45,67,89,87]
sel_sort(l)
print(l)



