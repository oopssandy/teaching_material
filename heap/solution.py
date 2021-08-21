''' 
Heap Practice Solution
    by 游硯竹
    12/30/2020
'''
class MinHeap:
    # this is the constructor for the min heap
    # initially the heap is a empty array
    # NOTE: NUM_CHILDREN is the max number of 
    #       children for a node in heap
    # raise ValueError if NUM_CHILDREN < 2
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
        return len(self.body)

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
        l = len(self.body)
        if (l < 2):
            return
        i = 0
        while (self.NUM_CHILDREN*i < l):
            children = self.children(i)
            minVal, minIndex = self.body[i], i
            for child in children:
                if (child < l and self.body[child] < minVal):
                    minVal, minIndex = self.body[child], child
            if (minIndex == i):
                return
            self.body[i], self.body[minIndex] = self.body[minIndex], self.body[i]
            i = minIndex

    # append a new value to body then organize the heap
    # NOTE: the organize process should start from end
    # do not need to return
    def push(self, data):
        self.body.append(data)
        i = len(self.body)-1
        p = self.parent(i)
        while (p >= 0 and self.body[i] < self.body[p]):
            self.body[i], self.body[p] = self.body[p], self.body[i]
            i, p = p, self.parent(p)

    # delete and return the minimum value in heap then 
    # organize the heap 
    # return None if heap is empty
    # NOTE: the organize process should start from root
    def pop(self):
        l = len(self.body)
        if (l==0):
            return None
        out, self.body[0] = self.body[0], self.body[l-1]
        del self.body[l-1]
        self.heapify()
        return out

    # return True if heap contains data, False otherwise
    def contains(self, data):
        return data in self.body

    # return True if heap is empty, False otherwise
    def isEmpty(self):
        return len(self.body)==0

    # return the minimum value in heap
    # return None if heap is empty
    # NOTE: do NOT delete the returned value
    def minVal(self):
        if (len(self.body) > 0):
            return self.body[0]
        return None

# import random
# random.seed(0)
# arr = [0 for i in range(20)]
# random.shuffle(arr)
# h2 = MinHeap()
# h4 = MinHeap(4)
# for i in arr:
#     h2.push(i)
#     h4.push(i)
# while (not h2.isEmpty() and not h4.isEmpty()):
#     print("h2",h2.pop(), len(h2),"h4",h4.pop(), len(h4))