def bubble_sort_optimized(vector):
    
    size = len(vector)

    for i in range(size):
        change = False

        for j in range(0, size - i - 1):

            if vector[j] > vector[j + 1]:
                vector[j], vector[j + 1] = vector[j + 1], vector[j]
                change = True

        if not change:
            break

    return vector