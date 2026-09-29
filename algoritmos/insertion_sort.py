def insertion_sort(vector):
    
    size = len(vector)

    for i in range(1, size):
        key = vector[i]
        j = i - 1

        while j >= 0 and vector[j] > key:
            vector[j + 1] = vector[j]
            j -= 1

        vector[j + 1] = key

    return vector