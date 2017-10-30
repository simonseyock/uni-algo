import numpy as np

def get_monotonies(narr):
    length = len(narr)
    monotonies = np.zeros((length, length), dtype=int)
    for i in range(length - 1):
        for j in range(1, length):
            if narr[i] < narr[j]:
                monotonies[i, j] = 1
    return monotonies

def create_next_row(last, low, high):
    length = len(last)
    monotonies = get_monotonies(last)
    misplaced = True
    next = None
    while misplaced:
        next = np.random.randint(low, high, size=length)
        for k in range(length):
            misplaced = False
            for i in range(length - 1):
                for j in range(1, length):
                    if monotonies[i, j] == 1 and next[i] >= next[j]:
                        next[i], next[j] = next[j], next[i]
                        misplaced = True
            if not misplaced:
                break
    return next

def create_monotone_matrix(m, n, low, high):
    mat = [np.random.randint(low, high, size=n)]
    for i in range(1, m):
        mat.append(create_next_row(mat[i-1], low, high))
    return np.array(mat)

def find_left_max(matrix):
    result = np.ones(matrix.shape[0], dtype=int) * -1
    _find_left_max(matrix, 0, 0, matrix.shape[0] - 1, matrix.shape[1] - 1, result)
    return result

def _find_left_max(matrix, m1, n1, m2, n2, result):
    mid = m1 + (m2 - m1) // 2
    max_i = n1
    for i in range(n1 + 1, n2 + 1):
        if matrix[mid, i] > matrix[mid, max_i]:
            max_i = i
    result[mid] = max_i
    if mid - m1 > 0:
        _find_left_max(matrix, m1, n1, mid - 1, max_i, result)
    if m2 - mid > 0:
        _find_left_max(matrix, mid + 1, max_i, m2, n2, result)

def naive_find_left_max(matrix):
    result = np.ones(matrix.shape[0], dtype=int) * -1
    for m in range(matrix.shape[0]):
        max_i = 0
        for n in range(1, matrix.shape[1]):
            if matrix[m, n] > matrix[m, max_i]:
                max_i = m
        result[m] = max_i
    return result

mat = create_monotone_matrix(7, 7, 0, 10)
#mat = np.array([[1, 7, 3, 5, 4, 5, 8], [0, 6, 3, 5, 4, 5, 8], [0, 6, 3, 5, 4, 5, 7], [0, 8, 1, 5, 2, 5, 9], [2, 7, 3, 5, 4, 6, 9], [0, 8, 1, 3, 2, 4, 9], [1, 8, 4, 6, 5, 7, 9]])
print(mat)
res = find_left_max(mat)
print(res)