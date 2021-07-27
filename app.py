def find_even_index(arr):
    first = arr[0]
    last = arr[-1]
    index = 0
    if sum(arr) == 0:
        index = 0
        return index
    if first == sum(arr[1:]):
        index = 0
    if last == sum(arr[:-1]):
        index = last
        return len(arr) - 1
    for i in range(1, len(arr)):
        if sum(arr[:i]) == sum(arr[-1:i:-1]):
            index = i
            break
        else:
            index = -1
    return index
