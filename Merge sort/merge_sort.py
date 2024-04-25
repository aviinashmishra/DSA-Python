# write a code to impliment merge sort


def merge_sort(data):
    if len(data)>1:
        med=len(data)//2
        leftlist=data[:med]
        rightlist=data[med:]

        merge_sort(leftlist)
        merge_sort(rightlist)

        i=j=k=0
        while i<len(leftlist) and j<len(rightlist):
            if leftlist[i]<rightlist[j]:
                data[k]=leftlist[i]
                i+=1
            else:
                data[k]=rightlist[j]
                j+=1
            k+=1
        while i<len(leftlist):
            data[k]=leftlist[i]
            i+=1
            k+=1
        while j<len(rightlist):
            data[k]=rightlist[j]
            j+=1
            k+=1

mylist=[12,24,12,34,34,56,45,56,57,67,78,56,55]
merge_sort(mylist)
print(mylist)

