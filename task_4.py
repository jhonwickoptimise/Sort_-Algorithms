#Bubble Sort algorithm:

"""ef bubble_sort(arr):
    # Get the length of the list
    n = len(arr)
    
    # Traverse through all list elements
    for i in range(n):
        # Track if any swaps are made during the current iteration
        swapped = False
        
        # Last i elements are already sorted, no need to check them
        for j in range(0, n - i - 1):
            
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if elements are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no two elements were swapped in the inner loop, the list is already sorted
        if not swapped:
            break
    
    return arr

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted array:", arr)
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)
"""
#Selection Sort algorithm:

def selection_sort(arr):
    # Traverse through all array elements
    n = len(arr)
    
    for i in range(n):
        # Find the index of the minimum element in the unsorted part
        min_index = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted array:", arr)
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)
