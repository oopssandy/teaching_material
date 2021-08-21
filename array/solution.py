''' 
Array Practice Solutions
    by 游硯竹
    12/29/2020
'''
def checkNumbers(arr):
    return all(isinstance(x, (int, float)) for x in arr)

def copy(a):
    return [x for x in a]

def sumArr(a, b):
    if (len(a) != len(b)):
        raise ValueError
    return [sum(x) for x in zip(a, b) ]    

def arrMean(a):
    return sum(a)/len(a) 

def arrVar(a):
    m = arrMean(a)
    return sum((x - m) ** 2 for x in a) / len(a)

def reverseArr(a):
    l = len(a)
    return [a[l-i-1] for i in range(0,l)]

def sortTwoArr(a,b):
    result = []
    x = 0
    y = 0
    while(x<len(a) or y<len(b)):
        if (x >= len(a) or (y < len(b) and a[x] > b[y])):
            result.append(b[y])
            y+=1
        else:
            result.append(a[x])
            x+=1
    return result

def bubbleSort(a):
    arr = copy(a)
    n = len(arr) 
    for i in range(n-1): 
        for j in range(n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    return arr

def selectionSort(a):
    arr = copy(a)
    for i in range(len(arr)): 
        minIdx = i 
        for j in range(i+1, len(arr)): 
            if arr[minIdx] > arr[j]: 
                minIdx = j      
        arr[i], arr[minIdx] = arr[minIdx], arr[i] 
    return arr

def insertionSort(a):
    arr = copy(a)
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
    return arr

print(sortTwoArr([1,2,3], [-3,-2,-1]))