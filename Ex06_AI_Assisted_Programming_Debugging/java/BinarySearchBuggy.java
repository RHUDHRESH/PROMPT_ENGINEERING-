public class BinarySearchBuggy {
    static int search(int[] a, int t) {
        int lo = 0, hi = a.length - 1;
        while (lo < hi) {                 // BUG 1: should be lo <= hi (misses single remaining element)
            int mid = (lo + hi) / 2;      // BUG 2: overflow risk
            if (a[mid] == t) return mid;
            if (a[mid] < t) lo = mid + 1; else hi = mid - 1;
        }
        return -1;
    }
}
