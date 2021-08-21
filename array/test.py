''' 
Array Practice Unit Test
    by 游硯竹
    12/29/2020
'''
import practice
import solution
import random
import unittest

class ArrayTest(unittest.TestCase):
    TEST_IN_TYPE = False
    def setUp(self):
        random.seed(0)
        self.arrays = [
            [0,0,0],[1,1,1],[1,2,3],[3,2,1],[-1,-2,-3],[-5,-3,-1],
            [1,4,2,1],[-7,1,6,-5,3],[0,1,2,3,4,5,-6],
            [i for i in range(200)],[i-100 for i in range(200)],
            [i%13 for i in range(200)],[i%13-7 for i in range(200)]
        ]
        for i in range(9,13):
            random.shuffle(self.arrays[i])

    def testSumArr(self):
        self.assertSumArr([0,0,0],[1,1,1])
        self.assertSumArr([-1,-2,-3],[-5,-3,-1])
        self.assertSumArr([-1,2,5],[5,-3,-10])
        self.assertSumArr([i for i in range(200)],[i*2 for i in range(200)])
        with self.assertRaises(ValueError):
            practice.sumArr([0,0,0],[0,0])
        if (self.TEST_IN_TYPE):
            with self.assertRaises(TypeError):
                practice.sumArr([0,0,0],"abc")
            with self.assertRaises(TypeError):
                practice.sumArr([1,2,"c"],[3,4,"d"])
            with self.assertRaises(TypeError):
                practice.sumArr(1,2)
            with self.assertRaises(TypeError):
                practice.sumArr(1,'a')

    def assertSumArr(self, a, b):
        self.assertEqual(practice.sumArr(a, b), solution.sumArr(a, b))

    def testMean(self):
        for a in self.arrays:
            self.assertEqual(practice.arrMean(a), solution.arrMean(a))
        if (self.TEST_IN_TYPE):
            with self.assertRaises(TypeError):
                practice.arrMean("abc")
            with self.assertRaises(TypeError):
                practice.arrMean([1,2,"c"])
            with self.assertRaises(TypeError):
                practice.arrMean(1)

    def testVar(self):
        for a in self.arrays:
            self.assertEqual(practice.arrVar(a), solution.arrVar(a))
        if (self.TEST_IN_TYPE):
            with self.assertRaises(TypeError):
                practice.arrVar("abc")
            with self.assertRaises(TypeError):
                practice.arrVar([1,2,"c"])
            with self.assertRaises(TypeError):
                practice.arrVar(1)

    def testReverse(self):
        for a in self.arrays:
            self.assertEqual(practice.reverseArr(a), solution.reverseArr(a))
        if (self.TEST_IN_TYPE):
            with self.assertRaises(TypeError):
                practice.reverseArr(1)

    def testSortTwoArr(self):
        self.assertSortTwoArr([0,0,0], [0,0,0])
        self.assertSortTwoArr([1,2,4], [3,5,6])
        self.assertSortTwoArr([1,2,3], [-3,-2,-1])
        self.assertSortTwoArr([-7,-5,3], [-7,-5,3])
        self.assertSortTwoArr([-9,-7,3,3,4,5], [-7,-5,100])
        self.assertSortTwoArr([i for i in range(200)], [198+i for i in range(200)])
        if (self.TEST_IN_TYPE):
            with self.assertRaises(TypeError):
                practice.sortTwoArr([1],["a"])
            with self.assertRaises(TypeError):
                practice.sortTwoArr(["a"],["b"])

    def assertSortTwoArr(self, a, b):
        self.assertEqual(practice.sortTwoArr(a, b), solution.sortTwoArr(a, b))

    def testBubbleSort(self):
        for a in self.arrays:
            self.assertEqual(practice.bubbleSort(a), solution.bubbleSort(a))
        if (self.TEST_IN_TYPE):
            with self.assertRaises(TypeError):
                practice.bubbleSort([1,"a",'b'])

    def testSelectionSort(self):
        for a in self.arrays:
            self.assertEqual(practice.selectionSort(a), solution.selectionSort(a))
        if (self.TEST_IN_TYPE):
            with self.assertRaises(TypeError):
                practice.selectionSort([1,"a",'b'])

    def testInsertionSort(self):
        for a in self.arrays:
            self.assertEqual(practice.insertionSort(a), solution.insertionSort(a))
        if (self.TEST_IN_TYPE):
            with self.assertRaises(TypeError):
                practice.insertionSort([1,"a",'b'])
        
if __name__ == '__main__':
    unittest.main(verbosity=2)