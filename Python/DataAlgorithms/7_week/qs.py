def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left, right = [], []

    for i in arr[:-1]:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)

    return quicksort(left) + [pivot] + quicksort(right)

def quicksort2(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left, right = [], []

    for i in arr[1:]:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)

    return quicksort2(left) + [pivot] + quicksort2(right)


def quicksort3(arr):
    if len(arr) <= 1:
        return arr

    pivot_idx = len(arr) // 2
    pivot = arr[pivot_idx]
    left, right = [], []

    for i in range(len(arr)):
        if i == pivot_idx:
            continue
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quicksort3(left) + [pivot] + quicksort3(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    sorted_arr = merge(left_half, right_half)

    return sorted_arr

def merge(left, right):
    result = []
    i = j = 0

    # Merge the two sub-arrays in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements from both sub-arrays (if any)
    result.extend(left[i:])
    result.extend(right[j:])

    return result



# Example usage
arr = [14, 1, 2, 6, 11, 8, 5, 9, 4, 3, 10, 7, 12, 13]
arr2 = [1,3,2,4,5,6,8,7,9,10,11,13,12,14]

sorted_arr = quicksort(arr)
print(sorted_arr)

#sorted_arr2 = quicksort2(arr)
# #print(sorted_arr2)

sorted_arr3 = quicksort3(arr)
print(sorted_arr3)

#sortedArr1 = quicksort(arr2)
#print(sortedArr1)

#sorted_arr4 = merge_sort(arr2)
#print(sorted_arr4)

