''' 
Graph Practice practice
    by 游硯竹
    1/21/2021
DESCRIPTION:
    let's implement min graph for fun!!! (･ω･)b
TODO:
    1. read the instructions carefully
    2. delete the "pass"
    3. implement the method
    4. go to test.py and run it (may take a few minutes for load test)
    5. fix your code if you does not pass the corresponding test
    6. try improve efficiency if possible (optional)
NOTE:
    1. feel free to make any helper methods
    2. it's totally fine to google the problems, but make sure
      you UNDERSTAND your code
    3. the answer key are in the solution.py file if needed
    4. this file will import your heap practice, make sure 
      relative path to heap practice is "../heap/practice.py"
      and it is CORRECT before you start 
'''
import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from heap.practice import *

class Graph:
    # this is the constructor for the graph
    # initially the graph is empty, with no
    # verticies and no edges
    # NOTE: by default, it will construct a
    #       weighted, directed graph
    # HINT: the keys of verdict are vertecies
    #       and the values pairs are edges
    # example: 
    #   vertex A with distance 2 edge to B would be
    #   -> verdict["A"]=["B"], edges[("A","B")]=2
    # do not need to modify
    def __init__(self, vertdict={}, edges={}, directed=True):
        self.vertdict = vertdict
        self.edges = edges
        self.DIRECTED = directed

    # return the string represents the current graph
    # do not need to modify
    def __str__(self):
        return str(self.vertdict)
    
    # return the amount of vertices
    # do not need to modify
    def __len__(self):
        return len(self.vertdict.keys())

    # add an edge from src to dst with input 
    # weight, override the weight if an edge 
    # from src to dst already exists
    # raise KeyError if any vertices not exist
    # NOTE: remember to make the edge bidirectional
    #       if graph is not directed
    # do not need to return
    def addEdge(self, src, dst, weight):
        pass

    # remove the edge from src to dst, do nothing 
    # if edge does not exist
    # raise KeyError if any vertices not exist
    # do not need to return
    def removeEdge(self, src, dst):
        pass
    
    # add a new vertex to the graph, do nothing
    # if vertex with input label already exists
    # do not need to return
    def addVertex(self, label):
        pass

    # remove the vertex with input label
    # raise KeyError if vertex not exist
    # NOTE: remember to remove associated edges
    # do not need to return
    def removeVertex(self, label):
        pass

    # do a Breadth-first search and return searched 
    # verticies in the traversal from src to dst, 
    # return empty array if no path found
    # raise KeyError if any vertices not exist
    def BFS(self, src, target):
        pass

    # do a Depth-first search and return searched 
    # verticies in the traversal from src to dst, 
    # return empty array if no path found
    # raise KeyError if any vertices not exist
    def DFS(self, src, target):
        pass

    # run Dijkstra's algorithm and return the shortest 
    # path from src to dst, return empty array if no 
    # path found
    # raise KeyError if any vertices not exist
    # NOTE: assume graph with no negative weight
    def dijkstra(self, src, target):
        pass

    # print the minimum spanning tree and return total 
    # weight of it
    # raise AttributeError if the graph is directed
    # NOTE: use Kruskal’s MST algorithm
    def MST(self):
        raise AttributeError("directed 'Graph' object has no attribute 'MST'")

# self test(uncomment to run)

# g = Graph(directed=False)
# for i in range(6):
#     g.addVertex(i)
# print(len(g)) #expect 6
# g.addEdge(1,1,1)
# g.addEdge(1,3,1)
# g.addEdge(1,2,1)
# g.addEdge(3,4,1)
# g.addEdge(4,5,1)
# g.addEdge(2,0,1)
# g.addEdge(0,4,1)
# print(g) #expect {0: [2, 4], 1: [3, 2], 2: [1, 0], 3: [1, 4], 4: [3, 5, 0], 5: [4]}
# print(g.BFS(1,5)) #expect [1, 3, 2, 4, 0, 5]
# print(g.BFS(1,1)) #expect [1]
# print(g.DFS(1,5)) #expect [1, 3, 4, 5]
# print(g.DFS(1,1)) #expect [1]
# print(g.dijkstra(1,5)) #expect [1, 3, 4, 5]
# g.addEdge(0,4,10)
# print(g.dijkstra(5,2)) #expect [5, 4, 3, 1, 2]
# g.addEdge(0,2,100)
# print(g.MST()) #expect 14, including edge 1 -- 2, 1 -- 3, 3 -- 4, 4 -- 5, 0 -- 4

# 1 - 3 - 4 - 5
#  \     /
#   2 - 0