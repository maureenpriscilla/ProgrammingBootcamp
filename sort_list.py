"""
This function sorts by comparing adjacent pairs of elements in the list, if the element's value
in the smaller index is larger than the element's value in the larger index the function will swap
their values and then move to the next pairs. This process continues until the largest element in the list
"bubbles up" to the highest position possible in the list and continues looping until the next largest element is
in the next highest position, hence in the end the list will be in ascending order when the loop stop iterating.
The algorithm used in this function is known as the bubble sort algorithms.
"""

def sort_list(lst): #this function uses bubble sort algorithm
    for i in range(0, len(lst)-1): #loop for len(lst) times (for every highest position)
        for j in range(1, len(lst)-i): #loop for len(lst)-i-1 times (to move the largest element to the highest position possible)
            if lst[j-1] > lst[j]: #check if element in index j-1 (smaller index) is larger than element in index j (larger index)
                lst[j], lst[j-1] = lst[j-1], lst[j] #swap the element in index j and j-1
    return lst #return the sorted lst in accending order


#test cases
print(sort_list([2, 4, 8, 6, 3, 1, 9, 7, 10, 5])) #random order list
print(sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) #accending order list
print(sort_list([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) #deccending order list