# What is a binary Tree? The following is the list of nodes in a binary tree in 2 orders:
# INORDER: HKDBILEAFCMJG
# PREORDER: ABDHKEILCFGJM
# Construct the corresponding binary tree and the postorder sequence


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def c_b_t(inorder, preorder):
    if not inorder or not preorder:
        return None

    root_data = preorder[0]
    root = Node(root_data)

    root_index = inorder.index(root_data)

    left_inorder = inorder[:root_index]
    right_inorder = inorder[root_index + 1:]

    left_preorder = preorder[1:root_index + 1]
    right_preorder = preorder[root_index + 1:]

    root.left = c_b_t(left_inorder, left_preorder)
    root.right = c_b_t(right_inorder, right_preorder)

    return root

def postorder_trav(root):
    if root is None:
        return []

    left_postorder = postorder_trav(root.left)
    right_postorder = postorder_trav(root.right)

    return left_postorder + right_postorder + [root.data]

inorder = "HKDBILEAFCMJG"
preorder = "ABDHKEILCFGJM"

root = c_b_t(inorder, preorder)
postorder = postorder_trav(root)

print("Postorder sequence is:", "".join(postorder))
print()

print("********************************************************")


# What is a B-Tree? Construct a B-Tree of order 4 with the alphabets (letters) arrive in the sequence as follows: a gfbkdhmjesirxcIntup


class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.child = []

class BTree:
    def __init__(self, order):
        self.root = BTreeNode(True)
        self.order = order

    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.order) - 1:
            temp = BTreeNode()
            self.root = temp
            temp.child.insert(0, root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append(k)
            x.keys.sort()
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.child[i].keys) == (2 * self.order) - 1:
                self.split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self.insert_non_full(x.child[i], k)

    def split_child(self, x, i):
        t = self.order
        y = x.child[i]
        z = BTreeNode(y.leaf)
        x.child.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t: (2 * t) - 1]
        y.keys = y.keys[0: t - 1]
        if not y.leaf:
            z.child = y.child[t: 2 * t]
            y.child = y.child[0: t - 1]

    def traverse(self, x):
        i = 0
        while i < len(x.keys):
            if x.leaf:
                print(x.keys[i])
            else:
                self.traverse(x.child[i])
                print(x.keys[i])
            i += 1

    def print_tree(self, x, l=0):
        print("Level", l, "Keys:", end=" ")
        for i in x.keys:
            print(i, end=" ")
        print()
        l += 1
        if len(x.child) > 0:
            for i in x.child:
                self.print_tree(i, l)

b_tree = BTree(4)

# Inserting given sequence of alphabets
sequence = "agfbkdhmjesirxcIntup"
for letter in sequence:
    b_tree.insert(letter)

# Printing the B-Tree
b_tree.print_tree(b_tree.root)

