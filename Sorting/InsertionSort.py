numbers = [11, 2, 32, 9, 29, 0, 15, 40, 8, 1, 37]

for i in range(1, len(numbers)):
    currentValue = numbers[i]
    position = i
    while position > 0 and numbers[position-1] > currentValue:
        numbers[position] = numbers[position-1]
        position -=1
    numbers[position] = currentValue

print(numbers)
