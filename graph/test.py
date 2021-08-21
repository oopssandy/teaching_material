''' 
Graph Practice Unit Test
    by 游硯竹
    1/23/2020
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
import copy
import random
import unittest
import time
from datetime import datetime

class GraphTest(unittest.TestCase):
    diret_vertex = {0: [1, 2], 1: [3], 2: [4], 3: [4], 4: [5], 5: [6, 7], 6: [8], 7: [9], 8: [9], 9: [10], 10: [11, 12], 11: [13], 12: [14], 13: [14], 14: [15], 15: [16, 17], 16: [18], 17: [19], 18: [19], 19: [20], 20: [21, 22], 21: [23], 22: [24], 23: [24], 24: [25], 25: [26, 27], 26: [28], 27: [29], 28: [29], 29: []}
    diret_edge = {(0, 1): 1, (0, 2): 1, (1, 3): 1, (2, 4): 1, (3, 4): 1, (4, 5): 1, (5, 6): 1, (5, 7): 1, (6, 8): 1, (7, 9): 1, (8, 9): 1, (9, 10): 1, (10, 11): 1, (10, 12): 1, (11, 13): 1, (12, 14): 1, (13, 14): 1, (14, 15): 1, (15, 16): 1, (15, 17): 1, (16, 18): 1, (17, 19): 1, (18, 19): 1, (19, 20): 1, (20, 21): 1, (20, 22): 1, (21, 23): 1, (22, 24): 1, (23, 24): 1, (24, 25): 1, (25, 26): 1, (25, 27): 1, (26, 28): 1, (27, 29): 1, (28, 29): 1}    
    ndiret_vertex = {0: [1, 2], 1: [3, 0], 2: [4, 0], 3: [4, 1], 4: [5, 2, 3], 5: [6, 7, 4], 6: [8, 5], 7: [9, 5], 8: [9, 6], 9: [10, 7, 8], 10: [11, 12, 9], 11: [13, 10], 12: [14, 10], 13: [14, 11], 14: [15, 12, 13], 15: [16, 17, 14], 16: [18, 15], 17: [19, 15], 18: [19, 16], 19: [20, 17, 18], 20: [21, 22, 19], 21: [23, 20], 22: [24, 20], 23: [24, 21], 24: [25, 22, 23], 25: [26, 27, 24], 26: [28, 25], 27: [29, 25], 28: [29, 26], 29: [27, 28]}
    ndiret_edge = {(0, 1): 1, (0, 2): 1, (1, 3): 1, (2, 4): 1, (3, 4): 1, (4, 5): 1, (5, 6): 1, (5, 7): 1, (6, 8): 1, (7, 9): 1, (8, 9): 1, (9, 10): 1, (10, 11): 1, (10, 12): 1, (11, 13): 1, (12, 14): 1, (13, 14): 1, (14, 15): 1, (15, 16): 1, (15, 17): 1, (16, 18): 1, (17, 19): 1, (18, 19): 1, (19, 20): 1, (20, 21): 1, (20, 22): 1, (21, 23): 1, (22, 24): 1, (23, 24): 1, (24, 25): 1, (25, 26): 1, (25, 27): 1, (26, 28): 1, (27, 29): 1, (28, 29): 1, (1, 0): 1, (2, 0): 1, (3, 1): 1, (4, 2): 1, (4, 3): 1, (5, 4): 1, (6, 5): 1, (7, 5): 1, (8, 6): 1, (9, 7): 1, (9, 8): 1, (10, 9): 1, (11, 10): 1, (12, 10): 1, (13, 11): 1, (14, 12): 1, (14, 13): 1, (15, 14): 1, (16, 15): 1, (17, 15): 1, (18, 16): 1, (19, 17): 1, (19, 18): 1, (20, 19): 1, (21, 20): 1, (22, 20): 1, (23, 21): 1, (24, 22): 1, (24, 23): 1, (25, 24): 1, (26, 25): 1, (27, 25): 1, (28, 26): 1, (29, 27): 1, (29, 28): 1}
    
    def setUp(self):
        self.graph_dir = practice.Graph()
        self.sol_dir = solution.Graph()
        self.graph_ndir = practice.Graph(directed=False)
        self.sol_ndir = solution.Graph(directed=False)
        self.start = datetime.now()

    def stop(self):
        end = datetime.now()
        diff = end - self.start
        print('%.3f ms' % (diff.total_seconds() * 1000) , end=" ")

    def setGraph(self):
        self.graph_dir = practice.Graph(copy.deepcopy(self.diret_vertex),copy.deepcopy(self.diret_edge))
        self.sol_dir = solution.Graph(copy.deepcopy(self.diret_vertex),copy.deepcopy(self.diret_edge))
        self.graph_ndir = practice.Graph(copy.deepcopy(self.diret_vertex),copy.deepcopy(self.diret_edge),directed=False)
        self.sol_ndir = solution.Graph(copy.deepcopy(self.diret_vertex),copy.deepcopy(self.diret_edge),directed=False)

    def assertGraphEqual(self, a, b, msg=None):
        self.assertEqual(a.vertdict,b.vertdict,msg=msg)
        self.assertEqual(a.edges,b.edges,msg=msg)
    
    def testDefault(self):
        self.assertEqual(self.graph_dir.vertdict, {})
        self.assertEqual(self.graph_ndir.vertdict, {})
        self.assertEqual(self.graph_dir.edges, {})
        self.assertEqual(self.graph_ndir.edges, {})
        self.stop()
    
    def testNone(self):
        self.graph_dir.addVertex(None)
        self.assertEqual(self.graph_dir.vertdict[None], [])
        self.assertEqual(len(self.graph_dir), 1)
        self.stop()
    
    def testAddVertex(self):
        for i in range(20):
            self.graph_dir.addVertex(i)
            self.sol_dir.addVertex(i)
            self.graph_ndir.addVertex(i)
            self.sol_ndir.addVertex(i)
            self.graph_dir.addVertex(chr(i+33))
            self.sol_dir.addVertex(chr(i+33))
            self.graph_ndir.addVertex(chr(i+33))
            self.sol_ndir.addVertex(chr(i+33))
        self.assertGraphEqual(self.graph_dir, self.sol_dir)
        self.assertGraphEqual(self.graph_ndir, self.sol_ndir)
        self.stop()

    def testAddEdge(self):
        for i in range(20):
            self.graph_dir.addVertex(i)
            self.sol_dir.addVertex(i)
            self.graph_ndir.addVertex(i)
            self.sol_ndir.addVertex(i)
        for i in range(20):
            for j in range(20):
                for g in [self.graph_dir, self.sol_dir, self.graph_ndir, self.sol_ndir]:
                    g.addEdge(i,j,i)
        self.assertGraphEqual(self.graph_dir, self.sol_dir, msg="edge adding not success")
        self.assertGraphEqual(self.graph_ndir, self.sol_ndir, msg="edge adding not success")
        for i in range(20):
            for j in range(20):
                for g in [self.graph_dir, self.sol_dir, self.graph_ndir, self.sol_ndir]:
                    g.addEdge(i,j,j)
        self.assertGraphEqual(self.graph_dir, self.sol_dir, msg="edge overriding not success")
        self.assertGraphEqual(self.graph_ndir, self.sol_ndir, msg="edge overriding not success")
        self.stop()

    def testRemoveVertex(self):
        self.setGraph()
        for i in range(30):
            for g in [self.graph_dir, self.sol_dir, self.graph_ndir, self.sol_ndir]:
                g.removeVertex(i)
            self.assertGraphEqual(self.graph_dir, self.sol_dir)
            self.assertGraphEqual(self.graph_ndir, self.sol_ndir)
        with self.assertRaises(KeyError, msg="key error not raised"):
            self.graph_dir.removeVertex(31)
        with self.assertRaises(KeyError, msg="key error not raised"):
            self.graph_ndir.removeVertex(31)
        self.stop()

    def testRemoveEdge(self):
        self.setGraph()
        for i in range(30):
            for j in range(30):
                for g in [self.graph_dir, self.sol_dir, self.graph_ndir, self.sol_ndir]:
                    g.removeEdge(i,j)
                self.assertGraphEqual(self.graph_dir, self.sol_dir)
                self.assertGraphEqual(self.graph_ndir, self.sol_ndir)
        with self.assertRaises(KeyError, msg="key error not raised"):
            self.graph_dir.removeEdge(-1,31)
        with self.assertRaises(KeyError, msg="key error not raised"):
            self.graph_ndir.removeEdge(-1,31)
        self.stop()
    
    def testBFS(self):
        self.setGraph()
        for i in range(30):
            self.assertCountEqual(self.graph_dir.BFS(1,i), self.sol_dir.BFS(1,i), msg="vertex searched in BFS not same")
            self.assertCountEqual(self.graph_ndir.BFS(1,i), self.sol_ndir.BFS(1,i), msg="vertex searched in BFS not same")
        with self.assertRaises(KeyError, msg="key error not raised"):
            self.graph_dir.BFS(1,31)
        with self.assertRaises(KeyError, msg="key error not raised"):
            self.graph_dir.BFS(-1,29)
        with self.assertRaises(KeyError, msg="key error not raised"):
            self.graph_ndir.BFS(1,31)
        with self.assertRaises(KeyError, msg="key error not raised"):
            self.graph_ndir.BFS(-1,29)
        self.stop()

    def testDFS(self):
        self.setGraph()
        for i in range(30):
            self.assertCountEqual(self.graph_dir.DFS(1,i), self.sol_dir.DFS(1,i), msg="vertex searched in DFS not same")
            self.assertCountEqual(self.graph_ndir.DFS(1,i), self.sol_ndir.DFS(1,i), msg="vertex searched in DFS not same")
        with self.assertRaises(KeyError, msg="key error not raised"):
            self.graph_dir.DFS(1,31)
        with self.assertRaises(KeyError, msg="key error not raised"):
            self.graph_dir.DFS(-1,29)
        with self.assertRaises(KeyError, msg="key error not raised"):
            self.graph_ndir.DFS(1,31)
        with self.assertRaises(KeyError, msg="key error not raised"):
            self.graph_ndir.DFS(-1,29)
        self.stop()

    def testDijkstra(self):
        self.setGraph()
        for i in range(30):
            for j in range(30):
                self.assertEqual(self.graph_dir.dijkstra(i,j), self.sol_dir.dijkstra(i,j))
                self.assertEqual(self.graph_ndir.dijkstra(i,j), self.sol_ndir.dijkstra(i,j))
        self.stop()

    def testMST(self):
        self.setGraph()
        with self.assertRaises(AttributeError, msg="MST attribute error not raised for directed graph"):
            self.graph_dir.MST()
        self.assertEqual(self.graph_ndir.MST(), self.sol_ndir.MST())
        self.stop()

    
    def testMix(self):
        self.setGraph()
        self.assertGraphEqual(self.graph_dir,self.sol_dir)
        self.assertGraphEqual(self.graph_ndir,self.sol_ndir)
        self.assertEqual(str(self.graph_dir), str(self.sol_dir))
        self.assertEqual(str(self.graph_ndir), str(self.sol_ndir))
        self.assertCountEqual(self.graph_dir.BFS(0,29), self.sol_dir.BFS(0,29), msg="vertex searched in BFS not same")
        self.assertCountEqual(self.graph_ndir.BFS(0,29), self.sol_ndir.BFS(0,29), msg="vertex searched in BFS not same")
        self.assertCountEqual(self.graph_dir.DFS(0,29), self.sol_dir.DFS(0,29), msg="vertex searched in DFS not same")
        self.assertCountEqual(self.graph_ndir.DFS(0,29), self.sol_ndir.DFS(0,29), msg="vertex searched in DFS not same")
        self.assertEqual(self.graph_dir.dijkstra(0,29), self.sol_dir.dijkstra(0,29), msg="dijkstra not same")
        self.assertEqual(self.graph_ndir.dijkstra(0,29), self.sol_ndir.dijkstra(0,29), msg="dijkstra not same")
        for i in range(5):
            self.graph_ndir.removeEdge(i*5+2,i*5+4)
        self.assertEqual(self.graph_ndir.MST(), self.sol_ndir.MST())

        self.stop()

    @unittest.skipIf(LOAD_TEST==False, "Load test disabled")
    def testLoad(self):
        for i in range(100000):
            self.graph_dir.addVertex(i)
        self.assertEqual(len(self.graph_dir), 100000)
        self.stop()

if __name__ == '__main__':
    unittest.main(verbosity=2)