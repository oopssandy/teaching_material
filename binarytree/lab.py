''' 
Binary Search Tree Lab
    by 游硯竹
    1/30/2021
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
# TODO: change the "solution" to "practice"
from solution import *
import matplotlib.pyplot as plt
from random import random, seed
from datetime import datetime
import sys
sys.setrecursionlimit(15000)
seed(0)

# TODO: give a proper title for the plot
TITLE = "BST lab"
# give the array of input sizes you want to test
# TODO: include appropriate numbers for testing
arrSize = [i*50 for i in range(20)]
results = {}

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
def recordSizeRuntime(func, name, arguments=1, *params):
    print("Running",name, end=" ")
    res = []
    for n in arrSize:
        inputs = makeInputs(n, arguments, *params)
        start = datetime.now()
        func(*inputs)
        end = datetime.now()
        diff = end - start
        res.append(diff.total_seconds() * 1000)
        print(end=".")
    results[name] = res
    print("done (total",sum(res),"ms)")

def recordLoopRuntime(func, name, arguments=1, *params):
    print("Running",name, end=" ")
    res = []
    for n in arrSize:
        inputs = makeInputs(n, arguments, *params)
        start = datetime.now()
        for i in range(n):
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
def makeInputs(size, arguments, *params):
    B = BST()
    for i in range(size):
        if params and params[0]=="random":
            B.insert(random())
        else:
            B.insert(i+1)
    return [B, size]

# TODO: define your wrapper function here and then
#       call r.recordSizeRuntime or r.recordLoopRuntime 
#       to test functions
# NOTE: don't forget to pass in the number of arguments 
#       if the testing fuction requires more than one 
#       argument

# wrapper functions, expect same inputs and call methods
def insert_zero(B, n):
    B.insert(0)

# pass in wrapper functions, to record
recordSizeRuntime(insert_zero,"insert zero")
recordSizeRuntime(insert_zero,"insert zero random", 1, "random")

# plot results
for (key, val) in results.items():
    plt.plot(arrSize, val, marker=".", label=key)
plt.xlabel("Input Sizes")
plt.ylabel("Runtime (ms)")
plt.legend()
plt.savefig(f"{TITLE}.png")
plt.show()