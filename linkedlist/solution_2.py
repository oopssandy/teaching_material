''' 
Linked List Practice Solution-2
    by 游硯竹
    12/29/2020
'''
from solution import *

class SortedLinkedList(LinkedList):
    def insert(self, data):
        if (self.head is None or self.head.data > data):
            self.head = Node(data, self.head)
        else:
            current = self.head
            while (current.next is not None and current.next.data < data):
                current = current.next
            current.next = Node(data, current.next)
        self.length += 1

    def append(self):
        raise AttributeError( "'SortedLinkedList' object has no attribute 'append'" )


class HeadTailLinkedList(LinkedList):
    def __init__(self):
        super(HeadTailLinkedList,self).__init__()
        self.tail = None
    
    def __getitem__(self, index):
        if (index == self.length-1):
            return self.tail.data
        return super(HeadTailLinkedList,self).__getitem__(index)

    def __setitem__(self, index, value):
        if (index == self.length-1):
            self.tail.data = value
        super(HeadTailLinkedList,self).__setitem__(index, value)

    def append(self, data):
        if (self.head is None):
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = self.tail = Node(data)
        self.length += 1

    def insert(self, data, index):
        if (index == self.length):
            self.append(data)
        else:
            super(HeadTailLinkedList,self).insert(data, index)

    def delete(self, index):
        if (self.length-1 == index == 0):
            self.tail = None
        return super(HeadTailLinkedList,self).delete(index)


class DoubleNode(Node):
    def __init__(self, data, next=None, prev=None):
        super(DoubleNode,self).__init__(data, next)
        self.prev = prev

class DoubleLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def index(self, data):
        current = self.head
        count = 0 
        while (current is not None):
            if (current.data == data):
                return count
            current = current.next
            count += 1
        return -1

    def __len__(self):
        return self.length
    
    def __str__(self):
        if (self.length == 0):
            return "[]"
        out = "["
        current = self.head
        while(current.next is not None):
            out += str(current.data)+" <-> "
            current = current.next
        return out + str(current.data) + "]"

    def __getitem__(self, index):
        if (index < 0 or index >= self.length):
            raise IndexError
        return self.move(index).data

    def __setitem__(self, index, value):
        if (index < 0 or index >= self.length):
            raise IndexError
        self.move(index).data = value

    def move(self, index):
        if (index <= self.length/2):
            current = self.head
            for i in range(index):
                current = current.next
        else:
            current = self.tail
            for i in range(self.length-index-1):
                current = current.prev
        return current

    def append(self, data):
        if (self.head is None):
            self.head = self.tail = DoubleNode(data)
        else:
            self.tail.next = self.tail = DoubleNode(data, prev=self.tail)
        self.length += 1

    def insert(self, data, index):
        if (index < 0 or index > self.length):
            raise IndexError
        if (index == self.length or self.head is None):
            return self.append(data)
        elif (index == 0):
            self.head.prev = self.head = DoubleNode(data, self.head)
        else:
            current = self.move(index)
            new_node = DoubleNode(data, current, current.prev)
            current.prev.next = current.prev = new_node
        self.length += 1

    def delete(self, index):
        if (index < 0 or index >= self.length):
            raise IndexError
        if (index == 0):
            out = self.head.data
            self.head = self.head.next
        else:
            current = self.head
            for i in range(index-1):
                current = current.next
            out = current.next.data
            current.next = current.next.next
        self.length -= 1
        return out