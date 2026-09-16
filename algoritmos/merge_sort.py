def merge_sort(vector):
    size = len(vector)
    middle = size // 2
    
    if len(vector) <= 1:
        return vector
    
    left = merge_sort(vector[:middle])
    right = merge_sort(vector[middle:])
    
    total = []
    sizel = len(left)
    sizer = len(right)
    
    i = 0
    j = 0
    
    while i < sizel and j < sizer:
        if (left[i] > right[j]):
            total.append(right[j])
            j += 1
        else:
            total.append(left[i])
            i += 1
            
    while i < sizel:
        total.append(left[i])
        i += 1

    while j < sizer:
        total.append(right[j])
        j += 1
        
        
    
    return total