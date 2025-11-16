def quick_sort(arr):
    if len(arr) <= 1: return arr
    pivot = arr[-1]                     # last element
    left  = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + quick_sort(right)   # ← no middle → duplicates lost