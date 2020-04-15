test =  [1, 2, 8 , 140, 32, 99, 5, 9, 7, 1, 2, 5]

def quicksort(arr):
    # Base Case
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    # Separate all values smaller and larger than pivot
    smaller = []
    larger = []
    for i in range(1, len(arr)):
    # Sort smaller and larger
        if arr[i] <= pivot:
            smaller.append(arr[i])
        else:
            larger.append(arr[i])
    smaller = quicksort(smaller)
    larger = quicksort(larger)
    # Concatenate smaller + pivot + larger
    return smaller + [pivot] + larger

# print("Quick sort", quicksort(test))

# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # estimate length of both arrays combined
    elements = len( arrA ) + len( arrB )
    # print(elements)
    merged_arr = [0] * elements
    # TO-DO
    # pointers - will increase depending on value of index by 1
    a = 0
    b = 0
    # for i in range(elements):
    for i in range(elements):
        if len(arrA) <= a:
            merged_arr[i] = arrB[b]
            b = b + 1
        elif len(arrB) <= b:
            merged_arr[i] = arrA[a]
            a = a + 1
        elif arrB[b] < arrA[a]:
            merged_arr[i] = arrB[b]
            b = b + 1
        else:
            merged_arr[i] = arrA[a]
            a = a + 1

    return merged_arr

# def merge_test(left, right):
#     merged_arr = []
#     left_i = 0
#     right_i = 0

#     while len(left) > left_i and len(right) > right_i:
#         if left[left_i] < right[right_i]:
#             merged_arr.append(left[left_i])
#             left_i = left_i + 1
#         else:
#             merged_arr.append(right[right_i])
#             right_i = right_i + 1

#     return merged_arr


# print(merge(array_a, array_b))

# TO-DO: implement the Merge Sort function below USING RECURSION
"""
1. While your data set contains more than one item, split it in half
2. Once you have gotten down to a single element, you have also *sorted* that element 
   (a single element cannot be "out of order")
3. Start merging your single lists of one element together into larger, sorted sets
4. Repeat step 3 until the entire data set has been reassembled
"""

def merge_sort( arr ):
    # TO-DO
    # Base Case
    if len(arr) <= 1:
        return arr
    else:
        mid_point = len(arr) // 2
        left_arr = arr[mid_point:]
        right_arr = arr[:mid_point]

    return merge(merge_sort(left_arr),merge_sort(right_arr))

test_1 = [1, 9, 3, 2, 1, 5]

print(merge_sort(test_1))

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
