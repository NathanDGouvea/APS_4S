def quick_sort_optimized(vector, low=0, high=None):
    
    if high == None:
        high = len(vector) - 1
        
    if low < high:
        pivot_index = partition(vector, low, high)
        
        quick_sort_optimized(vector, low, pivot_index - 1)
        quick_sort_optimized(vector, pivot_index + 1, high)
        
    return vector
        
        
        
        
def partition(vector, low, high):
    pivot = vector[high]
    i = low
    
    for j in range(low, high):
        if vector[j] < pivot:
            vector[j], vector[i] = vector[i], vector[j]
            i += 1
            
    vector[i], vector[high] = vector[high], vector[i]
    return i