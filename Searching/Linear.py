list = [23,23,14,23,24,35,45,65,47,67,98,67,58,96,45,34,23,12,23,34,45,56,67,78,89,67,455]
def linear_search(list,element):
    for i in range(len(list)):
        if list[i]==element:
            return i
    return None
print(linear_search(list, 58))