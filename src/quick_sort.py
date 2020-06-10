def quick_sort(books):
    if len(books) <=1:
        return books
    else:
        pivot = books[0]
        lhs = [item for item in books[1:] if item<= pivot]
        print("Left hand Side", lhs)
        rhs = [item for item in books[1:] if item> pivot]
        print("Right hand Side", rhs)
        print("Books: ", books)
        return quick_sort(lhs) + [pivot] + quick_sort(rhs)
       
quick_sort([5,2,8,4,0,1,9,7])