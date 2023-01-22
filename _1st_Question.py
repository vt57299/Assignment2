# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples

def last_element(tpl):     
    return tpl[-1]

def sort(tuple):                                                              
    return sorted(tuple, key = last_element)

lst = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print("Sorted list:\n", sort(lst))
