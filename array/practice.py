''' 
Array Practice Problems
    by 游硯竹
    12/29/2020
DESCRIPTION:
    here are some basic array problems for you to practice 
TODO:
    1. read the problem carefully
    2. delete the "pass"
    3. fill in your solution
    4. go to test.py and run it
    5. fix your code if you does not pass the corresponding test
    6. try improve efficiency if possible (optional)
NOTE:
    1. ALL problems require you to return a NEW variable,
      so DO NOT modify the original input variables
    2. ALL sorted arrays should be in ASCENDING order
    3. feel free to make any helper methods
    4. it's totally fine to google the problems, but make sure
      you UNDERSTAND your code
    5. you are NOT allowed to use numpy module
    6. the answer key are in the solution.py file if needed
'''
# this is a helper method written for you, nothing needs to 
# be implemented in this part
#
# It returns a copy of the input array, so you can play with 
# the new array and not modifying the original input array
def copy(a):
    return [x for x in a]
    
##################################################################
# return the mean of the number array
# example: a=[1,2,3] -> 2
##################################################################
def arrMean(a):
    pass

##################################################################
# return the variance of the number array
# Note: you can use arrMean for short
# example: a=[1,2,3] -> 0.6666...
##################################################################
def arrVar(a):
    pass

##################################################################
# return an array with element of a in reversed order
# example: a=[1,2,3] -> [3,2,1]
##################################################################
def reverseArr(a):
    pass

##################################################################
# return the sum of number arrays a,b
# raise value error if length of a, b does not match
# format of raising error:
'''   
if (YOUR_CONDITION):
    raise ValueError
'''
# example: a=[1,2,3] b=[4,5,6] -> [5,7,9]
##################################################################
def sumArr(a, b):
    pass

##################################################################
# return the sorted elements of sorted number arrays a,b
# example: a=[1,2,4] b=[3,5,6]-> [1,2,3,4,5,6]
##################################################################
def sortTwoArr(a,b):
    pass

##################################################################
# return a sorted array with elements of a using bubble sort 
# example: a=[1,3,2,4] -> [1,2,3,4]
##################################################################
def bubbleSort(a):
    pass

##################################################################
# return a sorted array with elements of a using selection sort
# example: a=[1,3,2,4] -> [1,2,3,4]
##################################################################
def selectionSort(a):
    pass

##################################################################
# return a sorted array with elements of a using insertion sort
# example: a=[1,3,2,4] -> [1,2,3,4]
##################################################################
def insertionSort(a):
    pass