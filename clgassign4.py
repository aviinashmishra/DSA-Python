class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def is_bst(root):
    def is_bst_util(node, min_val, max_val):
        if node is None:
            return True
        if node.value < min_val or node.value > max_val:
            return False
        return (is_bst_util(node.left, min_val, node.value - 1) and
                is_bst_util(node.right, node.value + 1, max_val))

    return is_bst_util(root, float('-inf'), float('inf'))

def closest_element_is(root, target):
    closest = float('inf')
    while root:
        if abs(root.value - target) < abs(closest - target):
            closest = root.value
        if target < root.value:
            root = root.left
        elif target > root.value:
            root = root.right
        else:
            break
    return closest

def balance_bst(root):
    def sorted_array_to_bst(arr):
        if not arr:
            return None
        mid = len(arr) // 2
        node = Node(arr[mid])
        node.left = sorted_array_to_bst(arr[:mid])
        node.right = sorted_array_to_bst(arr[mid + 1:])
        return node

    def in_order_traversal(node, arr):
        if node:
            in_order_traversal(node.left, arr)
            arr.append(node.value)
            in_order_traversal(node.right, arr)

    sorted_arr = []
    in_order_traversal(root, sorted_arr)
    return sorted_array_to_bst(sorted_arr)

# Driver code to test above functions:
root = None
root = insert(root, 5)
root = insert(root, 3)
root = insert(root, 7)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 6)
root = insert(root, 8)

print(is_bst(root)) 

closest_element = closest_element_is(root, 5.5)
print(closest_element) 

balanced_root = balance_bst(root)
print(is_bst(balanced_root))  