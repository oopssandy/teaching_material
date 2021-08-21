''' 
Binary Search Tree Solution 
    by 游硯竹
    12/30/2020
'''
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        return "["+self.inorder(self.root)+"]"

    def inorder(self, root):
        if root is not None:
            return self.inorder(root.left)+" "+str(root.data)+" "+self.inorder(root.right)
        return ""
    
    def traverse(self, root, data):
        # print(root.data)
        if (root.left is not None and data < root.data):
            return self.traverse(root.left, data)
        elif (root.right is not None and data > root.data):
            return self.traverse(root.right, data)
        return root

    def insert(self, data):
        self.size += 1
        if (self.root == None):
            self.root = Node(data)
        else:
            node = self.traverse(self.root, data)
            if (data < node.data):
                node.left = Node(data)
            elif (data > node.data):
                node.right = Node(data)  
            else:
                self.size -= 1
    
    def delete(self, data):
        self.root, val = self.deleteNode(self.root, data)
        if (val == data != None):
            self.size -= 1
        return val
        
    def deleteNode(self, root, data):
        if root is None:
            return root, None
        if (data < root.data):
            root.left, val = self.deleteNode(root.left, data)
        elif (data > root.data):
            root.right, val = self.deleteNode(root.right, data)
        else:
            val = root.data
            if (root.left is None):
                temp = root.right
                root = None
                return temp, val 
            elif (root.right is None):
                temp = root.left
                root = None
                return temp, val
            temp = root.right
            while (temp.left is not None):
                temp = temp.left
            root.data = temp.data
            root.right, num = self.deleteNode(root.right, temp.data)
        return root, val

    def contains(self, data):
        if (self.root is None):
            return False
        return self.traverse(self.root, data).data == data


# bst = BST()
# for i in [50, 30, 20, 40, 70, 60, 80]:
#     bst.insert(i)
# print(bst)
# print("----------------------------------------------------------------")
# for i in [50, 30, 20, 40, 70, 60, 80]:
#     print("root",bst.root)
#     print("delete",bst.delete(i), "contain",bst.contains(i),"len",len(bst))
#     print(bst)
#     print()

# print("root",bst.root)
# print("delete",bst.delete(None), "contain",bst.contains(None),"len",len(bst))
# print(bst)