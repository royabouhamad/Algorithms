numbers = [11, 2, 32, 9, 29, 0, 15, 40, 8, 1, 37]
swapMade = True
while swapMade == True:
    swapMade = False
    for i in range(0, len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
            swapMade = True
print(numbers)
