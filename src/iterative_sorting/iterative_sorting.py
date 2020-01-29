# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    for i in range(0, len(arr)-1):
        current_value = arr[i]
        flag = False
        for j in range(i+1 , len(arr)):
            if arr[j] < current_value:
                 flag = True
                 current_value = arr[j]
                 index_to_swap = j
        if flag:         
            arr[index_to_swap] = arr[i]         
            arr[i] = current_value 
    return arr




# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    finish_loop = True
    array_length = len(arr)
    while finish_loop:
        finish_loop = False
        for i in range(0, array_length - 1):
            left_value , right_value = arr[i] , arr[i+1]
            if left_value > right_value:
                arr[i] , arr[i+1] = right_value , left_value 
                finish_loop = True
        array_length = array_length -1 
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

bubble_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])    