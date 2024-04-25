# Write a python function to impliment bubble sort


# def bubble_sort(data_list):
#     for r in range(1,len(data_list)):
#         for i in range(len(data_list)-r):
#             if data_list[i]>data_list[i+1]:
#                 data_list[i],data_list[i+1]=data_list[i+1],data_list[i]
# l=[34,67,12,89,25,50]
# bubble_sort(l)
# print(l)






def bubble(data):
    n=len(data)
    for i in range(1,n):
        for j in range(n-i):
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
d=[23,1,23,34,56,35,45,66,34,34,23,45,43,23,45]
bubble(d)
print(d)
