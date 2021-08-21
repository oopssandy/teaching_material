''' 
Linked List Practice 
    by 游硯竹
    12/29/2020
DESCRIPTION:
    let's implement linked list for fun!!! (･ω･)b
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
# this is the node of linked list
# each node contains a data and a link to next node
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    # this is the constructor for the linked list
    # initially the list has no nodes and length 0
    def __init__(self):
        self.head = None
        self.length = 0

    # return the length of the current list
    def __len__(self):
        pass

    # return the string represents the current list
    # format: [1 -> 2 -> 3]
    def __str__(self):
        pass

    # return the data of node at index 
    # raise IndexError for illegal index
    # illegal index: index < 0 or index >= len
    def __getitem__(self, index):
        pass

    # set the node at the specified index to value
    # do not need to return
    # raise IndexError for illegal index
    # illegal index: index < 0 or index >= len
    def __setitem__(self, index, value):
        pass
    
    # add a new node at the end of list with data
    # do not need to return
    def append(self, data):
        pass

    # add a new node at index with data, so the original
    # node at index will become the next of the new node
    # do not need to return
    # raise IndexError for illegal index
    # illegal index: index < 0 or index > len
    def insert(self, data, index):
        pass

    # delete the node at index and return its data
    # raise IndexError for illegal index
    # illegal index: index < 0 or index >= len
    def delete(self, index):
        pass

    # start counting from the head, return the index 
    # of the first node found with data 
    # return -1 if desired data is not found
    def index(self, data):
        pass