# 2. Given a list of heterogenous elements. Write a python script to remove all the non int values from the list.
# Sample list with heterogeneous elements
mixed_list = [1, 'hello', 2.5, 3, 'world', True, 5]

# Remove non-integer values from the list
integer_list = [x for x in mixed_list if isinstance(x, int)]

print("Original List:", mixed_list)
print("List with only integers:", integer_list)

