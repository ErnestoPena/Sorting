def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = []#[0] * elements
    
    longest_array= []
    if len(arrA) > len(arrB):
        longest_array = arrA
        shortest_array = arrB
    else:
        longest_array = arrB
        shortest_array = arrA    

    # COUNTER FOR ARRAY
    i = 0 
    for array_item in longest_array:
        if len(shortest_array) >= i:
            if array_item <= shortest_array[i]: 
                merged_arr.append(array_item)
            else:
                merged_arr.append(shortest_array[i])
        else:
            merged_arr.append(array_item)        
        i=i+1

    return merged_arr

merge( [1,3,6,9,23,34,45], [2,5,15,24,44,55] )


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