public class BinarySearchTest {
    static int failures = 0;
    static void eq(int exp, int got, String name) {
        if (exp != got) { failures++; System.out.println("FAIL " + name + ": expected " + exp + " got " + got); }
    }
    public static void main(String[] args) {
        int[] a = {1, 3, 5, 7, 9};
        eq(-1, BinarySearch.search(new int[]{}, 1), "empty");
        eq(0, BinarySearch.search(a, 1), "first");
        eq(4, BinarySearch.search(a, 9), "last");
        eq(-1, BinarySearch.search(a, 4), "missing");
        eq(0, BinarySearch.search(new int[]{5}, 5), "single hit");
        eq(-1, BinarySearch.search(new int[]{5}, 4), "single miss");
        System.out.println(failures == 0 ? "All Java tests passed" : failures + " failure(s)");
        if (failures > 0) System.exit(1);
    }
}
