# TO-DO: Complete the selection_sort() function below 
"""
The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order)
from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.

In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.
"""
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
      cur_index = i
      smallest_index = cur_index
      # TO-DO: find next smallest element
      # (hint, can do in 3 loc) 
      for j in range(cur_index, len(arr)):  
            if arr[j] < arr[smallest_index]:  
                smallest_index = j 
      # TO-DO: swap
      temp_index = arr[cur_index] 
      arr[cur_index] = arr[smallest_index] 
      arr[smallest_index] = temp_index  
    
    return arr

# TO-DO:  implement the Bubble Sort function below
"""
Bubble Sort is the simplest sorting algorithm that works by repeatedly 
swapping the adjacent elements if they are in wrong order.
"""
def bubble_sort( arr ):
    n = len(arr)   
    for i in range(n):    
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]   # swap here

    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr