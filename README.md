SWE30009 - Software Testing and Reliability
Assignment 3 - Task 2
Student: Lu Nhat Hoang
Student ID: 105234956

=== SOURCE OF THE PROGRAM UNDER TEST (SUT) ===
Program: Quick Sort (recursive implementation)
Language: Python 3
Original Source:
https://github.com/TheAlgorithms/Python/blob/master/sorts/quick_sort.py

File: SUT/quick_sort.py
Description:
This is a standard recursive Quick Sort algorithm that:
- Selects the middle element as pivot
- Partitions into left (< pivot), middle (== pivot), right (> pivot)
- Recursively sorts left and right
- Handles duplicates correctly
- Base case: arrays of size <= 1

The program was downloaded on 16 November 2025 and is used unmodified as the System Under Test (SUT).

=== FOLDER STRUCTURE ===
SUT/             → Original program + this readme
MUTANTS/         → 30 non-equivalent mutants (mutant_1.py to mutant_30.py)
TEST/            → Test scripts and outputs
    ├── mt_test.py          → Runs 10 metamorphic test groups (MR1 + MR2)
    ├── mut_test.py         → Runs all 30 mutants against MR1 and MR2
    ├── mt_output.png       → Screenshot: All 10 groups passed
    └── mut_output.png      → Screenshot: Mutation score 83.3%


how to run the project
to test the orignal:

cd TEST

python mt_test.py  

to test all the mutants:

cd TEST

python mut_test.py  
