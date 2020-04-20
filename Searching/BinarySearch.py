number = [1, 8, 11, 17, 21, 24, 29, 30, 35, 42, 47]
lowerbound = 0
upperbound = len(number)
found = False
search = int(input("Please search for a number: "))
while found == False and lowerbound != upperbound:
    midpoint = round((lowerbound + upperbound)/2)
    if number[midpoint] == search:
        found = True
    elif number[midpoint] > search:
        upperbound = midpoint - 1
    elif number[midpoint] < search:
        lowerbound = midpoint + 1
if found == True:
    print("Item found at position "+str(midpoint))
else:
    print("Item not found")
