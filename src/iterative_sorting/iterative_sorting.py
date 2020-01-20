# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    # if arr has 1 or 0 item, return arr
    if len(arr) < 2:
        return arr
    # elif arr has 2 items, just compare these two items
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            temp = arr[1]
            arr[1] = arr[0]
            arr[0] = temp
        else:
            return arr
    # else
    # loop through n-1 elements
    else:
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
    # if arr has 1 or 0 item, return arr
    if len(arr) < 2:
        return arr
    # elif arr has 2 items, just compare these two items
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            temp = arr[1]
            arr[1] = arr[0]
            arr[0] = temp
        else:
            return arr
    # else
    else:
        swap_time = 1
        # while swap times equals to 0, sorting end, return arr
        while swap_time > 0:
            swap_time = 0
            # loop through n-1 items
            for i in range(0, len(arr) - 1):
                # compare arr[i] and arr[i+1]
                if arr[i] > arr[i + 1]:
                    swap_time += 1
                    # swap
                    temp = arr[i + 1]
                    arr[i + 1] = arr[i]
                    arr[i] = temp
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
