''' 
Heap Practice practice
    by 游硯竹
    12/30/2020
DESCRIPTION:
    let's implement min heap for fun!!! (･ω･)b
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
class MinHeap:
    # this is the constructor for the min heap
    # initially the heap is a empty array
    # NOTE: NUM_CHILDREN is the max number of 
    #       children for a node in heap
    # raise ValueError if NUM_CHILDREN < 2
    # do not need to modify
    def __init__(self, NUM_CHILDREN=2):
        if (NUM_CHILDREN < 2):
            raise ValueError
        self.body = []
        self.NUM_CHILDREN = NUM_CHILDREN

    # return the string represents the current heap
    # do not need to modify
    def __str__(self):
        return str(self.body)
    
    # return the length of the current heap
    def __len__(self):
        pass

    # return the children indices of idx in heap
    # helper method, do not need to modify
    def children(self, idx):
        return [self.NUM_CHILDREN*idx+i+1 for i in range(self.NUM_CHILDREN)]
    
    # return the parent index of idx in heap
    # helper method, do not need to modify
    def parent(self, idx):
        return (idx-1)//self.NUM_CHILDREN

    # helper method that organize heap start from root
    # NOTE: this method should be used after poping 
    #       the minimum value in heap
    # do not need to return
    def heapify(self):
        pass

    # append a new value to body then organize the heap
    # NOTE: the organize process should start from end
    # do not need to return
    def push(self, data):
        pass

    # delete and return the minimum value in heap then 
    # organize the heap 
    # return None if heap is empty
    # NOTE: the organize process should start from root
    def pop(self):
        pass

    # return True if heap contains data, False otherwise
    def contains(self, data):
        pass

    # return True if heap is empty, False otherwise
    def isEmpty(self):
        pass

    # return the minimum value in heap
    # return None if heap is empty
    # NOTE: do NOT delete the returned value
    def minVal(self):
        pass