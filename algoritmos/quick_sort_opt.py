def quick_sort_optimized(vector, low=0, high=None):

    if high is None:
        high = len(vector) - 1

    while low < high:

        pivot_index = partition(vector, low, high)

        # Recursão na menor partição
        if pivot_index - low < high - pivot_index:

            quick_sort_optimized(
                vector,
                low,
                pivot_index - 1
            )

            low = pivot_index + 1

        else:

            quick_sort_optimized(
                vector,
                pivot_index + 1,
                high
            )

            high = pivot_index - 1

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