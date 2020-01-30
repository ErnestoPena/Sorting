# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    print(arrA , arrB)
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    print("I am here", merged_arr)
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    #First two Edge cases, when arr is empty and array length iquals one
    if len(arr) == 0:
        return []
    elif len(arr) == 1:
        return arr
    else:
        splitted_list = [[item] for item in arr]
        initial_call = merge(splitted_list[0] , splitted_list[1])
        for i in range(2 , len(arr) +1):
            print(i)

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


merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])