def mergeSort(list):
    if len(list) > 1:
        mid = len(list)/2

        leftHalf = list[:mid]
        rightHalf = list[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i, j, k = 0, 0, 0
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                list[k] = leftHalf[i]
                i += 1
            else:
                list[k] = rightHalf[j]
                j += 1
            k += 1

        while i < len(leftHalf):
            list[k] = leftHalf[i]
            i += 1
            k += 1

        while j < len(rightHalf):
            list[k] = rightHalf[j]
            j += 1
            k += 1

numbers = [11, 2, 32, 9, 29, 0, 15, 40, 8, 1, 37]
mergeSort(numbers)
print(numbers)
