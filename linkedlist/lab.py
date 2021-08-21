''' 
Array Practice Unit Test
    by 游硯竹
    12/30/2020
DESCRIPTION:
    This is a template for investigating the functions you
    have implemented, it records their runtime and plot it
TODO:
    1. follow the TODOs
    2. read the instructions carefully
NOTE:
    You should finish implementing and testing ALL methods
    in practice.py before proceeding
'''
import matplotlib.pyplot as plt
from datetime import datetime
# TODO: change the "solution" to "practice"
from solution import *

# give the array of input sizes you want to test
# TODO: include appropriate numbers for testing
arrSize = [1, 10 ,20, 50, 100, 200, 500 ,1000, 2000, 5000, 10000]
results = {}
fL = LinkedList()
class Recorder:
    def __init__(self):
        self.setUp()
# those method will record the runtime of func at different
# input sizes or number of loops
# NOTE: do NOT need to modify
# PARAMETERS:
#   func = the function to test
#   name = the name of the fuction
#   arguments(optional) = the number of arguments required 
#                         for func, set to 1 by default
#   params(optional) = any additional parameters for setting 
#                      up inputs, set to None by default
    def recordSizeRuntime(self, func, name, arguments=1, *params):
        print("Running",name, end=" ")
        res = []
        for s in arrSize:
            inputs = self.makeInputs(s, arguments, *params)
            self.setUp()
            start = datetime.now()
            func(*inputs)
            end = datetime.now()
            diff = end - start
            res.append(diff.total_seconds() * 1000)
            print(end=".")
        results[name] = res
        print("done (total",sum(res),"ms)")

    def recordLoopRuntime(self, func, name, arguments=1, *params):
        print("Running",name, end=" ")
        res = []
        for s in arrSize:
            inputs = self.makeInputs(s, arguments, *params)
            self.setUp()
            # print(s)
            start = datetime.now()
            for i in range(s):
                func(*inputs)
            end = datetime.now()
            diff = end - start
            res.append(diff.total_seconds() * 1000)
            print(end=".")
        results[name] = res
        print("done (total",sum(res),"ms)")

# this method will make the desired input for func based 
# on given size, params, and number of arguments
# TODO: delete "pass" and implement this method so it can 
#       return the inputs that fit for the testing function
# NOTE: the returned inputs must be an array
    def makeInputs(self, size, arguments, *params):
        return [0]*arguments

# this method will set up needed variables before timing
# TODO: delete "pass" and implement this method so it can 
#       set up required variables for the testing function
    def setUp(self):
        self.L = LinkedList()
        while(len(fL)<max(arrSize)):
            fL.insert(0,0)

r = Recorder()  
# TODO: call r.recordSizeRuntime or r.recordLoopRuntime 
#       to test functions
# NOTE: don't forget to pass in the number of arguments 
#       if the testing fuction requires more than one 
#       argument
# example: 
# r.recordLoopRuntime(r.L.append, "append")
# r.recordLoopRuntime(r.L.index, "append")
r.recordLoopRuntime(r.L.insert, "insert", arguments=2)
r.recordLoopRuntime(fL.delete, "delete")


# plot results
for (key, val) in results.items():
    plt.plot(arrSize, val, marker=".", label=key)
plt.xlabel("Input Sizes")
plt.ylabel("Runtime (ms)")
plt.legend()
plt.show()