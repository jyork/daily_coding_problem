""" 
Daily Coding Problem: Problem #48 [Medium]
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

For example, given the following preorder traversal:

[a, b, d, e, c, f, g]

And the following inorder traversal:

[d, b, e, a, f, c, g]

You should return the following tree:

    a
   / \
  b   c
 / \ / \
d  e f  g
 """

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def print(self):
        val = self.value
        if self.left:
            val += ": left child is " + self.left.value
        if self.right:
            val += ": right child is " + self.right.value
        print(val)
        if self.left:
            self.left.print()
        if self.right:
            self.right.print()

def build_tree(preorder, inorder):
    if not preorder and not inorder:
        return None
    root = Node(preorder[0])
    root_index = inorder.index(root.value)
    if root_index > 0:
        root.left = build_tree(preorder[1:root_index + 1], inorder[:root_index])
    else:
        root.left = None

    root.right = build_tree(preorder[root_index + 1:], inorder[root_index + 1:])
    return root

preorder = ["a", "b", "d", "e", "c", "f", "g"]
inorder = ["d", "b", "e", "a", "f", "c", "g"]
tree = build_tree(preorder, inorder)
tree.print()
print("Next")
preorder = ["a", "b", "d", "c", "f", "g"]
inorder = ["d", "b", "a", "f", "c", "g"]
tree = build_tree(preorder, inorder)
tree.print()
