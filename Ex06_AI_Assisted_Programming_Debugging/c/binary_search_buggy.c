int binary_search(const int *arr, int n, int target) {
    int lo = 0, hi = n - 1;
    while (lo <= hi) {
        int mid = (lo + hi) / 2;   /* BUG 1: (lo+hi) can overflow int for huge n */
        if (arr[mid] == target) return mid;
        if (arr[mid] < target) lo = mid; /* BUG 2: infinite loop, should be mid + 1 */
        else hi = mid - 1;
    }
    return -1;
}
