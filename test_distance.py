# file: test_distance.py
from distance import euclidean_distance

def test_MR1():
    A = (1, 2)
    B = (3, 4)
    d1 = euclidean_distance(*A, *B)
    d2 = euclidean_distance(*B, *A)
    return abs(d1 - d2) < 1e-6  # True if MR holds

def test_MR2():
    A = (1, 2)
    B = (3, 4)
    k = 2
    d1 = euclidean_distance(*A, *B)
    d2 = euclidean_distance(*(k*A[0], k*A[1], k*B[0], k*B[1]))
    return abs(d2 - abs(k)*d1) < 1e-6

if __name__ == "__main__":
    print("MR1 holds:", test_MR1())
    print("MR2 holds:", test_MR2())
