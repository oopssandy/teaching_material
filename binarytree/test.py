''' 
Binary Search Tree Practice Unit Test
    by 游硯竹
    12/30/2020
DESCRIPTION:
    disable load test by changing LOAD_TEST to False
    enable by changing to True 
| | | | |
V V V V V
'''
LOAD_TEST = False
import sys
sys.setrecursionlimit(15000)

import practice
import solution
import random
import unittest
import time
from datetime import datetime

class BSTTest(unittest.TestCase):
    random.seed(0)
    arrays = [
        [x for x in range(20)],
        [x*2+1 for x in range(20)],
        [x for x in range(100)],
        [x-100 for x in range(200)],
        [x for x in range(500)],
        [chr(x) for x in range(33, 255)]
    ]
    random.shuffle(arrays[2])

    def setUp(self):
        self.clrArr()
        self.start = datetime.now()

    def stop(self):
        end = datetime.now()
        diff = end - self.start
        print('%.3f ms' % (diff.total_seconds() * 1000) , end=" ")
    
    def clrArr(self):
        self.tree = practice.BST()
        self.sol = solution.BST()

    def setArr(self, key):
        self.clrArr()
        for ele in self.arrays[key]:
            self.tree.insert(ele)
            self.sol.insert(ele)

    def assertBSTEqual(self, a, b):
        self.assertTrue(self.isIdentical(a.root,b.root))

    def isIdentical(self, root1, root2):
        if (root1 == root2 == None): 
            return True
        elif (root1 != None and root2 == None): 
            return False
        elif (root1 == None and root2 != None): 
            return False
        else: 
            return (root1.data == root2.data and 
                    self.isIdentical(root1.left, root2.left) and 
                    self.isIdentical(root1.right, root2.right))
    
    def testDefault(self):
        self.assertIsNone(self.tree.root)
        self.assertEqual(self.tree.size, 0)
        self.stop()
    
    def testNone(self):
        self.tree.insert(None)
        self.assertIsNone(self.tree.root.data)
        self.assertIsNone(self.tree.root.left)
        self.assertIsNone(self.tree.root.right)
        self.assertEqual(len(self.tree), 1)
        self.stop()

    def testDelete(self):
        for i in range (6):
            self.setArr(i)
            for j in self.arrays[i]:
                self.assertEqual(self.tree.delete(j), self.sol.delete(j))
                self.assertBSTEqual(self.tree, self.sol)
        self.stop()
    
    def testContains(self):
        for i in range (6):
            self.setArr(i)
            for j in self.arrays[i]:
                self.assertEqual(self.tree.contains(j), self.sol.contains(j))
        self.stop()

    def testInsert(self):
        for i in range (6):
            self.clrArr()
            for j in self.arrays[i]:
                self.tree.insert(j)
                self.sol.insert(j)
            self.assertBSTEqual(self.tree, self.sol)
        self.stop()

    def testIsBST(self):
        for i in range (6):
            self.setArr(i)
            self.assertIsBST(self.tree.root)
        self.stop()

    def assertIsBST(self, root):
        if (root is not None):
            if (root.left is not None):
                self.assertLess(root.left.data, root.data)
                self.assertIsBST(root.left)
            if (root.right is not None):
                self.assertGreater(root.right.data, root.data)
                self.assertIsBST(root.right)

    def testLength(self):
        for i in range(20):
            self.tree.insert(i)
            self.assertEqual(len(self.tree), i+1)
        for i in range (6):
            self.setArr(i)
            self.assertEqual(len(self.tree), len(self.sol))
        self.stop()

    def testString(self):
        for i in range (6):
            self.setArr(i)
            self.assertEqual(str(self.tree), str(self.sol))
        self.stop()

    def testMix(self):
        for i in range(4):
            for j in self.arrays[i]:
                self.tree.insert(j)
                self.sol.insert(j)
                self.assertEqual(len(self.tree),len(self.sol))
            self.assertEqual(str(self.tree), str(self.sol))
        for i in range(20):
            self.assertEqual(self.tree.contains(i),self.sol.contains(i))
        self.stop()

    @unittest.skipIf(LOAD_TEST==False, "Load test disabled")
    def testLoad(self):
        for i in range(10000):
            self.tree.insert(i)
        self.assertEqual(len(self.tree), 10000)
        self.stop()

if __name__ == '__main__':
    unittest.main(verbosity=2)