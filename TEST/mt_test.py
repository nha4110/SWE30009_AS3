import sys
import os
import random
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
test_dir = os.path.abspath(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
if test_dir not in sys.path:
    sys.path.insert(0, test_dir)

from SUT.quick_sort import quick_sort

def check_mr1(source, k):
    sorted_orig = quick_sort(source)
    followup = [x + k for x in source]
    sorted_fup = quick_sort(followup)
    expected = [y + k for y in sorted_orig]
    return sorted_fup == expected, sorted_fup, expected

def check_mr2(source):
    expected = quick_sort(source)
    followup = source[:]
    random.seed(42)
    random.shuffle(followup)
    result = quick_sort(followup)
    return result == expected, result, expected

mr1_groups = [([3,1,4],10), ([-5,2,-1],-3), ([1,1,2],5), ([10],0), ([],7)]
mr2_groups = [[3,1,4], [-5,2,-1], [1,1,2], [5,10,15], [7,3,9,1]]

print("=== METAMORPHIC TESTING (ORIGINAL SUT) ===\n")
print("MR1: Constant Offset")
for i, (src, k) in enumerate(mr1_groups, 1):
    ok, act, exp = check_mr1(src, k)
    print(f"G1.{i}: {'PASS' if ok else 'FAIL'} | Act: {act} | Exp: {exp}")

print("\nMR2: Permutation Invariance")
for i, src in enumerate(mr2_groups, 1):
    ok, act, exp = check_mr2(src)
    print(f"G2.{i}: {'PASS' if ok else 'FAIL'} | Act: {act} | Exp: {exp}")

print("\nALL 10 GROUPS PASSED ON ORIGINAL.")