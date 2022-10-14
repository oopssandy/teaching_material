''' 
Array Practice Problems-2
    by 游硯竹
    12/30/2020
DESCRIPTION:
    here are some more advanced array problems for you to practice 
TODO:
    1. read the problem carefully
    2. delete the "pass"
    3. fill in your solution
    4. go to test_2.py and run it
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
    6. the answer key are in the solution_2.py file if needed
'''
# this is a helper method written for you, nothing needs to 
# be implemented in this part
#
# It returns a copy of the input array, so you can play with 
# the new array and not modifying the original input array
def copy(a):
    return [x for x in a]
    
##################################################################
# return the maximum sum of any continuous subarray of a
# hint: consider dynamic programming 
# example: a=[1,2,1,-5,3] -> 4 (from subarray [1,2,1])
##################################################################
def maxSubSum(a):
    pass

##################################################################
# return the index of first duplicate element in a, return -1 if 
# not found
# hint: use a set or another array
# example: a=[1,2,1,3] -> 2; a=[1,2,3] -> -1
##################################################################
def firstDuplicate(a):
    
    for i in a :
        if a.count(i) > 1
        re

##################################################################
# return the count of the maximum number of duplicates in a
# hint: use a dictionary
# example: a=[1,1,1,2,2,3] -> 3
##################################################################
def maxDuplicate(a):
    pass

##################################################################
# return new array that has elements of a and reordered following 
# the index stored in b
# in other words, for element of a at index i, the element of b 
# at index i will be its new index in the array to return
# example: a=[11,22,33] b=[2,1,0]-> [33,22,11];
#          a=[33,44,55,22,11] b=[2,3,4,1,0]-> [11,22,33,44,55]
##################################################################
def reorderArr(a,b):
    pass

##################################################################
# return a sorted array with elements of a using merge sort 
# example: a=[1,3,2,4] -> [1,2,3,4]
##################################################################
def mergeSort(a):
    pass

##################################################################
# return a sorted array with elements of a using heap sort
# example: a=[1,3,2,4] -> [1,2,3,4]
##################################################################
def heapSort(a):
    pass
