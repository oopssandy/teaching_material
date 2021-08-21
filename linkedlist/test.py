''' 
Linked List Practice Unit Test
    by 游硯竹
    12/29/2020
DESCRIPTION:
    disable load test by changing LOAD_TEST to False
    enable by changing to True 
| | | | |
V V V V V
'''
LOAD_TEST = False
import practice
import solution
import random
import unittest
import time
from datetime import datetime

class LinkedListTest(unittest.TestCase):
    random.seed(0)
    arrays = [
        [x for x in range(20)],
        [x*2+1 for x in range(20)],
        [x for x in range(100)],
        [x-100 for x in range(200)],
        [x for x in range(1000)],
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
        self.list = practice.LinkedList()
        self.sol = solution.LinkedList()

    def setArr(self, key):
        self.clrArr()
        for ele in self.arrays[key]:
            self.list.append(ele)
            self.sol.append(ele)

    def assertLinkedListEqual(self, a, b):
        aCurr = a.head
        bCurr = b.head
        while (aCurr is not None and bCurr is not None):
            self.assertEqual(aCurr.data, bCurr.data)
            aCurr = aCurr.next
            bCurr = bCurr.next
        self.assertFalse(aCurr is not None and bCurr is None, msg="your list is too long")
        self.assertFalse(aCurr is None and bCurr is not None, msg="your list is too short")
    
    def testDefault(self):
        self.assertIsNone(self.list.head)
        self.assertEqual(self.list.length, 0)
        self.stop()
    
    def testNone(self):
        self.list.append(None)
        self.assertIsNone(self.list.head.data)
        self.assertIsNone(self.list.head.next)
        self.assertEqual(len(self.list), 1)
        self.stop()

    def testAppend(self):
        for i in range (6):
            self.setArr(i)
            self.assertLinkedListEqual(self.list, self.sol)
        self.stop()

    def testDelete(self):
        with self.assertRaises(IndexError, msg="no IndexError for empty list"):
            self.list.delete(0)
        for i in range (6):
            self.setArr(i)
            with self.assertRaises(IndexError, msg="no IdexError for negative index"):
                self.list.delete(-1)
            with self.assertRaises(IndexError, msg="no IdexError for out of range index"):
                self.list.delete(len(self.arrays[i]))
            for j in range (len(self.arrays[i])):
                k = len(self.arrays[i])-j-1
                self.assertEqual(self.list.delete(k), self.sol.delete(k))
        self.stop()

    def testGetItem(self):
        with self.assertRaises(IndexError, msg="no IndexError for empty list"):
            self.list[0]
        for i in range (6):
            self.setArr(i)
            with self.assertRaises(IndexError, msg="no IdexError for negative index"):
                self.list[-1]
            with self.assertRaises(IndexError, msg="no IdexError for out of range index"):
                self.list[len(self.arrays[i])]
            for j in range (len(self.arrays[i])):
                self.assertEqual(self.list[j], self.sol[j])
        self.stop()
    
    def testIndex(self):
        for i in range (6):
            self.setArr(i)
            for j in self.arrays[i]:
                self.assertEqual(self.list.index(j), self.sol.index(j))
            self.assertEqual(self.list.index(None), -1)
        self.stop()

    def testInsert(self):
        with self.assertRaises(IndexError, msg="no IdexError for negative index"):
            self.list.insert(0,-1)
        for i in range (6):
            self.clrArr()
            for j in self.arrays[i]:
                self.list.insert(j,0)
                self.sol.insert(j,0)
            self.assertLinkedListEqual(self.list, self.sol)
            with self.assertRaises(IndexError, msg="no IdexError for out of range index"):
                self.list.insert(0,len(self.arrays[i])+1)
        self.stop()

    def testLength(self):
        for i in range(20):
            self.list.insert(i,0)
            self.assertEqual(len(self.list), i+1)
        for i in range (6):
            self.setArr(i)
            self.assertEqual(len(self.list), len(self.arrays[i]))
        self.stop()

    def testSetItem(self):
        for i in range(20):
            self.list.append(0)
        for i in range(20):
            self.list[i] = i
            self.assertEqual(self.list[i], i)
        self.stop()

    def testString(self):
        for i in range (6):
            self.setArr(i)
            self.assertEqual(str(self.list), str(self.sol))
        self.stop()

    def testMix(self):
        for i in range(4):
            for j in self.arrays[i]:
                self.list.append(j)
                self.sol.append(j)
                self.list.insert(j,0)
                self.sol.insert(j,0)
                self.assertEqual(len(self.list),len(self.sol))
            self.assertEqual(str(self.list), str(self.sol))
        for i in range(20):
            self.assertEqual(self.list.index(i),self.sol.index(i))
        self.stop()

    @unittest.skipIf(LOAD_TEST==False, "Load test disabled")
    def testLoad(self):
        for i in range(10**5):
            self.list.append(i)
        self.assertEqual(len(self.list), 10**5)
        self.stop()

if __name__ == '__main__':
    unittest.main(verbosity=2)