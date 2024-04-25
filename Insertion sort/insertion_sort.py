# Write a python function to impliment insertion sort
def insertion_sort(list1):
    n=len(list1)
    for i in range(1,n):
        temp=list1[i]

        j=i-1
        while j>=0 and temp<list1[j]:
            list1[j+1]=list1[j]
            j-=1
        list1[j+1]=temp

mylist=[25,34,25,26,33,45,77,56,45,23,54]
insertion_sort(mylist)
print(mylist)
