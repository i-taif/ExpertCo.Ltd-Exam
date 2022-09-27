# fuction that sorts it alphabetically
# def sortAlphabetic(listName:list) -> list:
#     stringAsciiLowerCase=''.join(chr(i) for i in range(97,123))
#     for i in listName:
#         if i in stringAsciiLowerCase:
#             a=stringAsciiLowerCase.index(i)

def quicksort(lst):
    if not lst:
        return []
    return (quicksort([x for x in lst[1:] if x <  lst[0]])
            [lst[0]] +
            quicksort([x for x in lst[1:] if x >= lst[0]]))
lst = ['b', 'd', 'a', 'e', 'c',]
a=[x for x in lst[1:] if x <  lst[0]]
print(a)
