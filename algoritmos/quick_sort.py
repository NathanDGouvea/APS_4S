def quick_sort(vector, pivot_strategy="random"):
    
    size = len(vector)
    
    if size <= 1:
        return vector
    
    if pivot_strategy == "middle":
        pivot_index = size // 2
    elif pivot_strategy == "end":
        pivot_index = size - 1
    else:
        import random
        pivot_index = random.randint(0, size - 1)
        
    pivot = vector[pivot_index]
        
            
    left = []
    right = []
    
    for i, value in enumerate(vector):
        if i == pivot_index:
            continue
        
        if value < pivot:
            left.append(value)
        else:
            right.append(value)
            
    left = quick_sort(left, pivot_strategy)
    right = quick_sort(right, pivot_strategy)
    
    total = left + [pivot] + right
    
    
    return total
