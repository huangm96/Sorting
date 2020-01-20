# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    # if arr has 1 or 0 items, return arr
    if len(arr) < 2:
        return arr
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        j = i + 1
        next_smallest_index = j
        for j in range(i + 2, len(arr)):
            
            if arr[next_smallest_index] > arr[j]:
                next_smallest_index = j
        # TO-DO: swap
        if arr[cur_index] > arr[next_smallest_index]:
            temp = arr[cur_index]
            arr[cur_index] = arr[next_smallest_index]
            arr[next_smallest_index]=temp
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr