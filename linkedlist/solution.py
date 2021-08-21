''' 
Linked List Practice Solution
    by 游硯竹
    12/29/2020
'''
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length

    def __str__(self):
        if (self.length == 0):
            return "[]"
        out = "["
        current = self.head
        while(current.next is not None):
            out += str(current.data)+" -> "
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
        current = self.head
        for i in range(index):
            current = current.next
        return current

    def append(self, data):
        if (self.head is None):
            self.head = Node(data)
        else:
            current = self.head
            while(current.next is not None):
                current = current.next
            current.next = Node(data)
        self.length += 1

    def insert(self, data, index):
        if (index < 0 or index > self.length):
            raise IndexError
        if (index == 0):
            new_node = Node(data, self.head)
            self.head = new_node
        else:
            current = self.move(index-1)
            new_node = Node(data, current.next)
            current.next = new_node
        self.length += 1

    def delete(self, index):
        if (index < 0 or index >= self.length):
            raise IndexError
        if (index == 0):
            out = self.head.data
            self.head = self.head.next
        else:
            current = self.move(index-1)
            out = current.next.data
            current.next = current.next.next
        self.length -= 1
        return out

    def index(self, data):
        current = self.head
        count = 0 
        while (current is not None):
            if (current.data == data):
                return count
            current = current.next
            count += 1
        return -1