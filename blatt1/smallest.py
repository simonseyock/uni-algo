import random

def sweepLeft(arr, k):
    if arr[k] < 0:
        while k >= 2 and abs(arr[k - 2]) > arr[k-1] and abs(arr[k]) > arr[k-1]:
            arr[k - 2] = arr[k - 2] + arr[k - 1] + arr[k]
            k = k - 2
    return k

def smallest(arr):
    values = [0] * len(arr)
    lefts = [0] * len(arr)
    rights = [0] * len(arr)
    current = arr[0]
    k = 0

    for i in range(1, len(arr)):
        if arr[i] * current >= 0:
            current += arr[i]
        else:
            values[k] = current
            k = sweepLeft(values, k)
            rights[k] = i - 1
            k = k + 1
            current = arr[i]
            lefts[k] = i

    values[k] = current
    k = sweepLeft(values, k)
    rights[k] = len(arr) - 1

    if k == 0 and values[0] > 0:
        index = arr.index(min(arr))
        return index, index
    else:
        index = values.index(min(values[:k+1]))
        return lefts[index], rights[index]

def smallestNaive(arr):
    min = arr[0]
    left = 0
    right = 0
    for l in range(0, len(arr)):
        current = 0
        for r in range(l, len(arr)):
            current += arr[r]
            if current < min:
                min = current
                left = l
                right = r
    return left, right

# print smallest([-10, -1, -18, -36, 82, -5, 73, 57, 22, -65, -61, 36, -7, 21, -17, -19])

# print smallest([1, 2, -2, 3, 2, -4, 1, -5])
# print smallestNaive([1, 2, -2, 3, 2, -4, 1, -5])
#
# print smallest([2, 2, 3, 4, 5, 1 ,6])
# print smallestNaive([2, 2, 3, 4, 5, 1 ,6])
#
# print smallest([-66, -24, 6, -34, -43, -87, 1, -82, 55, 13])
# print smallestNaive([-66, -24, 6, -34, -43, -87, 1, -82, 55, 13])
#
# print smallest([72, 82, 92, -36, -62, 77, 98, 84, 75, -64, 31, 70, 9, 7, -17, -60])
# print smallestNaive([72, 82, 92, -36, -62, 77, 98, 84, 75, -64, 31, 70, 9, 7, -17, -60])
# print smallest([72, 82, 92, -36, -62, 77, 98, 84, 75, -64, 22, 1, 9, 7, -17, -60])
# print smallestNaive([72, 82, 92, -36, -62, 77, 98, 84, 75, -64, 22, 1, 9, 7, -17, -60])
#
for i in range(0,20):
    arr = random.sample(xrange(-100, 100), 16)
    print arr
    print smallest(arr)
    print smallestNaive(arr)