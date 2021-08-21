''' 
Graph Practice solution
    by 游硯竹
    1/22/2021
'''
import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from heap.solution import *
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
    def __init__(self, vertdict=None, edges=None, directed=True):
        self.vertdict = vertdict if vertdict is not None else {}
        self.edges = edges if edges is not None else {}
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
        if(not all(k in self.vertdict for k in (src,src))):
            raise KeyError
        if(dst not in self.vertdict[src]):
            self.vertdict[src].append(dst)
        self.edges[(src, dst)] = weight
        if (not self.DIRECTED):
            if(src not in self.vertdict[dst]):
                self.vertdict[dst].append(src)
            self.edges[(dst, src)] = weight

    # remove the edge from src to dst, do nothing 
    # if edge does not exist
    # raise KeyError if any vertices not exist
    # NOTE: remember to remove both edges if graph 
    #       is not directed
    # do not need to return
    def removeEdge(self, src, dst):
        if(src not in self.vertdict or dst not in self.vertdict):
            raise KeyError
        if(dst in self.vertdict[src]):
            self.vertdict[src].remove(dst)
            del self.edges[(src,dst)]
        if(not self.DIRECTED):
            if(src in self.vertdict[dst]):
                self.vertdict[dst].remove(src)
                del self.edges[(dst,src)]

    # add a new vertex to the graph, do nothing
    # if vertex with input label already exists
    # do not need to return
    def addVertex(self, label):
        if(label not in self.vertdict):
            self.vertdict[label] = []

    # remove the vertex with input label
    # raise KeyError if vertex not exist
    # NOTE: remember to remove associated edges
    # do not need to return
    def removeVertex(self, label):
        if(label not in self.vertdict):
            raise KeyError
        for v in self.vertdict.keys():
            self.removeEdge(v, label)
        del self.vertdict[label]

    # do a Breadth-first search and return searched 
    # verticies in the traversal from src to dst, 
    # return empty array if no path found
    # raise KeyError if any vertices not exist
    def BFS(self, src, target):
        if(src not in self.vertdict or target not in self.vertdict):
            raise KeyError
        visited = [src]
        if(src == target and (src,src) in self.edges):
            return visited
        queue = [src]
        while(queue):
            v = queue.pop(0)
            for u in self.vertdict[v]:
                if(u not in visited):
                    queue.append(u)
                    visited.append(u)
                    if(u == target):
                        return visited
        return []

    # do a Depth-first search and return searched 
    # verticies in the traversal from src to dst, 
    # return empty array if no path found
    # raise KeyError if any vertices not exist
    def DFS(self, src, target):
        if(src not in self.vertdict or target not in self.vertdict):
            raise KeyError
        if(src == target and (src,src) in self.edges):
            return [src]
        visited = []
        self.DFSrecurr(src, target, visited)
        if(visited[-1] == target):
            return visited
        return []
    
    def DFSrecurr(self, v, target, visited):
        visited.append(v)
        for u in self.vertdict[v]:
            if(u not in visited):
                self.DFSrecurr(u, target, visited)
            if (target in visited):
                return visited

    # run Dijkstra's algorithm and return the shortest 
    # path from src to dst, return empty array if no 
    # path found
    # raise KeyError if any vertices not exist
    # NOTE: assume graph with no negative weight
    def dijkstra(self, src, target):
        if(src not in self.vertdict or target not in self.vertdict):
            raise KeyError
        dist = {}
        queue = MinHeap()
        # preparing pirority queue and dist/ prev dictionary
        for v in self.vertdict.keys():
            if(v != src):
                dist[v] = (sys.maxsize, None)
                queue.push((sys.maxsize, v))
            else:
                dist[v] = (0, None)
                queue.push((0, v))
        # loop start
        while(not queue.isEmpty()):
            (u_weight, u) = queue.pop()
            # print(u,"dist",u_weight)
            # target found
            if(u == target):
                break
            for v in self.vertdict[u]: 
                alt = dist[u][0] + self.edges[(u, v)]
                old = dist[v][0]
                # print("\t",v,"weight",self.edges[(u, v)])
                # print("\t alt",alt,"old",old)
                # replacing dist and reorder heap
                if(alt < old):          
                    i = queue.body.index((old, v))
                    queue.body[i] = (alt, v)
                    p = queue.parent(i)
                    while(p>=0 and queue.body[i]<queue.body[p]):
                        queue.body[i], queue.body[p] = queue.body[p], queue.body[i]
                        i, p = p, queue.parent(p)    
                    dist[v] = (alt, u)
        if(dist[target][1]):
            result = []
            prev = target
            while(prev is not None):
                result.insert(0, prev)
                prev = dist[prev][1]
            return result
        return []

    # print the minimum spanning tree and return total 
    # weight of it
    # raise AttributeError if the graph is directed
    # NOTE: use Kruskal’s MST algorithm
    def MST(self):
        if(self.DIRECTED):
            raise AttributeError("directed 'Graph' object has no attribute 'MST'")
        cost = 0
        i = 0
        l = len(self.vertdict.keys())
        parents = {}
        queue = MinHeap()
        for v in self.vertdict.keys():
            for u in self.vertdict[v]:
                queue.push((self.edges[v, u], (v, u)))
            parents[v] = None
        print("edges in MST")
        while(not queue.isEmpty() and i < l-1):
            w, (v, u) = queue.pop()
            x = self.findRoot(parents, v)
            y = self.findRoot(parents, u)
            if(x != y):
                parents[x] = y
                cost += w
                i += 1
                print(v, "--", u, "==", w)
        return cost

    def findRoot(self, parents, v):
        p = v
        while(parents[p] is not None):
            p = parents[p]
        return p

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