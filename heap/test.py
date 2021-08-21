''' 
Heap Practice Unit Test
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

class HeapTest(unittest.TestCase):
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
        self.heap2 = practice.MinHeap()
        self.sol2 = solution.MinHeap()
        self.heap4 = practice.MinHeap(4)
        self.sol4 = practice.MinHeap(4)

    def setArr(self, key):
        self.clrArr()
        for ele in self.arrays[key]:
            self.heap2.push(ele)
            self.sol2.push(ele)
            self.heap4.push(ele)
            self.sol4.push(ele)

    def assertHeapEqual(self, a, b):
        self.assertEqual(a.body,b.body)
    
    def testDefault(self):
        self.assertEqual(self.heap2.body, [])
        self.assertEqual(self.heap4.body, [])
        self.stop()
    
    def testNone(self):
        self.heap2.push(None)
        self.assertEqual(self.heap2.body, [None])
        self.assertEqual(len(self.heap2), 1)
        self.stop()

    def testPop(self):
        for i in range (6):
            self.setArr(i)
            for j in range(len(self.arrays[i])):
                self.assertEqual(self.heap2.pop(), self.sol2.pop())
                self.assertHeapEqual(self.heap2, self.sol2)
                self.assertEqual(self.heap4.pop(), self.sol4.pop())
                self.assertHeapEqual(self.heap4, self.sol4)
        self.stop()
    
    def testContains(self):
        for i in range (6):
            self.setArr(i)
            for j in self.arrays[i]:
                self.assertEqual(self.heap2.contains(j), self.sol2.contains(j))
                self.assertEqual(self.heap4.contains(j), self.sol4.contains(j))
        self.stop()

    def testPush(self):
        for i in range (6):
            self.clrArr()
            for j in self.arrays[i]:
                self.heap2.push(j)
                self.sol2.push(j)
                self.heap4.push(j)
                self.sol4.push(j)
            self.assertHeapEqual(self.heap2, self.sol2)
            self.assertHeapEqual(self.heap4, self.sol4)
        self.stop()

    def testIsMinHeap(self):
        for i in range (6):
            self.setArr(i)
            self.assertIsMinHeap(self.heap2.body, 2)
            self.assertIsMinHeap(self.heap4.body, 4)
        self.stop()

    def assertIsMinHeap(self, body, n):
        l = len(body)
        for i in range(l):
            idx = l-i-1
            self.assertLessEqual(body[max((idx-1)//n,0)], body[idx])

    def testLength(self):
        for i in range(20):
            self.heap2.push(i)
            self.assertEqual(len(self.heap2), i+1)
            self.heap4.push(i)
            self.assertEqual(len(self.heap4), i+1)
        for i in range (6):
            self.setArr(i)
            self.assertEqual(len(self.heap2), len(self.sol2))
            self.assertEqual(len(self.heap4), len(self.sol4))
        self.stop()

    def testString(self):
        for i in range (6):
            self.setArr(i)
            self.assertEqual(str(self.heap2), str(self.sol2))
            self.assertEqual(str(self.heap4), str(self.sol4))
        self.stop()

    def testMix(self):
        for i in range(4):
            for j in self.arrays[i]:
                self.heap2.push(j)
                self.sol2.push(j)
                self.assertEqual(len(self.heap2),len(self.sol2))
                self.heap4.push(j)
                self.sol4.push(j)
                self.assertEqual(len(self.heap4),len(self.sol4))
            self.assertEqual(str(self.heap2), str(self.sol2))
            self.assertEqual(str(self.heap4), str(self.sol4))
        for i in range(20):
            self.assertEqual(self.heap2.contains(i),self.sol2.contains(i))
            self.assertEqual(self.heap4.contains(i),self.sol4.contains(i))
        self.stop()

    @unittest.skipIf(LOAD_TEST==False, "Load test disabled")
    def testLoad(self):
        for i in range(100000):
            self.heap2.push(i)
        self.assertEqual(len(self.heap2), 100000)
        self.stop()

if __name__ == '__main__':
    unittest.main(verbosity=2)