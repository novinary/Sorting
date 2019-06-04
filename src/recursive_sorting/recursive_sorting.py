from random import randint
# TO-DO: complete the helper function below to merge 2 sorted arrays
# No need to pick a index and split as arrA and arrB are already sorted
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements

    a = 0
    b = 0
    # compare the first element of each list
    for i in range(0, elements):
        # merge all elements in arrA
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1    
        # merge all elements in arrB
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        # add to final array as next element in arrA must be smaller
        elif arrA[a] < arrB[b]: 
            merged_arr[i] = arrA[a]
            a += 1
        # add it to final array as next element in arrB must be smaller
        else: 
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) > 1:
        # slice syntax to get the left half of the list.
        left = merge_sort( arr[0 : len(arr) // 2 ])    #using floor division operator to round down incase of odd number of items in the list 
        right = merge_sort( arr[len(arr) // 2: ])
        arr = merge(left, right)
    return arr

# Testing my merge_sort function 
# Generate random numbers where size is 10 and numbers no bigger than 50
def create_random_array(size = 10, max = 50):
    return [randint(0, max) for _ in range(size)]

test = create_random_array()
print(test)
result = merge_sort(test)
print(result)

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
