''' 
Linked List Practice-2
    by 游硯竹
    12/31/2020
DESCRIPTION:
    since we're done with classic Linked List, let's do some of its
    variants that aimed to improve original performance
    new classes in this file:
        SortedLinkedList
        HeadTailLinkedList
        DoubleNode
        DoubleLinkedList
TODO:
    1. look for TODOs
    2. read the instructions carefully
    3. implement the method
    4. go to test_2.py and run it (may take a few minutes for load test)
    5. fix your code if you does not pass the corresponding test
    6. try improve efficiency if possible (optional)
NOTE:
    1. feel free to make any helper methods
    2. it's totally fine to google the problems, but make sure
      you UNDERSTAND your code
    3. the answer key are in the solution_2.py file if needed
    4. this file imports LinkedList from solution.py, only change to
      practice.py if you passed test.py
    | | | | |
    V V V V V
'''
from solution import *

# this is a variant of LinkedList with elements sorted in 
# ascending order
class SortedLinkedList(LinkedList):
    # TODO: modify LinkedList insertion so instead of inserting
    # at given index, it inserts node at the first node
    # with data greater than given data, which will maintain
    # the list in ascending order
    # example: list=[1,3,5] insert 4 -> list=[1,3,4,5]
    def insert(self, data):
        pass
    
    # disable append method to prevent adding node unsorted 
    # do not need to modify
    def append(self):
        raise AttributeError( "'SortedLinkedList' object has no attribute 'append'" )

# this is a variant of LinkedList which not only keep track of
# the head of list but also the tail of list
class HeadTailLinkedList(LinkedList):
    # different from normal, there is an additional variable
    # keeping track of the tail of the list
    def __init__(self):
        super(HeadTailLinkedList,self).__init__()
        self.tail = None
    
    # all following methods functions same as LinkedList
    # TODO: adding tail cases to all following methods to improve
    #       performance of LinkedList, rewrite entire method if needed
    # NOTE: you can call parent method by 
    '''
    super(HeadTailLinkedList, self).FUNCTION_NAME(*PARAMS)
    '''
    def __getitem__(self, index):
        pass

    def __setitem__(self, index, value):
        pass

    def append(self, data):
        pass
    
    def insert(self, data, index):
        pass

# this is a node modified with two way binding where 
# next is the  next node and prev is the previous node
# do not need to modify
class DoubleNode(Node):
    def __init__(self, data, next=None, prev=None):
        super(DoubleNode,self).__init__(data, next)
        self.prev = prev

# this is a variant of LinkedList with two way binding nodes
# it keep tracks of head and tail of the list to improve performance
# NOTE: this class does not inherit LinkedList,
class DoubleLinkedList():
    # this is the constructor for the double linked list
    # initially the list has no nodes and length 0
    # do not need to modify
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # start counting from the head, return the index 
    # of the first node found with data 
    # return -1 if desired data is not found
    # do not need to modify
    def index(self, data):
        current = self.head
        count = 0 
        while (current is not None):
            if (current.data == data):
                return count
            current = current.next
            count += 1
        return -1

    # TODO: delete "pass" and implement following methods
    # NOTE: try to implement "move" first, it'll make things easier

    # return the node at index, you start moving from head or tail
    # depending on which is closer to index
    # this is a helper method for internal use
    def move(self, index):
        pass

    # return the length of the current list
    def __len__(self):
        pass
    
    # return the string represents the current list
    # format: [1 <-> 2 <-> 3]
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