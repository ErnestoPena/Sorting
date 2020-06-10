def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements       
    count_a, count_b = 0 , 0
    
    for i in range( 0, elements ):
        if count_a >= len(arrA):    
            merged_arr[i] = arrB[count_b]
            count_b += 1

        elif count_b >= len(arrB):  
            merged_arr[i] = arrA[count_a]
            count_a += 1

        elif arrA[count_a] < arrB[count_b]:  
            merged_arr[i] = arrA[count_a]
            count_a += 1

        else:  
            merged_arr[i] = arrB[count_b]
            count_b += 1

    return merged_arr


def merge_sort( arr ):
    if len( arr ) > 1:
       left_array = merge_sort( arr[ 0 : len( arr ) // 2 ] )
       right_array = merge_sort( arr[ len( arr ) // 2 : ] )
       arr = merge( left_array, right_array ) 
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