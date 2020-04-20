number = [1, 8, 11, 17, 21, 24, 29, 30, 35, 42, 47]
item = int(input("Please enter number to search for: "))
found = False
position = 0
while found == False and position < len(number):
    if number[position] == item:
        found = True
    else:
        position += 1
if found == True:
    print("Item found at position " + str(position))
else:
    print("Item not found")
