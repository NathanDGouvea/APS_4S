def selection_sort(vector):
    size = len(vector)
    
    for i in range(size):
        lowest = i
        for j in range(i + 1, size):
            if vector[j] < vector[lowest]:
                lowest = j
                
        if lowest != i:
            vector[i], vector[lowest] = vector[lowest], vector[i]
    
    return vector