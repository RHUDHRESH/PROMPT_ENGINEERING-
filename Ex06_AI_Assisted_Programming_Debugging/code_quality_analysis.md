# Code Quality Analysis - Manual vs AI-assisted

**Measurement note.** No stopwatch, no manual (human-only) implementation and no separate AI-only timing exist for this exercise. Metrics that need them are marked "not measured". Observations below come from running the code in this folder.

| Metric | Manual coding | AI-assisted | Notes |
|---|---|---|---|
| Time to first working version (min) | not measured | not measured | No timings were recorded |
| Bugs at first run | not measured | Buggy files: Python 3 planted bugs (2 observable: wrong result, hang; 1 masked), C 2 (1 hang, 1 latent overflow), Java 2 (1 wrong result, 1 latent overflow). Fixed files: 0 failures | See `bugs.md`. The buggy files are deliberately broken samples, not an AI's first attempt |
| Edge cases handled | not measured | Fixed versions handle empty array, single element hit/miss, first/last element, missing below/above range, 500k-element array (Python). Not tested: duplicates (returns some matching index, not necessarily the first), unsorted input, `None`, C `n < 0`, real overflow-sized arrays | |
| Test coverage | not measured | Python 5 tests, C 6 checks, Java 6 checks; no coverage tool was run so no percentage is claimed | Tests miss "target greater than all elements", which is exactly what triggers the hang in the buggy code |
| Readability / comments | not measured | Fixed versions are short and use the same structure across three languages; one-line docstring/Javadoc with complexity; C has no comment | |
| Complexity stated correctly | not measured | Yes: O(log n) time, O(1) space iterative (matches the code) | See the section below |
| Languages done (Py/C/Java) | not measured | Python, C, Java all have buggy, fixed and test files, and all fixed versions pass | |

## Findings
1. **Where AI helped most:** Running the buggy code in three languages and exhaustively in Python (34 cases) showed exactly which bugs manifest and on which inputs, faster and more completely than reading the code.
2. **Where AI (or the earlier notes) was wrong or overconfident:** The earlier `bugs.md` claimed `[5]`, target 5 fails in Python and that `hi = len(arr)` risks an index error. Running it showed both claims are false for the shipped file: bugs 1 and 2 mask each other on that input, and `[1,3]` target 3 returns 1 correctly (the earlier table said it hangs). Reading code and asserting failures without running gave wrong claims. Overflow bugs (C and Java) could not be reproduced with a real array and are reported as latent.
3. **What I would still do manually:** Decide the intended semantics for duplicates (first or any match), review test adequacy (the tests miss the hang trigger), and run the overflow scenario on a machine with enough memory if it matters.

## Complexity

Iterative binary search on a sorted array of n elements. Each iteration halves the remaining range `[lo, hi]`, so the loop runs at most floor(log2 n) + 1 times.

| Case | Time | Why |
|---|---|---|
| Best | O(1) | Target is the middle element and is found on the first probe |
| Average | O(log n) | About log2(n) - 1 probes for a successful search; about log2(n) for an unsuccessful one |
| Worst | O(log n) | Target absent or at the last remaining position: T(n) = T(n/2) + O(1) gives log2 n + 1 probes (about 20 for 10^6 elements) |
| Space | O(1) | Only lo, hi, mid; no recursion |

The recursive form would use O(log n) stack space. The buggy `lo = mid` versions have no valid bound: they loop forever on some inputs.

## Optimisation note
The fixed code is already asymptotically optimal for comparison-based search on a sorted array. Changes worth keeping: `lo + (hi-lo)//2` avoids overflow in C and Java (in Python it is harmless because ints are unbounded); `<=` loop condition with `mid+1` / `mid-1` guarantees progress. Possible micro-optimisations (not applied, not measured): use Python's `bisect.bisect_left` (C implementation, and it returns the leftmost match for duplicates); in C, a branchless variant or `size_t`/unsigned indexes for arrays above INT_MAX. For very few elements a linear scan can be faster due to branch prediction, but this was not benchmarked. Trade-off: extra variants reduce readability for gains that were not measured.
