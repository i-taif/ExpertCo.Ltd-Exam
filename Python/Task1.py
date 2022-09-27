from typing import List
def quicksort(arr: List) -> List:
    '''
    this func to sorts it alphabetically withou using sort(), by using recursion
    '''
    if not arr:
        return []
    return (quicksort([x for x in arr[1:] if x <  arr[0]])
            + [arr[0]] +
            quicksort([x for x in arr[1:] if x >= arr[0]]))

print(quicksort(['c','ad','as','y','p'])) #output: ['ad', 'as', 'c', 'p', 'y']
