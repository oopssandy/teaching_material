''' 
Array Practice-2 Unit Test
    by 游硯竹
    12/30/2020
'''
import practice_2 as practice
import solution_2 as solution
import random
import unittest

class ArrayTest(unittest.TestCase):
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

    def testReorderArr(self):
        self.assertReorderArr([11,22,33],[0,1,2])
        self.assertReorderArr([11,33,22,44,55],[4,1,3,2,0])
        self.assertReorderArr([-1,-2,-3],[2,1,0])
        self.assertReorderArr([i*2%11+i for i in range(200)],[199-i for i in range(200)])
        self.assertReorderArr(self.arrays[10],self.arrays[9])

    def assertReorderArr(self, a, b):
        self.assertEqual(practice.reorderArr(a, b), solution.reorderArr(a, b))

    def testFirstDuplicate(self):
        for a in self.arrays:
            self.assertEqual(practice.firstDuplicate(a), solution.firstDuplicate(a))
    
    def testMaxDuplicate(self):
        for a in self.arrays:
            self.assertEqual(practice.maxDuplicate(a), solution.maxDuplicate(a))
    
    def testMaxSubSum(self):
        for a in self.arrays:
            self.assertEqual(practice.maxSubSum(a), solution.maxSubSum(a))

    def testMergeSort(self):
        for a in self.arrays:
            self.assertEqual(practice.mergeSort(a), solution.mergeSort(a))

    def testHeapSort(self):
        for a in self.arrays:
            self.assertEqual(practice.heapSort(a), solution.heapSort(a))
        
if __name__ == '__main__':
    unittest.main(verbosity=2)