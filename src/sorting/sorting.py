
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements

    a_index = 0
    b_index = 0
    sorted_index = 0

    while a_index<len(arrA) and b_index<len(arrB):
        if arrA[a_index] > arrB[b_index]:
            merged_arr[sorted_index] = arrB[b_index]
            b_index += 1
            sorted_index += 1
        elif arrA[a_index] < arrB[b_index]:
            merged_arr[sorted_index] = arrA[a_index]
            a_index+= 1
            sorted_index += 1

    merged_arr = merged_arr[:sorted_index]

    if a_index< len(arrA):
        merged_arr = merged_arr + arrA[a_index:]
    if b_index < len(arrB):
        merged_arr = merged_arr + arrB[b_index:]

    return merged_arr



def merge_sort( arr ):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    arr = merge(left, right)

    return arr


# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    pass


def merge_sort_in_place(arr, l, r):
    pass

