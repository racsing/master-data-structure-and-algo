
def swap(arr, x, y):
    temp =  arr[x]
    arr[x] = arr[y]
    arr[y] = temp

#-------------------------
# 1. SELECTION SORT
#-------------------------
def selection_sort(arr, n):
    print(arr)
    for i in range(n-1):
        mini = i
        for j in range(i+1, n):
            if arr[mini] > arr[j]:
                mini = j
        swap(arr, mini, i)
        print(arr)

#-------------------------
# 2. BUBBLE SORT
#-------------------------
def bubble_sort(arr, n):
    print(arr, n)
    for i in range(n,0,-1):
        swapped = False
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                print(arr)
        if not swapped:
            break

#--------------------------     
# 3. INSERTION SORT
#--------------------------
def insertion_sort(arr, n):
    for i in range(1, n):
        current = arr[i]
        index_at = i
        for j in range(i-1, -1, -1):
            if current < arr[j]:
                index_at = j
                arr[j+1] = arr[j]
            else:
                break
        arr[index_at] = current
    print(arr)

# ---------------------------
# 4. MERGE SORT
#----------------------------
def merge(arr, low, mid, high):
    i = low
    j = mid+1
    result = []
    while i <= mid and j <= high: 
        if arr[i] <= arr[j]:
            result.append(arr[i])
            i+=1
        else:
            result.append(arr[j])
            j+=1

    while i <= mid:
        result.append(arr[i])
        i+=1
    while j <= high:
        result.append(arr[j])
        j+=1
    for k in range(len(result)):
        arr[low+k] = result[k]


def merge_sort(arr, low, high):
    if low >= high:
        return
    mid = low + (high-low) // 2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid+1, high)
    merge(arr, low, mid, high)

#---------------------------
# 5. QUICK SORT
#---------------------------

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i+=1
            swap(arr, i, j)
            print(arr, pivot)
    swap(arr, i+1, high)
    print(arr, pivot)
    return i+1

def partition_fast(arr, low, high):
    pivot = arr[low]
    i = low
    j = high



def quick_sort(arr, low, high):
    if low >= high:
        return
    
    pi = partition(arr, low, high)
    quick_sort(arr, low, pi-1)
    quick_sort(arr, pi+1, high)


#---------------------------
# INPUT     
#---------------------------
arr1 = [ 7, 12, 9, 11, 3]
arr2 = [1,2,3,4,5]
arr3 = [3, 7, 6, -10, 15, 23.5, 55, -13]
arr4 = [20,2,7,12,15,1,6,8]

quick_sort(arr4, 0, len(arr4)-1)
merge_sort(arr3, 0, len(arr3)-1)
insertion_sort(arr1, 5)
bubble_sort(arr1, 5)
selection_sort(arr1, 5)
print("result: ", arr4)
                
