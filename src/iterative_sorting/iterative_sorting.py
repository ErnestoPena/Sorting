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

    return print (arr)


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

#selection_sort([4,2,67,34,23,56,23])    