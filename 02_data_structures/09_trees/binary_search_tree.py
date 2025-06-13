from Node import *

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if data < current.data:
                if current.left_child is None:
                    current.left_child = new_node
                    return
                current = current.left_child
            else:
                if current.right_child is None:
                    current.right_child = new_node
                    return
                current = current.right_child

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left_child)
            print(node.data, end=" ")
            self.inorder(node.right_child)

    def preorder(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.preorder(node.left_child)
            self.preorder(node.right_child)

    def postorder(self, node):
        if node is not None:
            self.postorder(node.left_child)
            self.postorder(node.right_child)
            print(node.data, end=" ")

    def search(self, value):
        current = self.root
        while current is not None:
            if value == current.data:
                return True
            elif value < current.data:
                current = current.left_child
            else:
                current = current.right_child
        return False
