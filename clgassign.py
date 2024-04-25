
data = [43, 77, 22, 5, 31, 96, 18, 33, 37, 6, 32, 37, 41, 52, 21, 19, 61, 80, 45, 33]


def sel_sort_asce(data):
    n = len(data)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
    return data

def sel_sort_desc(data):
    n = len(data)
    for i in range(n-1):
        max_index = i
        for j in range(i+1, n):
            if data[j] > data[max_index]:
                max_index = j
        data[i], data[max_index] = data[max_index], data[i]
    return data

# Driver code of selection sorting
print("Original list for selection sorting:", data)
print("Ascending order:", sel_sort_asce(data.copy()))
print("Descending order:", sel_sort_desc(data.copy()))




def quick_sort(data, ascending=True):
    if len(data) <= 1:
        return data
    else:
        pivot = data[0]
        if ascending:
            less_than_pivot = [x for x in data[1:] if x <= pivot]
            greater_than_pivot = [x for x in data[1:] if x > pivot]
        else:
            less_than_pivot = [x for x in data[1:] if x >= pivot]
            greater_than_pivot = [x for x in data[1:] if x < pivot]
        return quick_sort(less_than_pivot, ascending) + [pivot] + quick_sort(greater_than_pivot, ascending)

# Driver code for quick sorting
print("Original list for quick sorting", data)
# Ascending order
sorted_array_asce = quick_sort(data)
print("Ascending Order:", sorted_array_asce)

# Descending order
sorted_array_desc = quick_sort(data, ascending=False)
print("Descending Order:", sorted_array_desc)




def bubble_sort_asce(data):
    b = len(data)
    for i in range(b):
        for j in range(0, b-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

def bubble_sort_desc(data):
    b = len(data)
    for i in range(b):
        for j in range(0, b-i-1):
            if data[j] < data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

# Driver code for bubble sorting
print("Original list for bubble sorting:", data)
print("Ascending order:", bubble_sort_asce(data.copy()))
print("Descending order:", bubble_sort_desc(data.copy()))




def insertion_sort_asce(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

def insertion_sort_desc(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key > data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

# Driver code for Insertion sorting
print("Original list for insertion sorting:", data)
print("Ascending order:", insertion_sort_asce(data.copy()))
print("Descending order:", insertion_sort_desc(data.copy()))




def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1

def merge_sort_asce(data):
    merge_sort(data)
    return data

def merge_sort_desc(data):
    merge_sort(data)
    return data[::-1]

# Driver code for Merge Sorting
print("Original list for merge sorting:", data)
print("Ascending order:", merge_sort_asce(data.copy()))
print("Descending order:", merge_sort_desc(data.copy()))





def linear_search(data, target):
    comparisons = 0
    for i in range(len(data)):
        comparisons += 1
        if data[i] == target:
            return comparisons, i  
    return comparisons, -1  

# Driver codes
ascending_list = sorted(data)
descending_list = sorted(data, reverse=True)

target = 20  

# Unsorted list
comparisons_unsorted, index_unsorted = linear_search(data, target)
print("Unsorted List:")
print("Number of comparisons:", comparisons_unsorted)
print("Index found:", index_unsorted)

# Ascending list
comparisons_ascending, index_ascending = linear_search(ascending_list, target)
print("\nAscending List:")
print("Number of comparisons:", comparisons_ascending)
print("Index found:", index_ascending)

# Descending list
comparisons_descending, index_descending = linear_search(descending_list, target)
print("\nDescending List:")
print("Number of comparisons:", comparisons_descending)
print("Index found:", index_descending)





def binary_search(data, target):
    comparisons = 0
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1

        if data[mid] == target:
            return comparisons  
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return comparisons  

# Driver code
asce_list = [5, 6, 18, 19, 21, 22, 31, 32, 33, 33, 37, 37, 41, 43, 45, 52, 61, 77, 80, 96]
desc_list = [96, 80, 77, 61, 52, 45, 43, 41, 37, 37, 33, 33, 32, 31, 22, 21, 19, 18, 6, 5]

target = 22  

# Ascending list
comp_asce = binary_search(asce_list, target)
print("Ascending List:")
print("Number of comparisons:", comp_asce)

# Descending list
comp_desc = binary_search(desc_list, target)
print("\nDescending List:")
print("Number of comparisons:", comp_desc)

