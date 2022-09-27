
from typing import List
def quicksort(arr: List) -> List:
    if not arr:
        return []
    return (quicksort([x for x in arr[1:] if x <  arr[0]])
            + [arr[0]] +
            quicksort([x for x in arr[1:] if x >= arr[0]]))

print(quicksort(['c','ad','as','y','p']))
