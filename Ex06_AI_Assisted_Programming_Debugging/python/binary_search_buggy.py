def binary_search(arr, target):
    lo, hi = 0, len(arr)          # BUG 1: hi should be len(arr) - 1
    while lo < hi:                # BUG 2: skips the last candidate with inclusive hi
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid              # BUG 3: infinite loop, should be mid + 1
        else:
            hi = mid - 1
    return -1
