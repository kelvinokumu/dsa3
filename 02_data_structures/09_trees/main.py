from binary_search_tree import *


bst = BinarySearchTree()
values = [10, 5, 15, 3, 7, 12, 17]
for v in values:
    bst.insert(v)

print("Inorder Traversal (Sorted):")
bst.inorder(bst.root)
print("\n")

print("Preorder Traversal:")
bst.preorder(bst.root)
print("\n")

print("Postorder Traversal:")
bst.postorder(bst.root)
print("\n")

print("Search for 12:", bst.search(12))
print("Search for 20:", bst.search(20))
