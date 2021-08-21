''' 
Array Practice Solutions
    by 游硯竹
    12/29/2020
'''
def copy(a):
    return [x for x in a]
    
##################################################################
# return the maximum sum of any continuous subarray of a
# hint: consider dynamic programming 
# example: a=[1,2,1,-5,3] -> 4 (from subarray [1,2,1])
##################################################################
def maxSubSum(a):
    dp = [0]*len(a)
    dp[0] = a[0]
    for i in range(1,len(a)):
         dp[i] = max(dp[i-1]+a[i],a[i])
    return max(dp)

##################################################################
# return the index of first duplicate element in a, return -1 if 
# not found
# hint: use a set or another array
# example: a=[1,2,1,3] -> 2; a=[1,2,3] -> -1
##################################################################

def firstDuplicate(a):
    checked = []
    for i in range(len(a)):
        if (a[i] in checked):
            return i
        checked.append(a[i])
    return -1
print(firstDuplicate([1,2,1,3]))
##################################################################
# return the count of the maximum number of duplicates in a
# hint: use a dictionary
# example: a=[1,1,1,2,2,3] -> 3
##################################################################
def maxDuplicate(a):
    count = {}
    for x in a:
        if (x not in count):
            count[x] = 1
        else:
            count[x] += 1
    return max([val for key, val in count.items()])

##################################################################
# return new array that has elements of a and reordered following 
# the index stored in b
# in other words, for element of a at index i, the element of b 
# at index i will be its new index in the array to return
# example: a=[11,22,33] b=[2,1,0]-> [33,22,11];
#          a=[33,44,55,22,11] b=[2,3,4,1,0]-> [11,22,33,44,55]
##################################################################
def reorderArr(a,b):
    out = [0]*len(a)
    for i in range(len(a)):
        out[b[i]] = a[i]
    return out

##################################################################
# return a sorted array with elements of a using merge sort 
# example: a=[1,3,2,4] -> [1,2,3,4]
##################################################################
def mergeSort(a):
    arr = copy(a)
    return mSort(arr,0,len(arr)-1) 

def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 
    L = [0] * (n1) 
    R = [0] * (n2) 
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
    i =  j = 0  
    k = l 
    while (i < n1 and j < n2): 
        if (L[i] <= R[j]): 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
    while (i < n1): 
        arr[k] = L[i] 
        i += 1
        k += 1
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1

def mSort(arr,l,r): 
    if l < r: 
        m = (l+(r-1))//2
        mSort(arr, l, m) 
        mSort(arr, m+1, r) 
        merge(arr, l, m, r) 
    return arr
  
##################################################################
# return a sorted array with elements of a using heap sort
# example: a=[1,3,2,4] -> [1,2,3,4]
##################################################################
def heapSort(a):
    arr = copy(a)
    n = len(arr) 
    for i in range(n // 2 - 1, -1, -1): 
        makeHeap(arr, n, i) 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]   # swap 
        makeHeap(arr, i, 0) 
    return arr

def makeHeap(arr, n, i): 
    largest = i 
    l = 2 * i + 1 
    r = 2 * i + 2 
    if (l < n and arr[i] < arr[l]): 
        largest = l 
    if (r < n and arr[largest] < arr[r]): 
        largest = r 
    if (largest != i): 
        arr[i], arr[largest] = arr[largest], arr[i]
        makeHeap(arr, n, largest) 

# import random
# random.seed(0)
# array = [i for i in range(30)]
# random.shuffle(array)
# print(array)
# print(mergeSort(array))
# print(heapSort(array))
# a=[11,22,33]
# b=[2,1,0]
# print(reorderArr(a,b))
# a=[33,44,55,22,11] 
# b=[2,3,4,1,0]
# print(reorderArr(a,b))
# print(maxSubSum([1,2,1,-5,3]))
# print(firstDuplicate([1,2,1,3]))
# print(firstDuplicate([1,2,3]))
# print(maxDuplicate([1,1,1,2,2,3]))