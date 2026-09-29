# Prompt set (use once per language)

## 1. Generate
```
Write a {{language}} function binary_search(arr, target) returning the index or -1 for a sorted array. Handle empty arrays and avoid integer overflow. Add comments.
```
## 2. Identify bugs
```
Find all bugs in this {{language}} code. For each: line, why it fails, failing input, fix.
{{code}}
```
## 3. Optimise
```
Optimise this code for readability and performance without changing behaviour. Explain each change and any trade-off.
{{code}}
```
## 4. Complexity
```
State the time and space complexity (best/avg/worst) of this code and justify with the recurrence or loop bound.
{{code}}
```
## 5. Unit tests
```
Write unit tests for this function covering: empty array, single element (hit/miss), first/last element, duplicates, target smaller/larger than all, large array. Use {{framework}}.
{{code}}
```
## 6. Compare manual vs AI
```
Given my manual solution and yours, list differences in correctness, edge cases, style and complexity.
```
