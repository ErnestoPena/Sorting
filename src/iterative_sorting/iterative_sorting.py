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
    #Edge Case
    if arr == []:
        new_arr = []
        return new_arr

    #Get the Maximum and Minimum
    minimum = min(arr)
    maximum = max(arr)

    #Creating new array to avoid modifying the function argument
    new_arr = []

    if minimum > -1 and maximum > -1:

        #Create Array for placeholding the counts. Array of zero values
        list_placeholder = [0] * (maximum+1)
        for i in range(0, len(arr)):
            list_placeholder[arr[i]] = arr.count(arr[i])
        '''Filtering to reduce next iteration to the minimum.
           You can have a range going from 1 to 1,000,000 but with a lot of empty values in between  
           Eliminating all zero values from list_placeholder.
           Filtered array structure [[value , quantity] , [value, quantity] , [value...., quantity...]]  
           Value is list_placeholder index and quantity comes from list_placeholder value   
        '''
        filtered_arr = [list((item, list_placeholder[item])) for item in range(len(list_placeholder)) if list_placeholder[item] != 0]
        #The beef of the problem. Ugh.. looping again...
        build_single_component = []
        for i in range(len(filtered_arr)):
            build_single_component = [filtered_arr[i][0]]*filtered_arr[i][1]
            new_arr.extend(build_single_component)  
    else:
        return "Error, negative numbers not allowed in Count Sort"          
    return new_arr




#count_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])    

