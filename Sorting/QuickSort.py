def partition(list, left, right, pivot):
    while left <= right:
        while list[left] < pivot:
            left += 1
        while list[right] > pivot:
            right -= 1
        if left <= right:
            list[left], list[right] = list[right], list[left]
            left += 1
            right -= 1
    return left

def quicksort(list, left, right):
    if left < right:
        pivot = list[(left+right)/2]
        index = partition(list, left, right, pivot)
        quicksort(list, left, index - 1)
        quicksort(list, index, right)
    return list

numbers = [11, 2, 32, 9, 29, 0, 15, 40, 8, 1, 37]
print(quicksort(numbers, 0, len(numbers) - 1))
