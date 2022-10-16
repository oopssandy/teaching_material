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

# this method will record the runtime of func at different array sizes
# NOTE: do NOT need to modify
# PARAMETERS:
#   func = the function to test
#   name = the name of the fuction
#   arguments(optional) = the number of arguments required for func,
#                         set to 1 by default
def recordRuntime(func, name, arguments=1):
    print("Running",name, end=" ")
    res = []
    for s in arrSize:
        inputs = makeInputs(s, arguments)
        start = datetime.now()
        func(*inputs)
        end = datetime.now()
        diff = end - start
        res.append(diff.total_seconds() * 1000)
        print(end=".")
    results[name] = res
    print("done (total",sum(res),"ms)")

# this method will make the desired input for func based 
# on given size, type, and number of arguments
# TODO: delete "pass" and implement this method so it can 
#       return the inputs that fit for the testing function
def makeInputs(size, arguments, type=None):
    pass
# example: 
'''
    out = []
    for i in range(arguments):
        out.append([0]*size)
    return out
'''

# TODO: call recordRuntime to test functions
# NOTE: don't forget to pass in the number of 
#       arguments if testing fuction requires
#       more than one argument
# example: 
'''
recordRuntime(bubbleSort, "bubbleSort")
recordRuntime(selectionSort, "selectionSort")
recordRuntime(insertionSort, "insertionSort")
'''

# plot results
for (key, val) in results.items():
    plt.plot(arrSize, val, marker=".", label=key)
plt.xlabel("Input Sizes")
plt.ylabel("Runtime (ms)")
plt.legend()
plt.show()

