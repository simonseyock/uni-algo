import matplotlib.pyplot as plt
import numpy as np
import time


def _merge(arr, l, m, r):
    L = np.concatenate((arr[l:m+1], [float('+inf')]), 0)
    R = np.concatenate((arr[m+1:r+1], [float('+inf')]), 0)
    li = 0
    ri = 0
    for i in range(l, r+1):
        if L[li] < R[ri]:
            arr[i] = L[li]
            li = li + 1
        else:
            arr[i] = R[ri]
            ri = ri + 1


def _merge_sort(arr, l, r):
    if l != r:
        m = l + (r - l) // 2
        _merge_sort(arr, l, m)
        _merge_sort(arr, m+1, r)
        _merge(arr, l, m, r)


def merge_sort(arr):
    _merge_sort(arr, 0, len(arr) - 1)


def insert_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > val:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = val


def get_time(fn, n, height):
    sample = np.random.randint(height, size=n)
    start = time.process_time()
    fn(sample)
    return time.process_time() - start


def get_avg_time(fn, n, height):
    return np.mean(np.vectorize(lambda m: get_time(fn, m, height))(np.ones(min(n, 200), dtype=int) * n))


ns = np.arange(1, 501, 1)
avg_merge_sorts = np.vectorize(lambda n: get_avg_time(merge_sort, n, 1000))(ns)
avg_insert_sorts = np.vectorize(lambda n: get_avg_time(insert_sort, n, 1000))(ns)

plt.plot(ns, avg_merge_sorts, label='merge sort')
plt.plot(ns, avg_insert_sorts, label='insert sort')
plt.legend(loc='best')
plt.show()