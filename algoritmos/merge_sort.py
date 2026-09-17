def merge_sort(vector):
    size = len(vector)
    middle = size // 2
    
    if len(vector) <= 1:
        return vector
    
    left = merge_sort(vector[:middle])
    right = merge_sort(vector[middle:])
    
    total = []
    size_left = len(left)
    size_right = len(right)
    
    i = 0
    j = 0
    
    while i < size_left and j < size_right:
        if (left[i] > right[j]):
            total.append(right[j])
            j += 1
        else:
            total.append(left[i])
            i += 1
            
    while i < size_left:
        total.append(left[i])
        i += 1

    while j < size_right:
        total.append(right[j])
        j += 1
        
        
    
    return total