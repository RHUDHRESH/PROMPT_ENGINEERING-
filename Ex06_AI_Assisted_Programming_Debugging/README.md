# Exp-6: AI-Assisted Programming and Debugging

**Due:** 25 Sep 2026 · **Reference repo:** RaajaThilahar/Ex.No.6

## Objective
Design prompts that get AI tools to write, debug, optimise, explain and test code in **Python, C and Java**, then compare manual vs AI-assisted coding.

## Task used: Binary search + intentionally buggy version
| Folder | Contents |
|---|---|
| `python/` | `binary_search_buggy.py`, `binary_search_fixed.py`, `test_binary_search.py` |
| `c/` | `binary_search_buggy.c`, `binary_search_fixed.c`, `test_binary_search.c` |
| `java/` | `BinarySearchBuggy.java`, `BinarySearch.java`, `BinarySearchTest.java` |
| `prompts/` | Prompts for generate / debug / optimise / complexity / unit tests |
| `bugs.md` | Bug list found (with how) |
| `code_quality_analysis.md` | Deliverable: manual vs AI comparison |

## Run
```
python3 python/test_binary_search.py
gcc c/test_binary_search.c c/binary_search_fixed.c -o c/t && ./c/t
cd java && javac BinarySearch.java BinarySearchTest.java && java BinarySearchTest
```


## Recorded run

Python passed locally (5 tests). C (6 checks) and Java (6 checks) compiled and passed in OneCompiler online on 2026-09-29. For the browser compiler, each implementation and its test cases were combined into one source file because the free editor uses a single-file harness. The original separate-file GCC/JDK commands above were not run locally; see validation_run.md.
