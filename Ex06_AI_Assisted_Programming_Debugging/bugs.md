# Bugs found

| # | Lang | Bug | Failing input | Found by (manual/AI) | Fix |
|---|---|---|---|---|---|
| 1 | Python | `hi = len(arr)` off-by-one | `[5]`, target 5 (index error risk with inclusive logic) | | `hi = len(arr) - 1` |
| 2 | Python | `lo < hi` skips last candidate | `[5]`, target 5 -> -1 | | `lo <= hi` |
| 3 | Python/C | `lo = mid` infinite loop | `[1,3]`, target 3 | | `lo = mid + 1` |
| 4 | C/Java | `(lo+hi)/2` overflow | n near INT_MAX | | `lo + (hi-lo)/2` |
| 5 | Java | `lo < hi` misses element | `{5}`, target 5 | | `lo <= hi` |
