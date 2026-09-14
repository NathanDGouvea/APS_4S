def bubble_sort(vector):
    size = len(vector)

    for i in range(size):
        for j in range(0, size - i - 1):

            if vector[j] > vector[j + 1]:
                vector[j], vector[j + 1] = vector[j + 1], vector[j]

    return vector


