''' 
Linked List Practice Unit Test-2
    by 游硯竹
    12/31/2020
DESCRIPTION:
    disable load test by changing LOAD_TEST to False
    enable by changing to True 
| | | | |
V V V V V
'''
LOAD_TEST = False
# there are 3 tests in total, each responsible 
# for one type of LinkedList, enable by setting to 
# True or disable by setting to False
TESTS_ACTIVATE={
    "SortedLinkedListTest": True,
    "HeadTailLinkedListTest": True,
    "DoubleLinkedListTest": True,
}
import practice_2 as practice
import solution_2 as solution
import random
import unittest
import time
from test import LinkedListTest
from datetime import datetime

class SortedLinkedListTest(LinkedListTest):
    def setArr(self, key):
        self.clrArr()
        for ele in self.arrays[key]:
            self.list.insert(ele)
            self.sol.insert(ele)

    def clrArr(self):
        self.list = practice.SortedLinkedList()
        self.sol = solution.SortedLinkedList()

    @unittest.skip("SortedLinkedListTest does not have attribute append")
    def testAppend(self):
        print("this test has been skipped")

    def testNone(self):
        self.list.insert(None)
        self.assertIsNone(self.list.head.data)
        self.assertIsNone(self.list.head.next)
        self.assertEqual(len(self.list), 1)
        self.stop()

    def testInsert(self):
        for i in range (6):
            self.clrArr()
            for j in self.arrays[i]:
                self.list.insert(j)
                self.sol.insert(j)
            self.assertLinkedListEqual(self.list, self.sol)
        self.stop()

    def testLength(self):
        for i in range(20):
            self.list.insert(0)
            self.assertEqual(len(self.list), i+1)
        for i in range (6):
            self.setArr(i)
            self.assertEqual(len(self.list), len(self.arrays[i]))
        self.stop()

    @unittest.skipIf(LOAD_TEST==False, "Load test disabled")
    def testLoad(self):
        for i in range(10000):
            self.list.insert(i)
        self.assertEqual(len(self.list), 10000)
        self.stop()
    
    def testMix(self):
        for i in range(4):
            for j in self.arrays[i]:
                self.list.insert(j)
                self.sol.insert(j)
                self.assertEqual(len(self.list),len(self.sol))
            self.assertEqual(str(self.list), str(self.sol))
        for i in range(20):
            self.assertEqual(self.list.index(i),self.sol.index(i))
        self.stop()

    def testSetItem(self):
        for i in range(20):
            self.list.insert(0)
        for i in range(20):
            self.list[i] = i
            self.assertEqual(self.list[i], i)
        self.stop()

class HeadTailLinkedListTest(LinkedListTest):
    def clrArr(self):
        self.list = practice.HeadTailLinkedList()
        self.sol = solution.HeadTailLinkedList()

    @unittest.skipIf(LOAD_TEST==False, "Load test disabled")
    def testLoad(self):
        for i in range(10000):
            self.list.append(i)
        self.assertEqual(len(self.list), 10000)
        self.stop()

class DoubleLinkedListTest(LinkedListTest):
    def clrArr(self):
        self.list = practice.DoubleLinkedList()
        self.sol = solution.DoubleLinkedList()

    @unittest.skipIf(LOAD_TEST==False, "Load test disabled")
    def testLoad(self):
        for i in range(10000):
            self.list.append(i)
        self.assertEqual(len(self.list), 10000)
        self.stop()

loader = unittest.TestLoader()
runner = unittest.TextTestRunner(verbosity=2)
for name, val in TESTS_ACTIVATE.items():
    if (val):
        print("#"*70)
        print("#\t\t\t\tRunning",name)
        print("#"*70)
        suite = unittest.TestSuite()
        suite.addTests(loader.loadTestsFromTestCase(globals()[name]))
        runner.run(suite)
        print()