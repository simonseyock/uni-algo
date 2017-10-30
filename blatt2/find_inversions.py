import numpy as np

def _find_inversions_merge(arr, l, m, r):
    L = np.concatenate((arr[l:m+1], [float('+inf')]), 0)
    R = np.concatenate((arr[m+1:r+1], [float('+inf')]), 0)
    li = 0
    ri = 0
    inversions = 0
    for i in range(l, r+1):
        if L[li] <= R[ri]:
            inversions += inversions
            arr[i] = L[li]
            li = li + 1
        else:
            inversions += 1
            arr[i] = R[ri]
            ri = ri + 1
    return inversions


def _find_inversions_eff(arr, l, r):
    inversions = 0
    if l != r:
        m = l + (r - l) // 2
        inversions += _find_inversions_eff(arr, l, m)
        inversions += _find_inversions_eff(arr, m+1, r)
        inversions += _find_inversions_merge(arr, l, m, r)
    return inversions

def find_inversions_eff(arr):
    return _find_inversions_eff(np.copy(arr), 0, len(arr) - 1)

def find_inversions_naive(arr):
    inversions = 0
    for i in range(len(arr)-1):
        for j in range(1, len(arr)):
            if arr[i] > arr[j]:
                inversions += 1
    return inversions

print(find_inversions_eff(np.array([88, 20, 77, 63, 59, 7, 16, 2])))

def compare(sampler, fn1, fn2, comparer, n):
    for i in range(n):
        sample = sampler()
        if not comparer(fn1(sample), fn2(sample)):
            raise('Not equal! Input: ' + sample)
    print('all equal')

compare(lambda: np.random.randint(100, size=8), find_inversions_eff, find_inversions_naive, lambda a, b: a==b, 10)

