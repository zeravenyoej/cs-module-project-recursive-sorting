# def countdown_to_one(n):
#     if n == 0: 
#         return
#     print(n)
#     countdown_to_one(n-1)

# print(countdown_to_one(5))

# def sum_list(items):
#     if len(items) == 1:
#         return items[0]
#     else:
#         return items[0] + sum_list(items[1:])

# 0, 1....1, 2, 3, 5, 8, 13, 21, 34
#  what is the base case?
#  what is the recursive case?
#  how does it move towards the base case

# def naive_fibonacci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     n_minus_1 = naive_fibonacci(n-1)
#     n_minus_2 = naive_fibonacci(n-2)
#     return n_minus_1 + n_minus_2

def quicksort(data):  
    # base case - check it data has 1 or 0 elements
    if len(data) <= 1:
        return data

    # partition the data
    # start by choose a pivot (choose the first item in the list)
    pivot = data[0]

    # we need to create storage for the LHS and RHS
    left = []
    right = []

    # we need to loop through each item
    for current in data[1:]:

        # if it's smaller or equal, add to LHS storage
        if current <= pivot:
            left.append(current)
        
        #  if it's bigger, add to RHS storage
        else: 
            right.append(current)

    # recursive case - recursively quick sort LHS and RHS until.....
    return quicksort(left) + [pivot] + quicksort(right)