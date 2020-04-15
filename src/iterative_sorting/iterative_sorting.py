test =  [1, 2, 8 , 140, 32, 99, 5, 9, 7, 1, 2, 5]
test_2 = [1, 2, 8 , 140, 32, 99, 5, 9, 7, 1, 2, 5]
test_3 = [1, 2, 8 , 140, 32, 99, 5, 9, 7, 1, 2, 5]
test_4 = [1, 2, 8 , 140, 32, 99, 5, 9, 7, 1, 2, 5]

def insertion_sort(arr):
    # Divide your hand into sorted on the left and unsorted on the right
    # Sorted is just the first element
    # then go card by card and move them into place.
    # Loop through all elements in unsorted...
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i  # j is our sliding index
        # Shift sorted to the right until correct position found
        while j > 0 and temp < arr[j - 1]:
            arr[j] = arr[j - 1]  # Slide over one element
            j -= 1
        # Insert at that position
        arr[j] = temp
    return arr

print("insertion", insertion_sort(test_3))

# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # cur_index = i - not necessary??
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        # loops through starting at i index till length of array. If value at arr[j] is smaller than the value at i index, the arr[j] becomes the new smallest index and it starts over??
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr

print("selection", selection_sort(test))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(len(arr) - 1):
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# def bubble_sort( arr ):
#     swaps = True
#     while swaps:
#         swaps = False
#         for i in range(len(arr) - 1):
#             if arr[i] > arr[i + 1]:
#                 arr[i], arr[i + 1] = arr[i + 1], arr[i]
#                 swaps = True
#     return arr

print("bubble", bubble_sort(test_2))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

# def loop_tester(arr):
#     for i in range(len(arr)):
#         for j in range(i, len(arr)):
#             print("i", i, "j", j)

# loop_tester(test_4)