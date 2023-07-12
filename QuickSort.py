def quick_sort(arr):
    if len(arr) < 2:
        return arr
    mid_index = len(arr) // 2
    left, mid, right = [], [], []
    for item in arr:
        if item > arr[mid_index]:
            right.append(item)
        elif item == arr[mid_index]:
            mid.append(item)
        elif item < arr[mid_index]:
            left.append(item)
    return quick_sort(left) + mid + quick_sort(right)

