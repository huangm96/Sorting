import random
l = list(range(10))
random.shuffle(l)
[7, 9, 6, 2, 5, 8, 4, 0, 3, 1]
# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    print("ArrA", arrA)
    print("ArrB", arrB)
    a_index = 0
    b_index = 0
    # TO-DO
    for i in range(0, len(merged_arr)):
        if a_index == len(arrA):
            for n in range(a_index+b_index, len(merged_arr)):
                merged_arr[n] = arrB[b_index]
                b_index += 1
        elif b_index == len(arrB):
            for n in range(a_index+b_index, len(merged_arr)):
                merged_arr[n] = arrA[a_index]
                a_index += 1
        # find the smaller number, put the smaller number in the merged_arr, and the index of the smaller number array +1    
        elif arrA[a_index] >= arrB[b_index]:
            merged_arr[i] = arrB[b_index]
            b_index += 1
        elif arrA[a_index] < arrB[b_index]:
            merged_arr[i] = arrA[a_index]
            a_index += 1
    print("merged_arr", merged_arr)        
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    print(arr)
    if len(arr) <= 1:
        return arr
    left = merge_sort(arr[0: len(arr) // 2])
    right = merge_sort(arr[len(arr) // 2 :])
    arr = merge(left, right)
    return arr


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



