def quick_sort_last_pivot(vector):
    size = len(vector)
    
    if size <= 1:
        return vector
    
    pivot = vector[-1]
        
            
    left = []
    right = []
    
    for value in vector[:-1]:
        
        if value < pivot:
            left.append(value)
        else:
            right.append(value)
            
    left = quick_sort_last_pivot(left)
    right = quick_sort_last_pivot(right)
    
    total = left + [pivot] + right
    
    return total
