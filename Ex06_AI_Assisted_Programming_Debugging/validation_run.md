# Browser compilation run: Experiment 6

Date: 2026-09-29  
Online compiler: OneCompiler C and Java editors (`onecompiler.com/c` and `onecompiler.com/java`).  
Result: **All C tests passed** and **All Java tests passed**.

The local environment has no `gcc`, `clang`, MSVC `cl`, `javac` or `java` executable. To finish the checks in the browser, I placed each implementation with its equivalent bundled checks into a single editor source: six C checks and six Java checks. The browser compiler reported success for both. The repository's original separate-file build commands were not run locally, and compiler warnings were not recorded. Python's five-test suite had already passed locally.