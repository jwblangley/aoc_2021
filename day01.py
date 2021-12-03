def get_num_increased(arr):
    res = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            res += 1
    return res
