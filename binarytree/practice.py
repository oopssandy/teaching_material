''' 
Binary Search Tree Practice 
    by 游硯竹
    12/30/2020
DESCRIPTION:
    let's implement binary tree for fun!!! (･ω･)b
TODO:
    1. read the instructions carefully
    2. delete the "pass"
    3. implement the method
    4. go to test.py and run it (may take a few minutes for load test)
    5. fix your code if you does not pass the corresponding test
    6. try improve efficiency if possible (optional)
NOTE:
    1. feel free to make any helper methods
    2. it's totally fine to google the problems, but make sure
      you UNDERSTAND your code
    3. the answer key are in the solution.py file if needed
'''
# this is the node of binary tree
# each node contains data and links to children nodes
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.data)

class BST:
    # this is the constructor for the binary tree
    # initially the tree has no nodes and size 0
    def __init__(self):
        self.root = None
        self.size = 0

    # return the size of the current tree
    def __len__(self):
        pass

    # return the string represents the current tree
    # format: [ 1 2 3 ] (in ascending order)
    def __str__(self):
        pass
    
    # add a new node with data to tree
    # do nothing if any node contains data
    def insert(self, data):
        pass

    # delete the node with data and return its data
    # do nothing if no node contains data
    def delete(self, data):
        pass

    # return True if any node contains data, False otherwise
    def contains(self, data):
        pass