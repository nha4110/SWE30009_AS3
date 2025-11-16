import os
import sys
import random

# === Setup path ===
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from SUT.quick_sort import quick_sort

# === Precompute correct outputs from ORIGINAL SUT ===
mr1_groups = [([3,1,4],10), ([-5,2,-1],-3), ([1,1,2],5), ([10],0), ([],7)]
mr2_groups = [[3,1,4], [-5,2,-1], [1,1,2], [5,10,15], [7,3,9,1]]

expected_mr1 = {tuple(src): quick_sort(src) for src, _ in mr1_groups}
expected_mr2 = {tuple(src): quick_sort(src) for src in mr2_groups}

def test_mutant(mutant_path):
    # Import mutant
    sys.path.insert(0, os.path.dirname(mutant_path))
    mod_name = os.path.basename(mutant_path).replace('.py', '')
    try:
        mod = __import__(mod_name)
        qs = mod.quick_sort
    except Exception:
        return True, True, True  # Import fail = killed by both

    killed_by_mr1 = False
    killed_by_mr2 = False

    # === MR1: Constant Offset ===
    for src, k in mr1_groups:
        fup = [x + k for x in src]
        try:
            result = qs(fup)
            expected = [y + k for y in expected_mr1[tuple(src)]]
            if result != expected:
                killed_by_mr1 = True
                break
        except Exception:
            killed_by_mr1 = True
            break

    # === MR2: Permutation Invariance ===
    for src in mr2_groups:
        fup = src[:]
        random.seed(42)  # Reproducible shuffle
        random.shuffle(fup)
        try:
            result = qs(fup)
            if result != expected_mr2[tuple(src)]:
                killed_by_mr2 = True
                break
        except Exception:
            killed_by_mr2 = True
            break

    final_killed = killed_by_mr1 or killed_by_mr2
    return final_killed, killed_by_mr1, killed_by_mr2

# === RUN ALL 30 MUTANTS ===
print("MUTANT".ljust(8), "MR1".ljust(10), "MR2".ljust(10), "STATUS")
print("-" * 45)

total_killed = 0
mr1_killed_count = 0
mr2_killed_count = 0

for i in range(1, 31):
    path = os.path.join("..", "MUTANTS", f"mutant_{i}.py")
    if not os.path.exists(path):
        print(f"{i:2d}      {'MISSING':<10} {'MISSING':<10} MISSING")
        continue

    killed, mr1_k, mr2_k = test_mutant(path)
    mr1_str = "KILLED" if mr1_k else "SURVIVED"
    mr2_str = "KILLED" if mr2_k else "SURVIVED"
    status = "KILLED" if killed else "SURVIVED"

    if killed:
        total_killed += 1
    if mr1_k:
        mr1_killed_count += 1
    if mr2_k:
        mr2_killed_count += 1

    print(f"{i:2d}      {mr1_str:<10} {mr2_str:<10} {status}")

# === Final Scores ===
score = (total_killed / 30) * 100
mr1_score = (mr1_killed_count / 30) * 100
mr2_score = (mr2_killed_count / 30) * 100

print(f"\nMUTATION SCORE:")
print(f"  MR1 (Offset):      {mr1_score:.1f}% ({mr1_killed_count}/30)")
print(f"  MR2 (Permutation): {mr2_score:.1f}% ({mr2_killed_count}/30)")
print(f"  OVERALL:           {score:.1f}% ({total_killed}/30 killed)")