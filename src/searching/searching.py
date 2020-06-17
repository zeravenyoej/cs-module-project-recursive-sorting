def binary_search(arr, target, start, end):
    low = start
    high = end
    mid = (low + high) // 2

    if low > high:
        return -1

    if arr[mid] == target:
        return arr.index(target)

    if arr[mid] < target:
        low = mid + 1
        return binary_search(arr, target, low, high)

    if arr[mid] > target:
        high = mid - 1
        return binary_search(arr, target, low, high)



# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    pass


# # Write an iterative implementation of Binary Search
# def binary_search(arr, target):
#     low = 0 
#     high = len(arr) - 1
#     while low <= high:
#         middle = (low + high) // 2
#         if target < arr[middle]:
#             high = middle - 1
#         elif target > arr[middle]:
#             low = middle + 1
#         else:
#             return middle


#     return -1  # not found
