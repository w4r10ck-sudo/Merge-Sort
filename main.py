# Merge sort
def merge(arr1, arr2):  # merging two arrays
    arr1.extend(arr2)  # extending list arr1 with arr2
    arr1.sort()
    return arr1


def merge_sort(tmp_arr):
    l = len(tmp_arr)
    if l == 1:
        return tmp_arr

    mid = int(len(tmp_arr) / 2)
    a1 = merge_sort(tmp_arr[:mid])
    a2 = merge_sort(tmp_arr[mid:])
    return merge(a1, a2)


arr = input().split()
arr = [int(i) for i in arr]  # converting list of string type numbers to int
print(merge_sort(arr))
